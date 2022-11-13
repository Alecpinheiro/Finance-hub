import pandas as pd
import pymysql
from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql_connection = MySQL(app, prefix="mysql", host="localhost", user="root", password="lulamolusco8",
                         db="financial_project", autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql_connection.init_app(app)

@app.route('/users', methods=['GET', 'POST', 'PUT'])
def get_users():
    cursor = mysql_connection.get_db().cursor()

    if request.method == 'GET':
        cursor.execute("SELECT name FROM financial_project.user")
        users = cursor.fetchall()
        return jsonify(users)

    if request.method == 'POST':
        new_user = request.form
        user_name = new_user['name']
        cursor.execute("INSERT INTO financial_project.user (name) values('{}')".format(user_name))
        return jsonify(new_user)

@app.route('/users/<id_user>/', methods=['GET', 'PUT'])
def single_user(id_user=0):
    cursor = mysql_connection.get_db().cursor()

    if request.method == 'PUT':
        user_update = request.form
        user_name = user_update['name']
        cursor.execute("UPDATE financial_project.user SET name='{}'  WHERE iduser={}".format(user_name, id_user))
        return jsonify(user_update)

    if request.method == 'GET':
        cursor.execute("SELECT name FROM financial_project.user WHERE iduser={}".format(id_user))
        user = cursor.fetchone()
        return jsonify(user)


# run api
app.run(debug=True)

# link = 'http://127.0.0.1:5000/getsell'
#
# request = requests.get(link)
#
# print(request)
# print(request.json())
#
# dictionary = request.json()
# print(dictionary['total_sell'])
