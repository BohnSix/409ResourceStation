import random

from flask import Blueprint, render_template

app_blue = Blueprint('app', __name__)


@app_blue.route('/')
def index():
    return render_template('index.html')


@app_blue.route('/local')
def local():
    return render_template('local_file.html')


@app_blue.route('/video_page/<title>/')
def video_page(title):
    return render_template("video_page.html", title=title)

