from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from controllers import user_controller
from models.user_model import UserModel

user_bp = Blueprint('user_routes', __name__, url_prefix='/users')

@user_bp.route('/', methods=['POST'])
@jwt_required()
def create_user():
    data = request.json
    user = UserModel(
        name=data.get('name'), 
        email=data.get('email'), 
        password=data.get('password')
    )
    res = user_controller.create_user(user)
    return jsonify({'id': res.id, 'name': res.name, 'email': res.email}), 201

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = user_controller.get_users()
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    userId = UserModel(id=user_id)
    user = user_controller.get_user(userId)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.json
    user = UserModel(
        id = user_id,
        name = data.get('name'),
        email = data.get('email'),
        password = data.get('password')
    )
    updated = user_controller.update_user(user)
    if updated:
        return jsonify({'id': updated.id, 'name': updated.name, 'email': updated.email})
    return jsonify({'message': 'User not found'}), 404

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    userId = UserModel(id=user_id)
    deleted = user_controller.delete_user(userId)
    if deleted:
        return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'}), 404
