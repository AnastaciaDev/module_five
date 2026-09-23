from flask import Flask
from dotenv import load_dotenv
from app.controller import create_member_blueprint

from app.repository.member_repo import MemberRepoWithDataStructures

from app.services import MemberService

from app.data.store import seed_data, store
from config.config import config_by_name

import os

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

    # Wiring thing up
    member_repository = MemberRepoWithDataStructures(store)

    member_service = MemberService(member_repository)

    # register blueprint (routing)
    app.register_blueprint(create_member_blueprint(member_service))

    # default health check endpoint
    @app.route("/health")
    def health():
        return {
            "status": "Active", 
            "service": "hrms-api", 
            "version": "1.0.0"
        }


    return app

