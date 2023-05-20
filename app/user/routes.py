from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.database import db
from app.user.forms import LoginForm, RegistrationForm
from app.user.models import User
from flask import Blueprint

bp = Blueprint('user', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.home'))
    return render_template('user/login.html', title='Sign In', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, cell_number=form.cell_number.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', title='Register', form=form)