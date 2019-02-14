from flask import Blueprint, url_for

blue = Blueprint('second_blur', __name__)


@blue.route('/')
def index():
    return 'Index'


@blue.route('/urlfor/')
def index():
    result = url_for('first_blue.index')
    return result

