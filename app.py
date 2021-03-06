import json
import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from auth import AuthError, requires_auth
from models import Movie, Actor, db_setup, db

## ROUTES
def create_app():
    app = Flask(__name__)
    db_setup(app)
    CORS(app)
     

    @app.route('/')
    def home():
        return 'Welcome to capstone' 
              

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_all_movies():
        
        movies = Movie.query.all()
            
        return jsonify({
            "success": True,
            "all_movies": [movies.format() for movies in movies]
        }),200
        

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie():
        
        data = request.get_json()
        
        title = data.get('title')
        release_date = data.get('release_date')
        
        movie = Movie(title=title, release_date=release_date)
        movie.insert()
        return jsonify({
            'success': True, 
            'movies': movie.format()
        })
        
        
    @app.route('/movies/<int:id>', methods =['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(id):
        data = request.get_json()
                
        movies = Movie.query.filter(Movie.id ==id).one_or_none()

        if not movies:
            abort(404)
            
        movies.title = data.get('title', movies.title)
        movies.update()
        
        return jsonify ({
            "success":True,
            "movies": movies.format()
        }),  200
        
        
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(id):
        
        movie = Movie.query.filter(Movie.id ==id).one_or_none()
        
        if not movie:
            abort(404)
            
        movie.delete()
        
        return jsonify({
            "success": True,
            "delete": id
        }), 200
        

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_all_actors():
        
        actors = Actor.query.all()
        return jsonify({
            "success": True,
            "all_actors": [actors.format() for actors in actors]
        }),200
        

    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor():
        
        data = request.get_json()
        
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        
        actor = Actor(
            name=name, 
            age=age, 
            gender=gender
            )
        db.session.add(actor)
        db.session.commit()
          
        return jsonify({
            'success': True, 
            'actors': actor.format()
        }), 201
        

    @app.route('/actors/<int:id>', methods =['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(id):
        data = request.get_json()
        
        actor = Actor.query.filter(Actor.id ==id).one_or_none()
                
        if not actor:
            abort(404)
        
        actor.name = data.get('name', actor.name)
        actor.age = data.get('age', actor.age)
        actor.gender = data.get('gender', actor.gender)  
        db.session.commit()
        
        return jsonify ({
            "success":True,
            "actors": actor.format()
        }), 200
        
        
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(id):
        
        actor = Actor.query.filter(Actor.id ==id).one_or_none()
        
        if not actor:
            abort(404)
            
        # actor.delete()
        db.session.add(actor)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "delete": id
        }), 200
        
    ## Error Handling
    '''
    Example error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False, 
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    '''
    @TODO implement error handler for 404
        error handler should conform to general task above 
    '''

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False, 
            "error": 404,
            "message": "resource not found"
        }), 404


    '''
    @TODO implement error handler for AuthError
        error handler should conform to general task above 
    '''
    @app.errorhandler(405)
    def permission_error(error):
        return jsonify({
            "success": False,
            "error":405,
            "message": "Authentication error"
        }), 405
        
    @app.errorhandler(400)
    def user_error(error):
        return jsonify({
            "sucess":False,
            "error":400,
            "message":error.description
        }),400
        
    return app
app = create_app()

if __name__ =='__main__':
    app.run()