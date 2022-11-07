import pandas as pd
import pymysql
from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql_connection = MySQL(app, prefix="mysql", host="localhost", user="root", password="lulamolusco8", db="financial_project", autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql_connection.init_app(app)


#develop functions
@app.route('/')
def homepage():
    return 'The API is on'

@app.route('/getusers')
def get_users():
    cursor = mysql_connection.get_db().cursor()
    cursor.execute("SELECT name FROM financial_project.user")
    users = cursor.fetchall()
    return jsonify(users)

#run api
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



