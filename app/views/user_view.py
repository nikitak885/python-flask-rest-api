from flask import Blueprint, request, jsonify
from ..controller.user_controller import get_all_users, create_user

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    """API endpoint to get all users"""
    users = get_all_users()
    return jsonify([{'id': u.id, 'username': u.username, 'email': u.email} for u in users]), 200

@user_blueprint.route('/users', methods=['POST'])
def add_user():
    """API endpoint to create a new user"""
    data = request.get_json()
    new_user = create_user(data['username'], data['email'])
    return jsonify({'id': new_user.id, 'username': new_user.username, 'email': new_user.email}), 201
