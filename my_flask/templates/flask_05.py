from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/<name>/<lastname>')
def success(name, lastname):
    return f'Hello {name} {lastname}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        lastname = request.form['lastname']
        return redirect(url_for('success', name=user, lastname=lastname))
    else:
        user = request.args.get('name')
        lastname = request.args.get('lastname')
        return redirect(url_for('success', name=user, lastname=lastname))


if __name__ == '__main__':
    app.run()
