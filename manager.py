from flask import Flask
from flask_script import Manager
from App.views import blue
# from App.view2 import blue as blue2

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'
app.register_blueprint(blueprint=blue)
# app.register_blueprint(blueprint=blue2)
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
