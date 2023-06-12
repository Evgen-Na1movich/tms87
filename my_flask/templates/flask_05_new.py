import csv
import os.path

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='/home/evgen/PycharmProjects/tms87/my_flask/templates')


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        with open('flask_users_05.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([user, lastname, age])
        return render_template('flask_05_added.html')
    else:
        return render_template('flask_05.html')


if __name__ == '__main__':
    if not os.path.exists('flask_users_05.csv'):
        with open('flask_users_05.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["user", "lastname", "age"])
    app.run()
