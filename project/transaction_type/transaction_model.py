from project.common.finance_model import FinanceModel


class TransactionModel(FinanceModel):
    def get_transactions(self):
        self.cursor.execute("SELECT name FROM financial_project.transaction_type")
        return self.cursor.fetchall()

    def get_single_transaction(self, id_transaction):
        self.cursor.execute("SELECT name FROM financial_project.transaction_type WHERE idtransaction_type={}".format(id_transaction))
        return self.cursor.fetchone()
