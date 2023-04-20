from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/livematch')
def livematch():
    return render_template('live-match.html')


@app.route('/fixtures')
def fixtures():
    return render_template('fixtures.html')


@app.route('/standings')
def standings():
    return render_template('standings.html')


@app.route('/highlights')
def highlights():
    return render_template('highlights.html')


if __name__ == '__main__':
    app.run()
