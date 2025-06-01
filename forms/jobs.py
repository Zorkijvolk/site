from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField


class JobsForm(FlaskForm):
    job = StringField('Job Title')
    team_leader = StringField('Team Leader Id')
    work_size = StringField('Work Size')
    collaborators = StringField('Collaborators')
    is_finished = BooleanField('Is Job Finished')
    submit = SubmitField('Submit')
