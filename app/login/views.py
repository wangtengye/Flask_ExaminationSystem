from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, current_user
from .. import db

from ..models import Student, Teacher, Admin, table_dict

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
    return render_template('login.html', next=request.args.get('next'))


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

    user = None
    stu = Student.query.filter_by(account=account).first()
    if stu is not None and stu.verify_password(password):
        user = stu

    tea = Teacher.query.filter_by(account=account).first()
    if tea is not None and tea.verify_password(password):
        user = tea

    admin = Admin.query.filter_by(account=account).first()
    if admin is not None and admin.verify_password(password):
        user = admin

    if user is not None:
        login_user(user)
        next_ = request.args.get('next')
        if next_ is None or not next_.startswith('/'):
            next_ = user.permission.lower()
        return next_
    return 'wrongpassword'


@login.route('/reset_password/<usr>', methods=['post'])
def reset_password(usr):
    user = table_dict[usr].query.get(current_user.id)
    user.password = request.form['password']

    db.session.add(user)
    db.session.commit()
    return 'true'
