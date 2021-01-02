from flask import Flask

app = Flask(__name__)

from get_contacts_app import routes
