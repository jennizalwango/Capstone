import json

from flask import Flask, request, jsonify, abort
from auth import requires_auth

from models import Movie, Actor, db_setup

app = Flask(__name__)


# db_drop_and_create_all()

## ROUTES

@app.route('/')
def home():
    return jsonify({
        'success': True,
        'message': 'Welcome to capstone'   
    })

@app.route('/movies')
@requires_auth('get:movies')
def get_all_movies():
    
    movies = Movie.query.all()
    return jsonify({
        "success": True,
        "drinks": movies
    }),200
    

@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movie():
    
    data = request.get_json()
    
    title = data.get('title')
     
    movie = Movie(title=title)
    movie.insert()
    return jsonify({
        'success': True, 
        'drinks': movie
    })
     
     
@app.route('/movies/<int:id>', methods =['PATCH'])
@requires_auth('patch:movies')
def edit_movie(id):
    data = request.get_json()
    
    movie = data.get('movie')
    
    movies = Movie.query.filter(Movie.id ==id).one_or_none()

    if not movie:
        abort(404)
        
    movies.update()
    return jsonify ({
        "success":True,
        "movies": movies 
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
    })
    

@app.route('/actors')
@requires_auth('get:actors')
def get_all_actors():
    
    actors = Actor.query.all()
    return jsonify({
        "success": True,
        "drinks": actors
    }),200
    

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actor():
    
    data = request.get_json()
    
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
     
    actor = Actor(name=name, age=age, gender=gender)
    actor.insert()
    return jsonify({
        'success': True, 
        'actors': actor
    })
     

@app.route('/actors/<int:id>', methods =['PATCH'])
@requires_auth('patch:actors')
def edit_actors(id):
    data = request.get_json()
    
    actor = data.get('actor')
    
    actors = Actor.query.filter(Actor.id ==id).one_or_none()

    if not actor:
        abort(404)
        
    actors.update()
    return jsonify ({
        "success":True,
        "movies": actors 
    }),  200
    
    
@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(id):
    
    actor = Actor.query.filter(Actor.id ==id).one_or_none()
    
    if not actor:
        abort(404)
        
    actor.delete()
    
    return jsonify({
        "success": True,
        "delete": id
    })
    
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
    
