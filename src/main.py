from flask import Flask, render_template, request, redirect, url_for, send_file, g, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from DataBaseManager import DBManager
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename='data/log.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')

DATABASE = 'data\\LittleHeroDB.db'
UPLOAD_FOLDER = 'data\\upload\\maps'
gamePath = 'LittleHeroFiles/little_hero.zip'
creatorPath = 'LittleHeroFiles/creator.zip'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['SECRET_KEY'] = '23dadd556c0f820e6a81887f0c3f41bd90357ab9'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, UPLOAD_FOLDER)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, DATABASE)))

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Авторизуйтесь для доступа к данной странице'
login_manager.login_message_category = 'success'


def addMap(file):
    text = file.stream.read().decode('utf-8')
    text.replace('\r', '')
    text = text.split('\n')
    print(f'User name: {text[0]}')
    print(f'User email: {text[1]}')
    print(f'Upload date: {text[2]}')
    print(f'Map name: {text[3]}')
    print(f'Map description: {text[4]}')
    print(f'Map: {text[5]}')
    print('-----------------')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


def get_img():
    return


@app.route('/')
def main_page():
    return render_template('main.html', user=current_user)


@app.route('/downloadgame', methods=['POST'])
def download_game():
    return send_file(gamePath, as_attachment=True)


@app.route('/downloadcreater', methods=['POST'])
def download_creater():
    return send_file(creatorPath, as_attachment=True)


@app.route('/maps', methods=['GET'])
@login_required
def maps_library():
    return render_template('maps_library.html', user=current_user, maps=dbase.getMaps())


@app.route('/maps/<map_id>')
@login_required
def map_details(map_id):
    map = dbase.getMap(map_id)
    return render_template('map_details.html', user=current_user, creator=dbase.getUser(map[4]), map=map)


@app.route('/maps/upload_map', methods=['POST'])
@login_required
def upload_map():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('maps_library'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('maps_library'))
    if file and allowed_file(file.filename):
        text = file.stream.read().decode('utf-8')
        text.replace('\r', '')
        text = text.split('\n')
        _user_id = dbase.getUserByEmail(text[1].rstrip())[0]
        result = dbase.addMap(_user_id, text[3], text[4], text[5])
        if type(result) == str:
            if result == 'UNIQUE constraint failed: Maps.map':
                flash('Такая карта уже существует!', 'error')
            else:
                flash('Произошла какая-то ошибка, попробуйте позже!', 'error')
        else:
            flash('File upload!')
        return redirect(url_for('maps_library'))


@app.route('/api/upload_map', methods=['POST'])
def api_upload_map():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Success', 201


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        form = request.form.to_dict()
        if form:
            nickname = form['nickname']
            password = generate_password_hash(form['password'])
            email = form['email']
            if 'file' not in request.files:
                filename = 'user.png'
            else:
                file = request.files['file']
                if file.filename == '':
                    filename = 'user.png'
                elif file and allowed_file(file.filename):
                    filename = str(len(os.listdir('static/img')))
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = dbase.addUser(nickname, password, email, filename)
            if type(result) == str:
                if result == 'UNIQUE constraint failed: Users.username':
                    flash('Имя уже используется!', 'error')
                elif result == 'UNIQUE constraint failed: Users.email':
                    flash('Имя уже используется!', 'error')
                else:
                    flash('Произошла какая-то ошибка, попробуйте позже!', 'error')
                return render_template('registration.html')
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
