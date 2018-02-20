import unittest

import itertools
from pprint import pprint

from flask import Flask, json
from pyecharts import Line

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
        grade = db.session.query(Student.name, Record.score).filter(Record.pid == 1) \
            .filter(Student.id == Record.sid).all()
        print(grade)
        raw_data = db.session.query(Record.score).filter(Record.pid == 1).all()
        data = list(itertools.chain(*raw_data))
        print(data)
        line = Line('233')
        line.add(None, is_xaxis_show=False, x_axis=[''] * 6, is_xaxis_boundarygap=False, y_axis=data,
                 mark_point=['min', 'max'],
                 mark_line=['average'])
        print(json.dumps(line.options, indent=" "))
