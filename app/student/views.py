from flask import Blueprint, render_template, session, redirect

student = Blueprint('student', __name__)


@student.before_request
def check_permission():
    permission = session.get('permission')
    if permission is None:
        return redirect('/')
    elif permission != 'Student':
        return redirect('/not_permission')


@student.route('/')
def home():
    return render_template('student/student_page.html')
