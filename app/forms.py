from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from .models import User
from werkzeug.security import check_password_hash

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[
        InputRequired(), 
        Length(min=6, message='Password should be at least 6 characters long.')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired(), 
        EqualTo('password', message='Passwords must match.')
    ])
    signup_submit = SubmitField('Confirm Sign-Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered.')

class SignInForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('No account found with that email.')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not check_password_hash(user.password, password.data):
            raise ValidationError('Incorrect password.')

class ChatForm(FlaskForm):
    data = StringField('Chat Content', validators=[InputRequired(), Length(min=1, max=1000)])
    img = FileField('Upload Image')
    submit = SubmitField('Add Chat')
