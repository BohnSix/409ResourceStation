from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from App.models import init_db
from App.views import blue

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(blueprint=blue)

init_db(app)
manager = Manager(app)
Bootstrap(app)


if __name__ == '__main__':
    manager.run()
