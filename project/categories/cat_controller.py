from project import app
from flask import jsonify, request

from project.categories.cat_model import CategoryModel


@app.route('/categories', methods=['GET', 'POST'])
def get_categories():
    category_model = CategoryModel()

    if request.method == 'GET':
        categories_list = category_model.get_categories()
        return jsonify(categories_list)

    if request.method == 'POST':
        category_name = request.form['name']
        new_category = category_model.new_category(category_name)
        return jsonify(new_category)


@app.route('/categories/<id_category>/', methods=['GET', 'PUT'])
def single_category(id_category=0):
    category_model = CategoryModel()

    if request.method == 'PUT':
        category_name = request.form['name']
        updated_category = category_model.update_category(category_name, id_category)
        return jsonify(updated_category)

    if request.method == 'GET':
        single_category = category_model.get_single_category(id_category)
        return jsonify(single_category)
