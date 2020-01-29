import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'thisissecret')


# class DevelopmentConfig(BaseConfig):
#     """
#     Development application configuration
#     """
#     DEBUG = True
#
#
# class TestingConfig(BaseConfig):
#     """
#     Testing application configuration
#     """
#     DEBUG = True
#     TESTING = True
#     DATABASE_NAME = "testdb"
#
#
# class ProductionConfig(BaseConfig):
#     """
#     Production application configuration
#     """
#     DEBUG = False

SQLALMEMY_DATABASE_URI = 'postgres://hkkekeqmxyxrss:fccdc54c7ca9c40dea56c6326c05c57ff2e2afbbd8a5fb7407314b3064ffac30@ec2-52-55-59-250.compute-1.amazonaws.com:5432/d3l49h14ujn7on'
