from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/')
def index():
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)