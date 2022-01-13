from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
import os
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comfy.db'

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
