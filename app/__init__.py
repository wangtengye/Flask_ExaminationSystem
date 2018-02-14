from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@:3306/airing?charset=utf8'
app.config['SECRET_KEY'] = 'a,buxiangxiele'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login.index'

from .login import login
from .student import student
from .teacher import teacher
from .admin import admin

app.register_blueprint(login)
app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(teacher, url_prefix='/teacher')
app.register_blueprint(admin, url_prefix='/admin')
