from flask import Blueprint, jsonify

users_bp = Blueprint('users', __name__, url_prefix='/api')

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": []})
