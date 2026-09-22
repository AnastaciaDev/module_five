import os

class Config():
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///data.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    pass

class Developemnt(Config):
    pass

class Production(Config):
    pass

class Staging(Config):
    pass

class Testing(Config):
    pass
