import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    wedding = datetime.datetime(2022, 6, 18, 0, 0, 0)
    diff = (wedding - now).days

    return render_template('index.html', diff=diff)

if __name__ == '__main__':
    app.run()