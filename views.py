from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/videopage')
def video():
    return render_template("videopage.html")


if __name__ == '__main__':
    app.run()
