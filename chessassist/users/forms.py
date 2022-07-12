from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

# Create a form classes

class UserForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('LiChess Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_2', message='Passwords must match.'), Length(min=8, message='Password must be at least 8 characters')])
    password_2 = PasswordField('Re-enter Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')