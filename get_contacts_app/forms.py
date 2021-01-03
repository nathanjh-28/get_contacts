from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FormField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_login import current_user
from wtforms.fields.html5 import URLField, TelField

# from get_contacts_app.models import User

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

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is taken.  Please choose a different one')
    
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('That email is taken.  Please choose a different one')