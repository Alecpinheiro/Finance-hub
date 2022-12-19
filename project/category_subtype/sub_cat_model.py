from project.common.finance_model import FinanceModel


class SubCategoryModel(FinanceModel):
    def get_subcategories(self):
        self.cursor.execute("SELECT name FROM financial_project.category_subtype")
        return self.cursor.fetchall()

    def new_sub_category(self, subcategory_name, category_idcategory):
        self.cursor.execute("INSERT INTO financial_project.category_subtype (name, category_idcategory) values('{}')".format(subcategory_name, category_idcategory))

    def update_subcategory(self, subcategory_name, idcategory_subtype):
        self.cursor.execute(
            "UPDATE financial_project.category_subtype SET name='{}'  WHERE idcategory_subtype={}".format(subcategory_name, idcategory_subtype))

    def get_single_subcategory(self, idcategory_subtype):
        self.cursor.execute("SELECT name FROM financial_project.category_subtype WHERE idcategory_subtype={}".format(idcategory_subtype))
        return self.cursor.fetchone()
