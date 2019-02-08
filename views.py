from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap

# CONFIGURATION
DATABASE = ''
DEBUG = False
SECRET_KEY = 'development key'
MANAGER_NAME = 'admin'
MANAGER_PWD = '123456'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("FLASK_SETTINGS", silent=True)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('templates/index.html')


@app.route("/manager_login", methods=['GET', "POST"])
def manager_login():
    error = None
    if request.method == "POST":
        if request.form["username"] != app.config["MANAGER_NAME"]:
            error = "invalid username"
        elif request.form["password"] != app.config["MANAGER_PWD"]:
            error = "invalid password"
        else:
            session.user_id = app.config["MANAGER_NAME"]
            return redirect(url_for('manager', error=error))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/videopage/<num>')
def play():
    return render_template("videopage.html", num=num)


def manager_judge():
    if not session['user_id']:
        error = 'Invalid manager, please log in'
        return redirect(url_for('manager_login', error=error))


@app.route('/manager')
def manager():
    manager_judge()
    return redirect(url_for('manager'))


if __name__ == '__main__':
    app.run()
