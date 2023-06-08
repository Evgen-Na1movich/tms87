from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'

@app.route('/my_world/<world>')
def my_world(name):
    if name %2 == 0 :
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', qeust=name))