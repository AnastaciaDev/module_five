from app import create_app

flask_instance = create_app()


if __name__ == "__main":
    flask_instance.run()
