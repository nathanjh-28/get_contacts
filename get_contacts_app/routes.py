from get_contacts_app import app, db, bcrypt
from get_contacts_app.models import User, Contact#, Post, Channel
from get_contacts_app.forms import RegistrationForm, LoginForm, UpdateAccountForm, ContactForm#, ChannelForm, PostForm, 
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/admin/contacts/new", methods=['GET','POST'])
@login_required
def add_contact():
    title = 'Add Contact'
    form = ContactForm()
    if form.validate_on_submit():
        new_c = Contact(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            subject=form.subject.data,
            body=form.body.data,
            join=form.join.data)
        db.session.add(new_c)
        db.session.commit()
        flash('Contact and Message Submitted!','is-success')
        return redirect(url_for('one_contact', contact_id=new_c.id))
    return render_template('form.html',form=form, title=title)

@app.route("/")
@app.route("/about")
def home():
    title='About This App'
    return render_template('about.html',title=title)

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
    return render_template('form.html',form=form, title='Register')

@app.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u and bcrypt.check_password_hash(u.password,form.password.data):
            login_user(u,remember=form.remember.data)
            next_page = request.args.get('next') 
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('login uncucessful.  Please check email and password', 'is-danger')
    return render_template('form.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    title = 'Your Account'
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.image = form.picture.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('changes made!', 'is-success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.picture.data = current_user.image
        form.bio.data = current_user.bio
    return render_template('account.html', title=title, form=form)

@app.route("/admin")
@app.route("/admin/contacts")
def admin_home():
    contacts = Contact.query.all()
    return render_template('admin-home.html', contacts=contacts)

@app.route("/admin/contacts/<int:contact_id>")
def one_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    return render_template('one-contact.html',contact=contact)

@app.route("/admin/contacts/<int:contact_id>/edit", methods=['GET','POST'])
def edit_contact(contact_id):
    title = 'Update Contact'
    form = ContactForm()
    this_contact = Contact.query.get(contact_id)
    if form.validate_on_submit():
        this_contact.name = form.name.data
        this_contact.email = form.email.data
        this_contact.phone = form.phone.data
        this_contact.subject = form.subject.data
        this_contact.body = form.body.data
        this_contact.join = form.join.data
        db.session.commit()
        flash('Contact Updated','is-success')
        return redirect(url_for('one_contact', contact_id=this_contact.id))
    elif request.method == 'GET':
        form.name.data = this_contact.name
        form.email.data = this_contact.email
        form.phone.data = this_contact.phone
        form.subject.data = this_contact.subject
        form.body.data = this_contact.body
        form.join.data = this_contact.join
    return render_template('form.html',form=form,title=title)

@app.route("/admin/contacts/<int:contact_id>/delete", methods=['POST'])
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact has been deleted','is-success')
    return redirect(url_for('admin_home'))
