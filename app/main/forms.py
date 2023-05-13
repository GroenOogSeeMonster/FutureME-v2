from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    response = RadioField('Response', choices=[('1', 'Very much unlike me'), ('2', 'Unlike me'),
                                              ('3', 'Neutral'), ('4', 'Like me'), ('5', 'Very much like me')],
                          validators=[DataRequired()])
    submit = SubmitField('Next')

from wtforms import TextAreaField

class WritingForm(FlaskForm):
    response = TextAreaField('Response', validators=[DataRequired(), Length(max=2000)])
    submit = SubmitField('Next')

from wtforms import TextAreaField, StringField

class GoalForm(FlaskForm):
    goal = StringField('Goal', validators=[DataRequired(), Length(max=250)])
    notes = TextAreaField('Notes')
    submit = SubmitField('Next')

from wtforms import TextAreaField

class JournalEntryForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Next')

from wtforms import SelectField, TimeField, StringField

class RoutineForm(FlaskForm):
    day_of_week = SelectField('Day of week', choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    activity = StringField('Activity', validators=[DataRequired()])
    submit = SubmitField('Save')

class UncompletedTaskForm(FlaskForm):
    task = StringField('Uncompleted Task', validators=[DataRequired()])
    submit = SubmitField('Save')

class GoalForm(FlaskForm):
    goal = StringField('Goal', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Save')

class ScheduleForm(FlaskForm):
    day = SelectField('Day', choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
                                      ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
                                      ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                                      ('Sunday', 'Sunday')], validators=[DataRequired()])
    hour = SelectField('Hour', choices=[(str(i), str(i)) for i in range(24)], coerce=str, validators=[DataRequired()])
    activity = StringField('Activity', validators=[DataRequired()])
    submit = SubmitField('Save')