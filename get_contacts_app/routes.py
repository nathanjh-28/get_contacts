from get_contacts_app import app#, db, bcrypt
# from get_contacts_app.models import User, Post, Contact, Channel
from get_contacts_app.forms import RegistrationForm#, LoginForm, UpdateAccountForm, PostForm, ContactForm, ChannelForm
from flask import render_template, url_for, flash, redirect, request
# from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/admin/contacts/new")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('hello')
    return render_template('register.html',form=form, title='Register')

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

