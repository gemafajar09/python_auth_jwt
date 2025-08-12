from controllers import auth_controller
from flask import Blueprint, request, jsonify
from models.user_model import UserModel

auth_bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserModel(
        email=data.get('email'), 
        password=data.get('password')
    )
    access_token = auth_controller.login(user)
    if access_token:
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Invalid email or password"}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = UserModel(
        name=data.get('name'), 
        email=data.get('email'), 
        password=data.get('password')
    )
    res = auth_controller.register(user)
    return jsonify({'id': res.id, 'name': res.name, 'email': res.email}), 201