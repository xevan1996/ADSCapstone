from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, FloatField, SubmitField
from wtforms.validators import DataRequired

class dataForm(FlaskForm):

    gender = FloatField('age', validators=[DataRequired()])
    age = FloatField('sex', validators=[DataRequired()])
    chpain = FloatField('chest pain type', validators=[DataRequired()])
    restbp = FloatField('resting blood pressure', validators=[DataRequired()])
    restecg = FloatField('resting ecg"', validators=[DataRequired()])
    maxhr = FloatField('maximum heart rate', validators=[DataRequired()])
    exian = FloatField('exercise-induced angina', validators=[DataRequired()])
    stdep = FloatField('st depression', validators=[DataRequired()])
    slp = FloatField('slope', validators=[DataRequired()])
    diab = FloatField('diabetic', validators=[DataRequired()])
    chole = FloatField('cholesterol', validators=[DataRequired()])
