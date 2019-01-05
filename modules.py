from app import db
from sqlalchemy import Column, Integer, Float, String, Time
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

class UserDetails(db.Model):
    __tablename__ = 'UserDetails'
    __bind_key__ = 'mymoves'
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
    def __init__(self, ID, Name, Age, Weight, Hrmin, Hrmax, HRThreshold, PaceThreshold, HRLim1, HRLim2, HRLim3, HRLim4, HRLim5, HRLim6, PaceLim1, PaceLim2, PaceLim3, PaceLim4, PaceLim5, PaceLim6):
        self.ID = ID
        self.Age = Age
        self.Weight = Weight
        self.Hrmin = Hrmin
        self.Hrmax = Hrmax
        self.HRThreshold = HRThreshold
        self.PaceThreshold = PaceThreshold
        self.HRLim1 = HRLim1
        self.HRLim2 = HRLim2
        self.HRLim3 = HRLim3
        self.HRLim4 = HRLim4
        self.HRLim5 = HRLim5
        self.HRLim6 = HRLim6
        self.PaceLim1 = PaceLim1
        self.PaceLim2 = PaceLim2
        self.PaceLim3 = PaceLim3
        self.PaceLim4 = PaceLim4
        self.PaceLim5 = PaceLim5
        self.PaceLim6 = PaceLim6
    def __repr__(self):
        return "<UserDetails %r>" % (self.Name)


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
