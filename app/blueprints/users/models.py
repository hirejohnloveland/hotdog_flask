from app import db
import base64
from datetime import datetime
import os


class User_Anonymous(db.Model):
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
    

