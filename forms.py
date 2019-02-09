#from flask_wtf import FlaskForm
#from flask_wtf.file import FileField, FileRequired
#from flask.ext.wtf import Form
from wtforms import Form, StringField, TextField, DateField
from wtforms.validators import Required, Length


#Update values in trainig plan
class UpdatePlan(Form):
    weeknumber = StringField('Week to update: ', validators = [Required()])
    tsscompleted = StringField('Completed TSS:', validators = [Required()])



#Create plan
class CreatePlan(Form):
    startdate = DateField('Start Date')

    tssplanweek0 = StringField('Planned TSS for Week 1')
    tssplanweek1 = StringField('Planned TSS for Week 2')
    tssplanweek2 = StringField('Planned TSS for Week 3')
    tssplanweek3 = StringField('Planned TSS for Week 4')
    tssplanweek4 = StringField('Planned TSS for Week 5')
    tssplanweek5 = StringField('Planned TSS for Week 6')
    tssplanweek6 = StringField('Planned TSS for Week 7')
    tssplanweek7 = StringField('Planned TSS for Week 8')
    tssplanweek8 = StringField('Planned TSS for Week 9')
    tssplanweek9 = StringField('Planned TSS for Week 10')
    tssplanweek10 = StringField('Planned TSS for Week 11')
    tssplanweek11 = StringField('Planned TSS for Week 12')
    tssplanweek12 = StringField('Planned TSS for Week 13')
    tssplanweek13 = StringField('Planned TSS for Week 14')
    tssplanweek14 = StringField('Planned TSS for Week 15')
    tssplanweek15 = StringField('Planned TSS for Week 16')
    tssplanweek16 = StringField('Planned TSS for Week 17')
    tssplanweek17 = StringField('Planned TSS for Week 18')
    tssplanweek18 = StringField('Planned TSS for Week 19')
    tssplanweek19 = StringField('Planned TSS for Week 20')
    tssplanweek20 = StringField('Planned TSS for Week 21')
    tssplanweek21 = StringField('Planned TSS for Week 22')
    tssplanweek22 = StringField('Planned TSS for Week 23')
    tssplanweek23 = StringField('Planned TSS for Week 24')
    tssplanweek24 = StringField('Planned TSS for Week 25')
    tssplanweek25 = StringField('Planned TSS for Week 26')
    tssplanweek26 = StringField('Planned TSS for Week 27')
    tssplanweek27 = StringField('Planned TSS for Week 28')
    tssplanweek28 = StringField('Planned TSS for Week 29')
    tssplanweek29 = StringField('Planned TSS for Week 30')
    tssplanweek30 = StringField('Planned TSS for Week 31')
    tssplanweek31 = StringField('Planned TSS for Week 32')
    tssplanweek32 = StringField('Planned TSS for Week 33')
    tssplanweek33 = StringField('Planned TSS for Week 34')
    tssplanweek34 = StringField('Planned TSS for Week 35')
    tssplanweek35 = StringField('Planned TSS for Week 36')
    tssplanweek36 = StringField('Planned TSS for Week 37')
    tssplanweek37 = StringField('Planned TSS for Week 38')
    tssplanweek38 = StringField('Planned TSS for Week 39')
    tssplanweek39 = StringField('Planned TSS for Week 40')
    tssplanweek40 = StringField('Planned TSS for Week 41')
    tssplanweek41 = StringField('Planned TSS for Week 42')
    tssplanweek42 = StringField('Planned TSS for Week 43')
    tssplanweek43 = StringField('Planned TSS for Week 44')
    tssplanweek44 = StringField('Planned TSS for Week 45')
    tssplanweek45 = StringField('Planned TSS for Week 46')
    tssplanweek46 = StringField('Planned TSS for Week 47')
    tssplanweek47 = StringField('Planned TSS for Week 48')
    tssplanweek48 = StringField('Planned TSS for Week 49')
    tssplanweek49 = StringField('Planned TSS for Week 50')
    tssplanweek50 = StringField('Planned TSS for Week 51')
    tssplanweek51 = StringField('Planned TSS for Week 52')
    
#class Uploadform(Form):
#    filename = FileField(validators=[FileRequired()])

class UserEdit(Form):
    name = TextField('Name', validators = [Required()])
    age = TextField('Age',  validators = [Required()])
    weight = TextField('Weight', validators = [Required()])
    hrthreshold = TextField('HRThreshold', validators = [Required()])
    pacethreshold = TextField('PaceThreshold', validators = [Required()])
    hrmin = TextField('Hrmin', validators = [Required()])
    hrmax = TextField('Hrmax', validators = [Required()])
    hrlim1 = TextField('HRLim1', validators = [Required()])
    hrlim2 = TextField('HRLim2', validators = [Required()])
    hrlim3 = TextField('HRLim3', validators = [Required()])
    hrlim4 = TextField('HRLim4', validators = [Required()])
    hrlim5 = TextField('HRLim5', validators = [Required()])
    hrlim6 = TextField('HRLim6', validators = [Required()])
    pacelim1 = TextField('PaceLim1', validators = [Required()])
    pacelim2 = TextField('PaceLim2', validators = [Required()])
    pacelim3 = TextField('PaceLim3', validators = [Required()])
    pacelim4 = TextField('PaceLim4', validators = [Required()])
    pacelim5 = TextField('PaceLim5', validators = [Required()])
    pacelim6 = TextField('PaceLim6', validators = [Required()])
