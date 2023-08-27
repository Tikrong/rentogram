import os


class BaseConfig:

    APP_PORT = os.environ.get("APP_PORT", default="8000")
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SEND_FILE_MAX_AGE_DEFAULT = 3600

    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(base_dir, 'project.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_SORT_KEYS = False


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False