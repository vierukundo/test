from flask import render_template, flash, redirect, url_for
from app.email import send_password_reset_email
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from flask import request
from werkzeug.urls import url_parse
from app import app
from app.models.user import User
import os

@app.route('/')
@app.route('/index')
@login_required
def index():
    images_folder = '/home/rukundo/test/app/static/images'
    images = os.listdir(images_folder)
    images_path = [f'images/{image}' for image in images if image.startswith('profile')]
    return render_template('homepage.html', title='Home Page', images=images_path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        from app.models import storage
        user = storage.check_user(User, form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        from app.models import storage
        user = storage.load_user_by_email(User, email=form.email.data)
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        user.save()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/materials')
def materials():
    images_folder = '/home/rukundo/test/app/static/images'
    images = os.listdir(images_folder)
    images_path = [f'images/{image}' for image in images]
    return render_template('materials.html', images=images_path)

@app.route('/machineries')
def machineries():
    images_folder = '/home/rukundo/test/app/static/images'
    images = os.listdir(images_folder)
    images_path = [f'images/{image}' for image in images]
    return render_template('machinery.html', images=images_path)

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/money')
def money():
    return render_template('money.html')

@app.route('/manpowers')
def manpowers():
    images_folder = '/home/rukundo/test/app/static/images'
    images = os.listdir(images_folder)
    images_path = [f'images/{image}' for image in images]
    return render_template('manpower.html', images=images_path)

@app.route('/search_results')
def search_results():
    query = request.args.get('query')
    page_name = request.args.get('page')

    return {page_name: query}
