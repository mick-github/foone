from flask_wtf import FlaskForm
from .models import UNIT, GRADE
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    explain = StringField('Explain')
    answer = StringField('Answer', validators=[DataRequired()])
    grade = StringField('Grade')
    unit = StringField('Unit')
    tags = StringField('Tags')
    submit = SubmitField('Submit')

    '''
    def __init__(self):
        self.grade.choices = [(item, item) for item in GRADE]
        self.unit.choices = [(item, item) for item in UNIT]
    '''