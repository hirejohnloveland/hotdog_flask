from . import bp as api
from flask import jsonify
from app.blueprints.users.models import User_Anonymous

@api.route('/tokens/anon', methods=['POST'])
def get_anon_token():
    user = User_Anonymous()
    user.save_user()
    return jsonify({ 'token': user.token})
