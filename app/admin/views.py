from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)


@admin.before_request
@login_required
def check_permission():
    if current_user.permission != 'Admin':
        return redirect('/not_permission')


@admin.route('/')
def home():
    return render_template('admin/admin_page.html')
