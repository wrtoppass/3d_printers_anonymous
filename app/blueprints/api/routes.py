from flask import request, jsonify

from . import bp
from app.models import Printer, User

@bp.get('/post')
def api_printers():
    result = []
    printers = Printer.query.all()
    for printer in printers:
        result.append(
            {
            'id': printer.id,
            'company': printer.brand,
            'name': printer.model,
            'description': printer.description,
            'author': printer.user_id
            }
        )
    return jsonify(result), 200

@bp.get('/post/<username>')
def user_printers(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
            'id': printer.id,
            'company': printer.brand,
            'name': printer.model,
            'description': printer.description
        }for printer in user.printers]), 200
    return jsonify([{'message':'Invalid Username'}]), 404

@bp.get('/post/<id>')
def get_printer(id):
    try:
        printer = Printer.query.get(id)
        return jsonify([{
            'id': printer.id,
            'company': printer.brand,
            'name': printer.models,
            'description': printer.description,
            'author': printer.user_id

        }])
    except:
        return jsonify([{'message':'Invalid Post Id'}]), 404             