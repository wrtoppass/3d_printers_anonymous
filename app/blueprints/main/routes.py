from flask import render_template

from . import bp 

@bp.route('/')
def home():
    printers={
        'admins': ('William'),
        'owned_printers': ['Creality CR-10', 'Creality Ender 3 Pro V2', 'Elegoo Saturn 8k', 'Prusa MK4', 'Anycubic Photon Mono X']
    }
    return render_template('index.jinja',title='Home', admins=printers['admins'], owned_printers=printers['owned_printers'])

@bp.route('/forum')
def about():
    return render_template('forum.jinja',title='Forum')