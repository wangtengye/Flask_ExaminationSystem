from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

teacher = Blueprint('teacher', __name__)


@teacher.before_request
@login_required
def check_permission():
    if current_user.permission != 'Teacher':
        return redirect('/not_permission')


@teacher.route('/')
def home():
    return render_template('teacher/teacher_page.html')
