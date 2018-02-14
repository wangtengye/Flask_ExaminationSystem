from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

student = Blueprint('student', __name__)


@student.before_request
@login_required
def check_permission():
    if current_user.permission != 'Student':
        return redirect('/not_permission')


@student.route('/')
def home():
    return render_template('student/student_page.html')
