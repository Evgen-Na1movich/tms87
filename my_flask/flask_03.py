from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/qeust/<qeust>')
def hello_user(qeust):
    return f'Hello {qeust} as Geust'


@app.route('/user/<name>')
def user_name(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user', qeust=name))

if __name__ == '__main__':
    app.run()