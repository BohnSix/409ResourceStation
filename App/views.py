from flask import blueprints
from manager import app


blue = blueprints('first_blue', __name__)


@app.route('/')
def hello_world():
    return "Hello world"
