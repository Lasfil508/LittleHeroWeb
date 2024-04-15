from flask import Flask, render_template, request, redirect, url_for, send_file, g, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from DataBaseManager import DBManager
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename='data/log.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

DATABASE = '/data/LittleHeroDB.db'
gamePath = 'LittleHeroFiles/little_hero.zip'


app = Flask(__name__)
app.config['SECRET_KEY'] = '23dadd556c0f820e6a81887f0c3f41bd90357ab9'
app.config.from_object(__name__)
app.config.update(dict(DATABASE=path.join(app.root_path, 'data\\LittleHeroDB.db')))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Авторизуйтесь для доступа к данной странице'
login_manager.login_message_category = 'success'


@login_manager.user_loader
def load_user(user_id):
    logging.debug(f'User load: {user_id}')
    return UserLogin().fromDB(user_id, dbase)


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(e):
    if hasattr(g, 'link_db'):
        g.link_db.close()


dbase = None
@app.before_request
def before_requests():
    global dbase
    db = get_db()
    dbase = DBManager(db)


@app.route('/')
def main_page():
    return render_template('main.html', user=current_user)


@app.route('/download', methods=['POST'])
def download():
    return send_file(gamePath, as_attachment=True)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        form = request.form.to_dict()
        if form:
            nickname = form['nickname']
            password = generate_password_hash(form['password'])
            email = form['email']
            result = dbase.addUser(nickname, password, email)

            if not result:
                return render_template('registration.html', errors=True)
            else:
                return redirect(url_for('main_page'))

    return render_template('registration.html', user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form:
            email = request.form['email']
            password = request.form['password']
            user = dbase.getUserByEmail(email)
            if user and check_password_hash(user['password'], password):
                userlogin = UserLogin().create(user)
                rm = True if request.form.get('remainme') else False
                login_user(userlogin, remember=rm)
                return redirect(url_for('main_page'))
        flash('Неверен пароль или логин', 'error')
    return render_template('login.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта!', 'success')
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
