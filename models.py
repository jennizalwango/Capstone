
from flask_sqlalchemy import SQLAlchemy

DATABASE_PATH = 'postgres://sgxcqirecstqak:3aef306fac7303731134404c39175767d14399b6cfb94b2a3c63937d25794924@ec2-3-220-86-239.compute-1.amazonaws.com:5432/d6hj3k2cvv4nq1'
db = SQLAlchemy()

def db_setup(app, database_path = DATABASE_PATH):
    app.config['SQLALCHEMY_DATABASE_URI']= database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.app = app
    db.init_app(app)
    db.create_all()
    


class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    
    def __init__(self, name, age, gender):
        self.name = name,
        self.age = age,
        self.gender = gender
    
    def format(self):
        '''
        serialize Actor table data for a json object
        '''
        return{
            'id': self.id,
            'name': self.name,
            'age' : self.age,
            'gender': self.gender
        }


class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String(120))
    
    def __init__(self, title, release_date):
        self.title = title,
        self.release_date = release_date


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        
    
    def format(self):
        '''
        serialize Actor table data for a json object
        '''
        return{
            'id': self.id,
            'title': self.title,
            'release_date' : self.release_date
        }
      
# db.init_app(app)
# db.create_all()
