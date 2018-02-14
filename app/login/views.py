from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user

from ..models import Student, Teacher, Admin

login = Blueprint('login', __name__)
static_file_suffix = ['.css', '.png']


@login.before_app_request
def static_file():
    if request.endpoint != 'static':
        path = request.path
        if path[path.rfind('.'):] in static_file_suffix:
            return redirect('static' + request.path)


@login.route('/')
def index():
    return render_template('login.html')


@login.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html')


@login.route('/not_permission')
def not_permission():
    return render_template('not_permission.html')


@login.route('/doLogin', methods=['post'])
def do_login():
    account = request.form['account']
    password = request.form['password']

    stu = Student.query.filter_by(account=account).first()
    if stu is not None and stu.verify_password(password):
        login_user(stu)
        return '/student'

    tea = Teacher.query.filter_by(account=account).first()
    if tea is not None and tea.verify_password(password):
        login_user(tea)
        return '/teacher'

    admin = Admin.query.filter_by(account=account).first()
    if admin is not None and admin.verify_password(password):
        login_user(admin)
        return '/admin'

    return 'wrongpassword'
