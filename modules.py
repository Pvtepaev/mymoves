from app import db
from sqlalchemy import Column, Integer, Float, String, Time
from datetime import datetime



ROLE_USER = 0
ROLE_ADMIN = 1

class Plan(db.Model):
    __tablename__ = 'Plan'
    id = db.Column(db.Integer, primary_key = True)
    Date = db.Column(db.Date)
    Week = db.Column(db.Integer)
    TSSplan = db.Column(db.Integer)
    TSScompl = db.Column(db.Integer)
    TrainingPhase = db.Column(db.String(128))
    def __init__(self, *args, **kwargs):
        super(Plan, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<id: {}, Date: {}, Week: {}, TSSplan: {}, TSScompl: {}, TrainingPhase: {}>'.format(self.id, self.Date, self.Week, self.TSSplan, self.TSScompl, self.TrainingPhase)


class UserDetails(db.Model):
    __tablename__ = 'UserDetails'
    ID = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(128), index = True, unique = True)
    Age = db.Column(db.Integer)
    Weight = db.Column(db.Float)
    Hrmin = db.Column(db.Integer)
    Hrmax = db.Column(db.Integer)
    HRThreshold = db.Column(db.Integer)
    PaceThreshold = db.Column(db.Time)
    HRLim1 = db.Column(db.Integer)
    HRLim2 = db.Column(db.Integer)
    HRLim3 = db.Column(db.Integer)
    HRLim4 = db.Column(db.Integer)
    HRLim5 = db.Column(db.Integer)
    HRLim6 = db.Column(db.Integer)
    PaceLim1 = db.Column(db.Time)
    PaceLim2 = db.Column(db.Time)
    PaceLim3 = db.Column(db.Time)
    PaceLim4 = db.Column(db.Time)
    PaceLim5 = db.Column(db.Time)
    PaceLim6 = db.Column(db.Time)
    def __init__(self, *args, **kwargs):
        super(UserDetails, self).__init__(*args, **kwargs)


class Moves(db.Model):
    __bind_key__ = 'mymoves'
    __tablename__ = 'Moves'
    ID = db.Column(db.Integer, primary_key = True)
    UserID = db.Column(db.Integer)
    MoveID = db.Column(db.String)
    Activity = db.Column(db.String(128))
    Date = db.Column(db.DateTime)
    Time = db.Column(db.Time)
    Distance = db.Column(db.Float)
    Duration = db.Column(db.Time)
    hrTss = db.Column(db.Float)
    pTSS = db.Column(db.Float)
    AverageSpeed = db.Column(db.Float)
    AverageHR = db.Column(db.Float)

    def __init__(self, ID=None, UserID=None, MoveID=None, Activity=None, Date=None, Time=None, Distance=None, Duration=None, hrTss=None, pTSS=None, AverageSpeed=None, AverageHR=None):
        self.ID = ID
        self.UserID = UserID
        self.Activity = Activity
        self.Distance = Distance
        self.Duration = Duration
        self.hrTss = hrTss
        self.pTSS = pTSS
        self.MoveID = MoveID
        self.Date = Date
        self.Time = Time
        self.AverageSpeed = AverageSpeed
        self.AverageHR = AverageHR
    def __repr__(self):
        return "<Moves(MoveID='%r')>" % (self.MoveID)
