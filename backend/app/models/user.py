from sqlalchemy.sql import func
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    nama = db.Column(db.VARCHAR(100), nullable=False)
    password_hash = db.Column(db.VARCHAR(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nama": self.nama,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None
        }

    def __repr__(self):
        return f"<User {self.username}>"