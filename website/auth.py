from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login Successful! :)', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Wrong password! :(', category='error')
        else:
            flash('Username doesn\'t exist!', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()

        """
        account creation restrictions:
        - unique username 
        - username must be at least 3 characters
        - username cannot have spaces, and cannot start with digits, and must be alphanumeric
        - first name must be at least 2 characters
        - password must be at least 8 characters
        """

        if user:
            flash('Username is taken :(', category='error')
        elif len(username)<3:
            flash('Username should be at least 3 characters :(', category='error')
        
        elif " " in username:
            flash('Username cannot have spaces in them :(', category='error')
        
        elif username[0].isdigit():
            flash('Username cannot start with a number :(', category='error')
        
        elif not username.isalnum():
            flash('Username cannot have special characters :(', category='error')
            
        elif len(first_name) < 2:
            flash('Your first name is longer than this, right?', category='error')
        
        elif len(password1) < 8:
            flash('Password should be at least 8 characters :(', category='error')
            
        elif password1!=password2:
            flash('Passwords don\'t match :(', category='error')
            
        else:
            # add user to database
            new_user = User(username=username, first_name=first_name, password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created! :)', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
