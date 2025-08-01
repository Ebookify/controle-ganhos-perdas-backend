
from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/me')
def me():
    return jsonify({'nome': 'Gerente', 'cargo': 'gerente'})
