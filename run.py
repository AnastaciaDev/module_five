import os
from app import create_app

# You can hardcode a profile here, or let FLASK_ENV drive it
config_name = os.environ.get("", "")
flask_instance = create_app(config_name)

if __name__ == "__main__":
    flask_instance.run()
