from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from chessassist.users.forms import UserForm, LoginForm
from chessassist import db
from werkzeug.security import generate_password_hash, check_password_hash
from chessassist.models import Users
from flask_login import login_user, login_required, logout_user, current_user
from chessassist.users.utils.make_lists import make_lists

#blueprint instance
users = Blueprint('users', __name__)

#blueprint(user) routes
@users.route('/create-account', methods=['GET', 'POST'])
def create_account():
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            password_hash = generate_password_hash(form.password.data, 'sha256')
            user = Users(email=form.email.data, username=form.username.data, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()
        form.email.data = ''
        form.username.data = ''
        form.password.data = ''
        form.password_2.data = ''
        flash('Account Creation Successful')
        return redirect(url_for('users.login'))
    return render_template('create_account.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash('Login Succesful')
                return redirect(url_for('users.profile'))
            else:
                flash("Wrong Password, Try Again")
        else:
            flash('No user associated with that email. Try again.')
    return render_template('login.html', form=form)

@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have logged out.')
    return redirect(url_for('users.login'))


@users.route('/profile')
@login_required
def profile():
    missed_checkmates, opening_dict, missed_check_caps, games_your_blunders, games_their_blunders = make_lists(current_user.username)
    
    return render_template('user_profile.html', games_your_blunders=games_your_blunders, games_their_blunders=games_their_blunders, opening_dict = opening_dict, missed_checkmates=missed_checkmates, missed_check_caps=missed_check_caps)

@users.route('/test')
def test():
    return render_template('profile_test.html')