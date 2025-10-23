from ..models.user import User
from ..extensions import db
from flask_jwt_extended import create_access_token
from ..utils.validators import validate_registration_data, validate_login_data

def register_user(data):
    errors = validate_registration_data(data)
    if errors:
        return {"error": errors}, 400

    if User.query.filter_by(username=data["username"]).first():
        return {"error": "Username already exists"}, 400
    if User.query.filter_by(email=data["email"]).first():
        return {"error": "Email already exists"}, 400

    user = User(
        username=data["username"],
        email=data["email"],
        nama=data["nama"]
    )
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return {"message": "Registrasi berhasil"}, 201


def login_user(data):
    errors = validate_login_data(data)
    if errors:
        return {"error": errors}, 400

    user = User.query.filter_by(username=data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return {"error": "Invalid username or password"}, 401

    token = create_access_token(identity=str(user.id))
    return {"message": "Login berhasil", "token": token, "user": user.to_dict()}, 200


def get_all_users():
    users = User.query.all()
    return {"users": [u.to_dict() for u in users]}, 200


def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.nama = data.get("nama", user.nama)

    if "password" in data:
        user.set_password(data["password"])

    db.session.commit()
    return {"message": "Data user berhasil diperbarui"}, 200


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()
    return {"message": "User berhasil dihapus"}, 200

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}, 404
    return {"user": {"id": user.id, "nama": user.nama, "email": user.email, "username": user.username}}, 200