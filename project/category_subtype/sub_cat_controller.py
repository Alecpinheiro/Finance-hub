from project import app
from flask import jsonify, request

from project.category_subtype.sub_cat_model import SubCategoryModel


@app.route('/subcategories', methods=['GET', 'POST'])
def get_subcategories():
    sub_category_model = SubCategoryModel()

    if request.method == 'GET':
        sub_categories_list = sub_category_model.get_subcategories()
        return jsonify(sub_categories_list)

    if request.method == 'POST':
        sub_category_name = request.form['name']
        new_sub_category = sub_category_model.new_sub_category(sub_category_name)
        return jsonify(new_sub_category)


@app.route('/subcategories/<idcategory_subtype>/', methods=['GET', 'PUT'])
def single_subcategory(idcategory_subtype=0):
    sub_category_model = SubCategoryModel()

    if request.method == 'PUT':
        sub_category_name = request.form['name']
        updated_subcategory = sub_category_model.update_subcategory(sub_category_name, idcategory_subtype)
        return jsonify(updated_subcategory)

    if request.method == 'GET':
        single_subcategory = sub_category_model.get_single_subcategory(idcategory_subtype)
        return jsonify(single_subcategory)
