 
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

database_path = 'postgres://hkkekeqmxyxrss:fccdc54c7ca9c40dea56c6326c05c57ff2e2afbbd8a5fb7407314b3064ffac30@ec2-52-55-59-250.compute-1.amazonaws.com:5432/d3l49h14ujn7on'

db = SQLAlchemy()

def db_setup(app, database_path = database_path):
    app.config.from_object('config')
    app.config['SQLALCHEMY_DATABASE_URL']= database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.app = app
    migrate = Migrate(app, db)
    db.init_app(app)
    return db


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    gender = db.Column(db.String(120))

    def __repr__(self):
      return f'<Actor: { self.name }>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String(120))


    def __repr__(self):
      return f'<Movie: { self.title }>'


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
      
# # db.init_app(app)
# # db.create_all()
