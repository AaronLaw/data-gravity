from datetime import datetime

from flask import url_for
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .exceptions import ValidationError
from . import db

class Permission:
    READ_ONLY = 0x01
    MEETING_CREATOR = 0x02
    ACCOUNT_MANAGER = 0x04
    ACCOUNT_OWNER = 0x08
    METAREACT_ADMIN = 0x512


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='roles', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    """
        Represents a single user in the system.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        json_user = {
            'url': url_for('get_user', user_id=self.id, _external=True),
            'email': self.email,
        }
        return json_user
    
    def __repr__(self):
        return '<User %r>' % self.email


class Follower(db.Model):
    """
        Represents a count of followers for one service.
    """
    __tablename__ = 'follower'
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.Integer, db.ForeignKey('service.id'))
    count = db.Column(db.Integer)
    timestamped = db.Column(db.DateTime)

    def __init__(self, service, count=0, timestamp=datetime.utcnow()):
        self.service = service.id
        self.count = count
        self.timestamped = timestamp


class Service(db.Model):
    """
        Represents a service that is being tracked by the user,
        for example Twitter or GitHub.
    """
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    site_url = db.Column(db.String(1024))
    followers = db.relationship('Follower', backref='followers',
                                lazy='dynamic')

    def __init__(self, name, site_url):
        self.name = name
        self.site_url = site_url

