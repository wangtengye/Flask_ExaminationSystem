from flask import Blueprint, render_template, session, redirect

admin = Blueprint('admin', __name__)


@admin.before_request
def check_permission():
    permission = session.get('permission')
    if permission is None:
        return redirect('/')
    elif permission != 'Admin':
        return redirect('/not_permission')


@admin.route('/')
def home():
    return render_template('admin/admin_page.html')
