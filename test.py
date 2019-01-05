from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qazwsx@127.0.0.1:3306/testdb'
#app.config['SQLALCHEMY_ECHO'] = 'True'

db = SQLAlchemy(app)

class Moves(db.Model):
    __tablename__ = 'Moves'
    ID = db.Column(db.Integer, primary_key = True)
    UserID = db.Column(db.Integer, db.ForeignKey('UsedDetails.ID'))
    Activity = db.Column(db.String(128))
    Distance = db.Column(db.Float)
    Duration = db.Column(db.Time)
    hrTss = db.Column(db.Float)
    pTSS = db.Column(db.Float)
    def __init__(self, UserID, Activity, Distance, Duration, hrTss, pTSS):
        self.UserID = UserID
        self.Activity = Activity
        self.Distance = Distance
        self.Duration = Duration
        self.hrTSS = hrTss
        self.pTSS = pTSS
    def __repr__(self):
        return '<Moves %r>' % self.Distance


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
