from website import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    stext = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    file = db.Column(db.String(150), nullable=False)
    file1 = db.Column(db.String(150), nullable=False)
    file2 = db.Column(db.String(150), nullable=False)
    file3 = db.Column(db.String(150), nullable=False)
    file4 = db.Column(db.String(150), nullable=False)
    file5 = db.Column(db.String(150), nullable=False)
    file6 = db.Column(db.String(150), nullable=False)
    file7 = db.Column(db.String(150), nullable=False)
    file8 = db.Column(db.String(150), nullable=False)
    file9 = db.Column(db.String(150), nullable=False)
    file10 = db.Column(db.String(150), nullable=False)
    file11 = db.Column(db.String(150), nullable=False)
    file12 = db.Column(db.String(150), nullable=False)
    file13 = db.Column(db.String(150), nullable=False)
    file14 = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

db.create_all()