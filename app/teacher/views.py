from flask import Blueprint, render_template, session, redirect

teacher = Blueprint('teacher', __name__)


@teacher.before_request
def check_permission():
    permission = session.get('permission')
    if permission is None:
        return redirect('/')
    elif permission != 'Teacher':
        return redirect('/not_permission')


@teacher.route('/')
def home():
    return render_template('teacher/teacher_page.html')
