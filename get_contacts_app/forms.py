from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FormField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_login import current_user
from wtforms.fields.html5 import URLField, TelField

from get_contacts_app.models import User

# ===========================================================

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[ 
        DataRequired(), 
        Length(min=2,max=20 )], render_kw={'placeholder':'Username'})
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email()], render_kw={'placeholder':'Email'})
    
    password = PasswordField('Password', validators=
        [DataRequired()], render_kw={'placeholder':'Password'})
    
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo( 'password' )], render_kw={'placeholder':'Confirm'})
    
    submit = SubmitField( 'Sign Up' )

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.  Please choose a different one')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.  Please choose a different one')

#____________________________________________________________

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email()], render_kw={'placeholder':'Email'})

    password = PasswordField('Password', validators=
        [DataRequired()], render_kw={'placeholder':'Password'})

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

#____________________________________________________________

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators=[
            DataRequired(), 
            Length(min=2, max=20)])

    email = StringField('Email', 
        validators=[
            DataRequired(), 
            Email()],)

    picture = URLField('Update Profile Picture')

    bio = TextAreaField('About Me', render_kw={'placeholder':'Hello, I am'})

    submit = SubmitField('Update Account')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken.  Please choose a different one')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken.  Please choose a different one')