# -*- coding: utf-8 -*-

from flask import flash, redirect, render_template, request, url_for, Blueprint, session
import project.model.users as Users
users_blueprint = Blueprint(
        'users', __name__,
        template_folder='templates'
)
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        per, lvl = Users.login(request.form['username'], request.form['password'])
        if not per:
            error = 'username password not match!'
        else:
            session['permission'] = lvl
            flash('welcome,' + per)
            return redirect(url_for('users.home'))
    return render_template('login.html', error=error)

@users_blueprint.route('/logout')
def logout():
    session.pop('permission',None)
    flash('Bye')
    return redirect(url_for('users.home'))

@users_blueprint.route('/')
def home():
    return render_template('home.html')

