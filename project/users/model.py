from project.common.finance_model import FinanceModel


class UserModel(FinanceModel):
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
