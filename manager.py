from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager

from App.views import app_blue

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'

app.register_blueprint(blueprint=app_blue)

manager = Manager(app)
Bootstrap(app)


if __name__ == '__main__':
    manager.run()
