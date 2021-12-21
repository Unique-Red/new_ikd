from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
import os
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://modbbwxczgreni:2d84f5ad03a054888be482357c79cc7d47ef3887326d72f2eafb0fc2fa55d386@ec2-54-89-105-122.compute-1.amazonaws.com:5432/dbu5dstpmb5r3s'

db = SQLAlchemy(app)
ckeditor = CKEditor(app)

from .models import User


login_manager = LoginManager()
login_manager.login_view = 'auth'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

from website import routes