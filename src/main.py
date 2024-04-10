from flask import Flask, render_template, request, redirect, url_for, send_file, g
from flask_login import LoginManager
from UserLogin import UserLogin
from DataBaseManager import DBManager
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, filename='data/log.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

DATABASE = '/data/LittleHeroDB.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '23dadd556c0f820e6a81887f0c3f41bd90357ab9'
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'data\\LittleHeroDB.db')))

login_manager = LoginManager(app)


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
def close_db():
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
    return render_template('main.html')


@app.route('/download', methods=['POST'])
def download():
    path = 'LittleHeroFiles/test.txt'
    return send_file(path, as_attachment=True)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        form = request.form.to_dict()
        if form:
            nickname = form['nickname']
            login = form['login']
            password = form['password']
            email = form['email']
            result = dbase.addUser(nickname, login, password, email)

            if not result:
                return render_template('registration.html', errors=True)
            else:
                return redirect(url_for('main_page'))

    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form.to_dict()
        if form:
            login = form['login']
            password = form['password']
    return render_template('login.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 8080, debug=True)
