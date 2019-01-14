from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

from flask_bcrypt import Bcrypt

from app import db

from app.users.forms import LoginForm

from app.users.models import User

mod_auth = Blueprint('auth',__name__,url_prefix='/auth')

@mod_auth.route('/signin', methods=['GET','POST'])
def signin():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and Bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['name'] = user.name
            session['email'] = user.email
            flash('Welcome {}'.format(user.name),'success')
            return redirect(url_for('auth.home'))
        flash('Wrong email or password','danger')
    return render_template('auth/signin.html', form = form)