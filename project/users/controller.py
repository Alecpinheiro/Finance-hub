from project import app
from flask import jsonify, request

from project.users.model import UserModel


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    user_model = UserModel()

    if request.method == 'GET':
        users_list = user_model.get_users()
        return jsonify(users_list)

    if request.method == 'POST':
        user_name = request.form['name']
        new_user = user_model.new_user(user_name)
        return jsonify(new_user)


@app.route('/users/<id_user>/', methods=['GET', 'PUT'])
def single_user(id_user=0):
    user_model = UserModel()

    if request.method == 'PUT':
        user_name = request.form['name']
        updated_user = user_model.update_user(user_name, id_user)
        return jsonify(updated_user)

    if request.method == 'GET':
        single_user = user_model.get_single_user(id_user)
        return jsonify(single_user)
