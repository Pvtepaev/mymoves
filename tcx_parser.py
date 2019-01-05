#!/usr/bin/python3
# -*- coding: utf-8 -*-
#tcx_parser_1-2
#
from app import app
import xml.etree.cElementTree as ET
import pymysql
import datetime as DT
from datetime import datetime
import time
from config import Configuration


def mainfunction():
    global tcx_file
    global UserId
#TEmporary!!!!
##    print("Введите имя файла:")
#    tcx_file = input()
    UserId = 1
    tcx_file = '../upload/test.tcx'
    parsetcx(tcx_file, UserId)

def parsetcx(tcx_file, UserId):
    """
    Парсинг XML используя ElementTree
    """
    tree = ET.ElementTree(file=tcx_file)
    root = tree.getroot()

    ns = 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'
    StringId = 1
    global connection
    connection = pymysql.connect(host='localhost', user = app.config['DATABASE_USER'], password = app.config['DATABASE_PASSWORD'], db= app.config['DATABASE'], port=3306, charset='utf8mb4')

    selectstring = "SELECT Hrmin, Hrmax, HRThreshold, PaceThreshold FROM UserDetails WHERE ID = " + str(UserId)
    Result = list(getdb(selectstring))
    Hrmin = Result[0]
    Hrmax = Result[1]
    HRThreshold = Result[2]
    PaceThreshold = Result[3]
    SpeedThreshold = 1 / (float(PaceThreshold.seconds) / 1000)

    for Activities in root.findall('{%s}Activities' %(ns)):
        for Activity in Activities.findall('{%s}Activity' %(ns)):
            ActivityType = str(Activity.attrib)
            Id = Activity.find('{%s}Id' %(ns))
            ActivityStartTime = (str(Id.text)[0:-1]).replace('T', ' ')
            MoveId = 'Move_' + ((Id.text).replace(':', '_').replace('-','_').replace('T', '_'))[0:-1]
#Здесь  проверяем есть ли уже таблица с такаим именем. Или проверить наличие записи в таблице Moves
            SelectMoveString = "SELECT MoveID FROM Moves WHERE MoveID = " + "\'" + MoveId + "\'"
            Result = getdb(SelectMoveString)
            if Result == None:

#Создаем таблицу Move_XXX
                with connection.cursor() as cursor:
                    create_table = 'create table ' + MoveId + ' (Id varchar(128), Activity varchar(128), LapNum smallint, LapStartTime DATETIME, LapDuration TIME, DistanceMeters decimal(9,3), MaximumSpeed decimal(9,3), Calories decimal(9,3), Timedelta time, Time datetime, Latitude decimal(12,6), Longitude decimal(12,6), Altitude decimal(9,3), Cadence decimal(6,3), Speed decimal(9,3), Pace TIME, HeartRate decimal(5,2), HRZone varchar(128), PaceZone varchar(128), HrateIF decimal(4,2), PaceIF decimal(4,2), hrTSS decimal(5,3), pTSS decimal(5,3))'
                    cursor.execute(create_table)
                connection.commit()
                LapNum = 0

#ИЗвлекаем из XML данные
                for Lap in Activity.findall('{%s}Lap' %(ns)):
                    LapNum += 1
                    LapStartTimeTemp = str(Lap.attrib)
                    LapStartTime = LapStartTimeTemp[15:-3].replace('T', ' ')
                    TotalTimeSeconds =  Lap.find('{%s}TotalTimeSeconds' %(ns))
                    LapDuration = DT.timedelta(float(TotalTimeSeconds.text)/(60*60*24))
                    DistanceMeters = Lap.find('{%s}DistanceMeters' %(ns))
                    MaximumSpeed = Lap.find('{%s}MaximumSpeed' %(ns))
                    Calories = Lap.find('{%s}Calories' %(ns))
                    Intencity = Lap.find('{%s}Intencity' %(ns))
                    for Track in Lap.findall('{%s}Track' %(ns)):
                        for Trackpoint in Track.findall('{%s}Trackpoint' %(ns)):
                            Timepoint = (str((Trackpoint.find('{%s}Time' %(ns))).text).replace('T', ' '))[0:-1]
                            for Position in Trackpoint.findall('{%s}Position' %(ns)):
                                LatitudeDegrees = Position.find('{%s}LatitudeDegrees' %(ns))
                                LongitudeDegrees = Position.find('{%s}LongitudeDegrees' %(ns))
                            AltitudeMeters = Trackpoint.find('{%s}AltitudeMeters' %(ns))
                            if AltitudeMeters == None:
                                Altitude = 0
                            else:
                                Altitude = float(AltitudeMeters.text)
                            for HeartRateBpm in Trackpoint.findall('{%s}HeartRateBpm' %(ns)):
                                HeartRateValue = HeartRateBpm.find('{%s}Value' %(ns))
                            if float(HeartRateValue.text) == None:
                                HeartRate = 0
                            else:
                                HeartRate = int(HeartRateValue.text)
                            CadenceTemp = Trackpoint.find('{%s}Cadence' %(ns))
                            if CadenceTemp == None:
                                Cadence = 0
                            else:
                                Cadence = float(CadenceTemp.text)
                            for Extensions in Trackpoint.findall('{%s}Extensions' %(ns)):
                                for TPX in Extensions.findall('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TPX'):
                                    Speed = TPX.find('{http://www.garmin.com/xmlschemas/ActivityExtension/v2}Speed')
                                    if float(Speed.text) == 0:
                                        Pace = 0
                                    else:
                                        Pace = time.strftime('%H:%M:%S', time.gmtime(1000 / float(Speed.text)))

                                    Timedelta = (datetime.strptime(Timepoint , '%Y-%m-%d %H:%M:%S') - datetime.strptime(ActivityStartTime, '%Y-%m-%d %H:%M:%S'))
#TODO to calculate zones
                                    PaceIF = float(Speed.text) / SpeedThreshold
                                    HrateIF = (HeartRate - Hrmin) / (HRThreshold - Hrmin)
                                    hrTSS = 100 * HrateIF / 3600
                                    pTSS = 100 * PaceIF / 3600
#
#Записываем данные в таблицу
                                    with connection.cursor() as cursor:
                                        sql = "INSERT INTO " + MoveId + "(hrTSS, pTSS, HrateIF, PaceIF, HeartRate, Timedelta, Time, LapStartTime, Id, Cadence, Altitude, Pace, Activity, MaximumSpeed, DistanceMeters, LapDuration, Calories, Speed, LapNum, Latitude, Longitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                        cursor.execute(sql, (hrTSS, pTSS, HrateIF, PaceIF, HeartRate, Timedelta, Timepoint, LapStartTime, StringId, Cadence, Altitude, Pace, ActivityType[11:-2], MaximumSpeed.text, DistanceMeters.text, LapDuration, Calories.text, Speed.text, LapNum, LatitudeDegrees.text, LongitudeDegrees.text))
                                    connection.commit()
                                    StringId += 1
                getstring = "SELECT MAX(Timedelta), SUM(hrTSS), SUM(pTSS), AVG(Pace), AVG(Speed), AVG(HeartRate), SUM(Calories), AVG(Cadence), SUM(DISTINCT DistanceMeters) from " + MoveId
                Result = list(getdb(getstring))
                Duration = Result[0]
                TotalhrTSS = Result[1]
                TotalpTSS = Result[2]
                AverageSpeed = Result[4]
                AveragePace = time.strftime('%H:%M:%S', time.gmtime(1000 / float(AverageSpeed)))
                AverageHR = Result[5]
                CaloriesTotal = Result[6]
                AverageCadence = Result[7]
                Distance = Result[8]
#TODO 4. Calculate Start time
#TODO 5. Correct AveragePace
#TODO 10. Calculate time in HR and Pace zones

#Создаем запись в таблице Moves
                with connection.cursor() as cursor:
                    CreateStringInMoves = "INSERT INTO Moves (MoveId, Activity, Date, Duration, Distance, hrTss, pTSS, AveragePace, AverageSpeed, AverageHR, Calories, AverageCadence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(CreateStringInMoves, (MoveId, ActivityType[11:-2], ActivityStartTime[0:-9], Duration, Distance, TotalhrTSS, TotalpTSS, AveragePace, AverageSpeed, AverageHR, CaloriesTotal, AverageCadence))
                connection.commit()
                print('Upload finished successfully')
            else:
                print('Move ' + MoveId + ' already exist')

    connection.close()


def getdb(getstring):
    with connection.cursor() as cursor:
        cursor.execute(getstring)
        getResult = cursor.fetchone()
    return getResult






def insertdb(sql, value):

    connection = pymysql.connect(host='localhost', user='root', password='qazwsx', db='testdb', port=3306, charset='utf8mb4')
    with connection.cursor() as cursor:
        cursor.execute(sql, value)
    connection.commit()
    connection.close()

#Здесь нужно посчитать расчетные спредние величины и записать в таблицу Moves

if __name__ == "__main__":
    mainfunction()
