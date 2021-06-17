from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

from . import routes_tokens, routes_menu, routes_orders