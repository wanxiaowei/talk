# -*- coding: utf-8 -*-

from flask import flash redirect, render_template, request, url_for, Blueprint, session

admin_blueprint = Blueprint(
        'admin', __name__,
        template_folder='template'
)
@admin_blueprint.route('/')
def home():
    return render_template('home.html')

@admin_register.route('/register', method=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        re_password = request.form['re_password']
        if password != re_password:
            error = 'two passwords do not match'
        elif Admin.check_username(username):
            error = 'username is existed'
        else:
            Admin.register(username, password)
            flash('success')
            return redirect(url_for('admin.home'))
    return render_template('register.html', error=error)

@admin_register.route('/manage', method=['GET', 'POST'])
def manage():
    error = None
    info = Admin.get_perminfo()
    if request.method == 'POST':
        print(request.form)
        flash('success')
        redirect(url_for('admin.home'))
    return render_template('manage.html', error=error, perinfo=info)

