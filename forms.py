from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, Length

class Uploadform(FlaskForm):
    fileName = FileField(validators=[FileRequired()])

class UserEdit(Form):
    Name = TextField('Name', validators = [Required()])
    Age = TextField('Age',  validators = [Required()])
    Weight = TextField('Weight', validators = [Required()])
    HRThreshold = TextField('HRThreshold', validators = [Required()])
    PaceThreshold = TextField('PaceThreshold', validators = [Required()])
    Hrmin = TextField('Hrmin', validators = [Required()])
    Hrmax = TextField('Hrmax', validators = [Required()])
    HRLim1 = TextField('HRLim1', validators = [Required()])
    HRLim2 = TextField('HRLim2', validators = [Required()])
    HRLim3 = TextField('HRLim3', validators = [Required()])
    HRLim4 = TextField('HRLim4', validators = [Required()])
    HRLim5 = TextField('HRLim5', validators = [Required()])
    HRLim6 = TextField('HRLim6', validators = [Required()])
    PaceLim1 = TextField('PaceLim1', validators = [Required()])
    PaceLim2 = TextField('PaceLim2', validators = [Required()])
    PaceLim3 = TextField('PaceLim3', validators = [Required()])
    PaceLim4 = TextField('PaceLim4', validators = [Required()])
    PaceLim5 = TextField('PaceLim5', validators = [Required()])
    PaceLim6 = TextField('PaceLim6', validators = [Required()])
