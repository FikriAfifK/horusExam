from flask import Flask
from .config import Config
from .extensions import init_extensions
from .routes.users import bp as users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    app.register_blueprint(users_bp, url_prefix="/users")
    
    @app.route("/")
    def index():
        return "API is running!"

    return app