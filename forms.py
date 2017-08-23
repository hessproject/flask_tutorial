from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Passwords must be at least 6 characters.")])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Sign In")