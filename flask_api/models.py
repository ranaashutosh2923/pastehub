import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerialize

db = SQLAlchemy()
fs_mixin = FlaskSerialize(db)

class User(db.Model, fs_mixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(87), nullable=False)
    comments = db.relationship('Comment', backref='user')
    pastes = db.relationship('Paste', backref='user')

class Paste(db.Model, fs_mixin):
    __tablename__ = 'pastes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_hash = db.Column(db.String(8), unique=True, nullable=False)
    blob_url = db.Column(db.String(256), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    expire_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    comments = db.relationship('Comment', backref='paste')
    
class Comment(db.Model, fs_mixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    expire_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    paste_id = db.Column(db.Integer, db.ForeignKey('pastes.id'), nullable=False)
