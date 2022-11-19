from project.common.finance_model import FinanceModel


class CurrencyModel(FinanceModel):
    def get_currencies(self):
        self.cursor.execute("SELECT name, initials, symbol FROM financial_project.currency")
        return self.cursor.fetchall()

    def get_single_currency(self, id_currency):
        self.cursor.execute("SELECT name, initials, symbol FROM financial_project.currency WHERE idcurrency={}".format(id_currency))
        return self.cursor.fetchone()
