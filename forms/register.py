from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Ник', validators=[DataRequired()])
    password = PasswordField('пароль', validators=[DataRequired()])
    password_again = PasswordField('повторите пароль', validators=[DataRequired()])
    submit = SubmitField('submit')
