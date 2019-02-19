import random

from flask import Blueprint, render_template

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/video_page/<title>/')
def video_page(title):
    return render_template("video_page.html", title=title)

