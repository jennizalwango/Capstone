 
from flask import Flask
# from config import *
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

db = SQLAlchemy()


def db_setup(app):
    app.config.from_object('config')
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
    # shows = db.relationship("Show", backref=db.backref("showss", lazy=True))
  
    def __repr__(self):
      return f'<Actor: { self.name }>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String(120))

    # shows = db.relationship("Show", backref=db.backref("shows", lazy=True))

    def __repr__(self):
      return f'<Movie: { self.title }>'
    
    
    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink(title=req_title, recipe=req_recipe)
            drink.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.id == id).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
    '''
    def update(self):
        db.session.commit()
      
# # db.init_app(app)
# # db.create_all()
