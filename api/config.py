import os


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://USER:PASSWORD@172.17.0.2:3306/sakila"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://USER:PASSWORD@172.17.0.2:3306/sakila'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


match os.getenv('ENV'):
    case 'DEV':
        config = DevConfig
    case 'TEST':
        config = TestConfig
    case _:
        config = ProdConfig
