import os

base_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """
    Base application configuration
    """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'thisissecret')


DATABASE_URI = 'postgres://gtkobtgaiovffn:ae5290ccf64770f13834b50250041cb0f83201359730308bd763ce72bbe9b9b0@ec2-34-224-55-230.compute-1.amazonaws.com:5432/da5sjir1610ap6
'
SQLALCHEMY_DATABASE_URL = DATABASE_URI