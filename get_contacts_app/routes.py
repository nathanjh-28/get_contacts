from get_contacts_app import app
from flask import render_template

@app.route("/")
def home():
    return render_template('home.html')