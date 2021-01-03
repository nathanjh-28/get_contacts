from get_contacts_app import app
from flask import render_template

@app.route("/")
@app.route("/admin/contacts/new")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return 'This is the logout route'

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/admin")
@app.route("/admin/contacts")
def admin_home():
    return render_template('admin-home.html')

@app.route("/admin/contacts/one")
def one_contact():
    return render_template('one-contact.html')

