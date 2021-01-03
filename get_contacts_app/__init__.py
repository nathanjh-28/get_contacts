from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '<hklasdjhfwehuhflaiudsghakjsdh>'

from get_contacts_app import routes
