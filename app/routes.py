# Implement the API endpoints (GET /users, POST /users, PUT /users/{id}, DELETE /users/{id})

from flask import Blueprint, request, jsonify
from app.models import User
from app.database import db


user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
# retrieve data
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])

# @user_routes.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()  
#     user_list = [
#         {"id": user.id, "name": user.name, "email": user.email}
#         for user in users
#     ]
#     return jsonify(user_list)

@user_routes.route('/users', methods=['POST'])
# add new data
def create_user():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_routes.route('/users/<int:id>', methods=['PUT'])
# update data
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@user_routes.route('/users/<int:id>', methods=['DELETE'])
# remove data
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

@user_routes.route('/', methods=['GET'])
def home():
    users = User.query.all()  
    user_list = [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ]
    return jsonify(user_list)
    # return "YOU DID IT TSHILIDZI!!!!"



