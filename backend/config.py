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

SQLALMEMY_DATABASE_URI = 'postgres://aynfsfqgbdvyfp:a9d37d905a49931414b728b2e754d910a149028de26647eee8d2abf5e9e07b33@ec2-54-174-221-35.compute-1.amazonaws.com:5432/d8fqcfq8mq61n7'