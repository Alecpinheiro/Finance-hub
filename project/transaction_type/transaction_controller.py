from project import app
from flask import jsonify, request

from project.transaction_type.transaction_model import TransactionModel


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transaction_model = TransactionModel()

    if request.method == 'GET':
        transactions_list = transaction_model.get_transactions()
        return jsonify(transactions_list)


@app.route('/transactions/<id_transaction>/', methods=['GET'])
def single_transaction(id_transaction=0):
    transaction_model = TransactionModel()

    if request.method == 'GET':
        single_transaction = transaction_model.get_single_transaction(id_transaction)
        return jsonify(single_transaction)
