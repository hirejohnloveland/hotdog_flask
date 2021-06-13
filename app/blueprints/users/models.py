from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from time import time
from flask import current_app as app
import base64
from datetime import datetime, timedelta
import os

## Enterprise ready User management is currently out of scope, 
## as the core of the project is to demo React E-commerce and React Native
## with a Flask endpoint.  Project can easily be upgraded to include user self serve
## password resets, JWS tokens, profile updates, etc. 

## In the current context, this is a single user application as the the only authenticated user
## is for management of the POS system, customers are tokenized for session managmeent but not registerd / autheniticated

# User is currently instantiated and logged to the database via the Flask shell when initializing the database.

@login.user_loader
# Default user_loader function is provided by and required for Flask_Login to work
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)   

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def __repr__(self):
        return f'<User | {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

class User_Anonymous(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(32), index=True, unique=True)
    origination = db.Column(db.DateTime, default = datetime.utcnow())

    def __init__(self):
        self.token = self.get_anon_token()
    
    def get_anon_token(self):
        # For simplicity, these tokens do not expires.  As long as a user
        # doesn't clear their local cache, their order persists.
        return base64.b64encode(os.urandom(24)).decode('utf-8')

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def check_token(token):
        user = User_Anonymous.query.filter_by(token=token).first()
        if user is None:
            return None
        return user
    

