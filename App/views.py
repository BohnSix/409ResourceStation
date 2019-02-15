from flask import Blueprint, render_template, request, Response, url_for, session
from werkzeug.utils import redirect

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def hello_world():
    return render_template('index.html')


@blue.route('/home/')
def home():
    username = session.get('user')

    return render_template('home.html', username=username)


@blue.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        username = request.form.get('username')
        print(username)

        session['user'] = username
        resp = Response(response='登陆成功:%s' % username)
        resp.set_cookie('user', username)
        return resp


@blue.route('/logout/')
def logout():
    resp = redirect(url_for('first_blue.home'))
    resp.delete_cookie('user')
    return resp


@blue.route('/mine/')
def mine():
    return render_template('mine.html')
