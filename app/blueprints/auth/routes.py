from flask import render_template

from . import bp

@bp.route('/signup')
def register():
    return render_template('signup.jinja',title='Sign Up')

@bp.route('/signin')
def signin():
    return render_template('signin.jinja',title='Sign In')