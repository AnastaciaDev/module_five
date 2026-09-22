from flask import Flask
from dotenv import load_dotenv
from app.controller.user_controller import user_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    # app.config.from_object("config.Developement")

    # extension

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

