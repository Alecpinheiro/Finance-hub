from project import app
from flaskext.mysql import MySQL
import pymysql

mysql_connection = MySQL(app, prefix="mysql", host="localhost", user="root", password="lulamolusco8",
                         db="financial_project", autocommit=True, cursorclass=pymysql.cursors.DictCursor)
mysql_connection.init_app(app)


class UserModel:
    def __init__(self):
        self.cursor = mysql_connection.get_db().cursor()

    def get_users(self):
        self.cursor.execute("SELECT name FROM financial_project.user")
        return self.cursor.fetchall()

    def new_user(self, user_name):
        self.cursor.execute("INSERT INTO financial_project.user (name) values('{}')".format(user_name))

    def update_user(self, user_name, id_user):
        self.cursor.execute("UPDATE financial_project.user SET name='{}'  WHERE iduser={}".format(user_name, id_user))

    def get_single_user(self, id_user):
        self.cursor.execute("SELECT name FROM financial_project.user WHERE iduser={}".format(id_user))
        return self.cursor.fetchone()
