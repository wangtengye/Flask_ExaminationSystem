from flask_login import UserMixin
from .. import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    id = db.Column(db.BIGINT, primary_key=True)
    account = db.Column(db.VARCHAR(20))
    name = db.Column(db.CHAR(20))
    password_hash = db.Column(db.CHAR(20))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.__tablename__, self.id


class Student(db.Model, User):
    __tablename__ = 'student'
    class_id = db.Column(db.BIGINT, db.ForeignKey('class.id'))
    permission = 'Student'


class Teacher(db.Model, User):
    __tablename__ = 'teacher'
    permission = 'Teacher'


class Admin(db.Model, User):
    __tablename__ = 'admin'
    permission = 'Admin'


class Class(db.Model):
    __table__name = 'class'
    id = db.Column(db.BIGINT, primary_key=True)
    tid = db.Column(db.BIGINT, db.ForeignKey('teacher.id'))
    name = db.Column(db.CHAR(20))

    @staticmethod
    def get_id_by_name(name):
        return Class.query.filter_by(name=name).first().id

    @staticmethod
    def get_name_by_id(id):
        return Class.query.get(id).name


table_dict = {'student': Student, 'teacher': Teacher, 'admin': Admin}


@login_manager.user_loader
def load_user(user_id):
    tablename, id = user_id
    return table_dict[tablename].query.get(id)
