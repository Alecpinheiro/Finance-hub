from project import app
from flaskext.mysql import MySQL
import pymysql

mysql_connection = MySQL(app, prefix="mysql", host="localhost", user="root", password="lulamolusco8",
                         db="financial_project", autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql_connection.init_app(app)


class FinanceModel:
    def __init__(self):
        self.cursor = mysql_connection.get_db().cursor()
