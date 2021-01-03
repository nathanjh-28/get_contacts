from get_contacts_app import app, db, bcrypt
from get_contacts_app.models import User#, Post, Contact, Channel
from get_contacts_app.forms import RegistrationForm, LoginForm#, UpdateAccountForm, PostForm, ContactForm, ChannelForm
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/admin/contacts/new")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_u = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pw
        )
        db.session.add(new_u)
        db.session.commit()
        flash('Your account has been created.  Please Login','is-success')
        return redirect(url_for('login'))
    return render_template('auth_form.html',form=form, title='Register')

@app.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u and bcrypt.check_password_hash(u.password,form.password.data):
            login_user(u,remember=form.remember.data)
            next_page = request.args.get('next') 
            return redirect(nextpage) if next_page else redirect(url_for('home'))
        else:
            flash('login uncucessful.  Please check email and password', 'is-danger')
    return render_template('auth_form.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_required
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

