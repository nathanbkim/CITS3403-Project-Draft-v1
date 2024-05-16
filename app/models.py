from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the user
    email = db.Column(db.String(150), unique=True, nullable=False)  # Unique email address
    password = db.Column(db.String(150), nullable=False)  # User's password
    username = db.Column(db.String(150), nullable=False)  # User's username

    def get_id(self):
        return str(self.id)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the chat
    data = db.Column(db.String(1000))  # Text content of the chat
    img_path = db.Column(db.String(100), nullable=True)  # Optional image path
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of chat creation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User
    user = db.relationship('User', backref=db.backref('chats', lazy=True))  # Relationship to User

    def __repr__(self):
        return f'<Chat {self.id}>'


""" 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150))

    @property
    def is_active(self):
        return self.active

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
 """