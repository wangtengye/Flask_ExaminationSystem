import unittest

from flask import Flask

from app.models import Student, Record
from app import app, db


class StudentModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_password(self):
        stu = Student.query.filter_by(account='zal').first()
        print(stu.name)

    def test_grade_list(self):
        grade= db.session.query(Student.name, Record.score).filter(Record.pid == 1) \
            .filter(Student.id == Record.sid).all()
        print(grade)
