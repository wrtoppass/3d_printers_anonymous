from flask import Blueprint

bp = Blueprint('printers', __name__, url_prefix='/printers')

from . import routes