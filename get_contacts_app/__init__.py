from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '2APngFaCxp6CZ1jG'

#Dev 2 of 2
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Prod
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lbfwidkcmtpqht:f1ee0c93db2ed278ea614b7f2e2182b0c7d8da3a6f2282faace6ae49674ac5bc@ec2-50-19-247-157.compute-1.amazonaws.com:5432/d17vful3o0p4nc'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from get_contacts_app import routes