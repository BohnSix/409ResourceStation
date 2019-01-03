from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/<videoname>')
def video():
    return render_template(url_for('/<videoname>', VideoName = videoname))


if __name__ == '__main__':
    app.run()
