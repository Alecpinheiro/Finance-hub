from project import app
from flask import jsonify, request

from project.currencies.currencies_model import CurrencyModel


@app.route('/currencies', methods=['GET'])
def get_currencies():
    currency_model = CurrencyModel()

    if request.method == 'GET':
        currencies_list = currency_model.get_currencies()
        return jsonify(currencies_list)


@app.route('/currencies/<id_currency>/', methods=['GET'])
def single_currency(id_currency=0):
    currency_model = CurrencyModel()

    if request.method == 'GET':
        single_currency = currency_model.get_single_currency(id_currency)
        return jsonify(single_currency)
