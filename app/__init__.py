from flask import Flask
from dotenv import load_dotenv
from app.controller.user_controller import user_bp
from app.data.store import seed_data
from config.config import config_by_name

load_dotenv()

def create_app(config_name: str = None) -> Flask:
    # 1. Resolve config profile
    if config_name is None:
        config_name = os.environ.get("FLASK_ENV", "default")

    config_class = config_by_name.get(config_name, config_by_name["default"])

    # 2. Create app and load config layer
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 3. Seed data if config allows
    if app.config.get("SEED_DATA"):
        seed_data()

    # register blueprint (routing)
    app.register_blueprint(user_bp)

    # default health check endpoint
    @app.route("/health")
    def health():
        return {
            "status": "Active", 
            "service": "hrms-api", 
            "version": "1.0.0"
        }


    return app

