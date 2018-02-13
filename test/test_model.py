import unittest

from flask import Flask

from app.models import Student
from app import app

class StudentModelTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_password(self):
        stu=Student.query.filter_by(account='zal').first()
        print(stu.name)