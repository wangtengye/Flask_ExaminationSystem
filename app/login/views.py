from flask import Blueprint, render_template, request, redirect, session
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
    session.clear()
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
        session['userid'] = stu.id
        session['name'] = stu.name
        session['permission'] = stu.permission
        return '/student'

    tea = Teacher.query.filter_by(account=account).first()
    if tea is not None and tea.verify_password(password):
        session['userid'] = tea.id
        session['name'] = tea.name
        session['permission'] = tea.permission
        return '/teacher'

    admin = Admin.query.filter_by(account=account).first()
    if admin is not None and admin.verify_password(password):
        session['userid'] = admin.id
        session['name'] = admin.name
        session['permission'] = admin.permission
        return '/admin'

    return 'wrongpassword'
