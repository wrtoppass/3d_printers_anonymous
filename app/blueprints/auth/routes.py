from flask import render_template, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User

from . import bp 
from app.forms import RegisterForm, SigninForm

@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data,email=form.username.data,password=form.password.data)
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f'{form.username.data} has been registered', 'success')
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already taken, try again')
        else:
            flash(f'{form.email.data} already taken, try again')
    return render_template('register.j2', form=form)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form=SigninForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f'{form.username.data} signed in!', 'Welcome')
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash(f'{form.username.data} Username or Password is incorrect')
    return render_template('signin.j2', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('main.home'))