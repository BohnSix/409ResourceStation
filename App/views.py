import random

from flask import Blueprint, render_template

from App.models import Person, db

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/create_db')
def create_db():
    db.create_all()
    return 'DB CREATE SUCCESS'


@blue.route('/addperson/')
def add_person():
    p = Person()
    p.p_name = '睡着了， 拉出去枪毙%d下' % random.randrange(100)
    db.session.add(p)
    db.session.commit()
    return 'PERSON ADD SUCCESS'


@blue.route('/videopage/')
def videopage():
    return render_template("videopage.html")

