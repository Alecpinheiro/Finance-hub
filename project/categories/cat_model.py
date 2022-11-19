from project.common.finance_model import FinanceModel


class CategoryModel(FinanceModel):
    def get_categories(self):
        self.cursor.execute("SELECT name FROM financial_project.category")
        return self.cursor.fetchall()

    def new_category(self, category_name):
        self.cursor.execute("INSERT INTO financial_project.category (name) values('{}')".format(category_name))

    def update_category(self, category_name, id_category):
        self.cursor.execute(
            "UPDATE financial_project.category SET name='{}'  WHERE idcategory={}".format(category_name, id_category))

    def get_single_category(self, id_category):
        self.cursor.execute("SELECT name FROM financial_project.category WHERE idcategory={}".format(id_category))
        return self.cursor.fetchone()
