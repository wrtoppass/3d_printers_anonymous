from flask import render_template, flash, redirect, flash, url_for

from app.models import User
from app import db

from . import bp
from app.forms import SignupForm

@bp.route('/signin')
def signin():
    return render_template('signin.jinja')

@bp.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data,email=form.email.data,password=form.password.data)
            u.commit()
            flash(f"{form.username.data} signed up")
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already taken, try again')
        else:
            flash(f'{form.email.data} already taken, try again')
    return render_template('signup.jinja', form=form)