from flask import render_template

from . import bp

@bp.route('/')
def home():
    return render_template('index.j2', title='Home')

@bp.route('/inventory')
def inventory():
    return render_template('about.j2')