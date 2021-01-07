from datetime import datetime
from get_contacts_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

default_image = 'https://images.unsplash.com/photo-1528797471109-9a6649153bc3?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=841&q=80'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    image = db.Column(db.String(200), nullable=False,default=default_image)
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.String(280))
    posts = db.relationship('Post',backref='post_author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image}' )"
    
#____________________________________________________________
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, 
        default=datetime.utcnow)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.Integer)
    subject = db.Column(db.String(75), nullable=False)
    body = db.Column(db.String(280), nullable=False)
    join = db.Column(db.Boolean)
    contacted = db.Column(db.Boolean)
    #relationship
    posts = db.relationship('Post',backref='contact_thread',lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text)
    date_posted = db.Column(
        db.DateTime, 
        nullable=False, 
        default=datetime.utcnow)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id'), 
        nullable=False)
    contact_id = db.Column(
        db.Integer,
        db.ForeignKey('contact.id'),
        nullable=False)