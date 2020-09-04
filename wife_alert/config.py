import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    # CSRF_ENABLED = True
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
    # SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    # WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
    # MAIL_SERVER = "localhost"
    # MAIL_PORT = 8025


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
