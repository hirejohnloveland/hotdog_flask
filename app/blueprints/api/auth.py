from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.blueprints.users.models import User, User_Anonymous
from werkzeug.security import check_password_hash


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    u = User.query.filter_by(username=username).first()
    if u and check_password_hash(u.password, password):
        return u


@token_auth.verify_token
def verify_token(token):
    print("auth script")
    if token:
        if User.check_token(token):
            return User.check_token(token)
        if User_Anonymous.check_token(token):
            return User_Anonymous.check_token(token)
    print("auth script")
    return None
