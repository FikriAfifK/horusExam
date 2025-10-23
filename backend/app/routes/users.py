from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..services.user_service import (
    register_user, login_user, get_all_users, update_user, delete_user, get_user_by_id
)

bp = Blueprint("users", __name__)

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result, status = register_user(data)
    return jsonify(result), status

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result, status = login_user(data)
    return jsonify(result), status

@bp.route("/", methods=["GET"])
@jwt_required()
def get_users():
    result, status = get_all_users()
    return jsonify(result), status

@bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update(user_id):
    data = request.get_json()
    result, status = update_user(user_id, data)
    return jsonify(result), status

@bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete(user_id):
    result, status = delete_user(user_id)
    return jsonify(result), status

@bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    result, status = get_user_by_id(user_id)
    return jsonify(result), status