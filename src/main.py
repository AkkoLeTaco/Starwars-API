"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planet, Characters, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def handle_hello():

    people = People.query.all()
    people_list = list(map(lambda x: x.serialize(), people))

    return jsonify(people_list), 200

@app.route('/people', methods=['POST'])
def create_people():

    request_body = request.get_json()
    new_person = People(email=request_body['email'], password=request_body['password'], is_active=request_body['is_active'])
    db.session.add(new_person)
    db.session.commit()
    return f"The new user {request_body['email']} was created sucessfully", 200

@app.route('/people/<int:people_id>', methods=['GET'])
def handle_person(id):
    people = People.query.get(people_id)
    return (people.serialize())

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_person(id):
    person1 = Person.query.get(person_id)
    if person1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(person1)
    db.session.commit()
    return f"The user {request_body['email']} was removed sucessfully", 200


@app.route('/planets', methods=['GET'])
def handle_planets():
    planet = Planet.query.all()
    planet_list = list(map(lambda y: y.serialize(), planet))
    return jsonify(planet_list), 200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def handle_planet(id):
    planets = Planet.query.get(planets_id)
    return (planets.serialize())

@app.route('/planets', methods=['POST'])
def create_planets():
    request_planets = request.get_json()
    new_planet = Planet(planet_name=request_planets['planet_name'], climate=request_planets['climate'])
    db.session.add(new_planet)
    db.session.commit()
    return f"The planet {request_planets['planet_name']} was created sucessfully", 200

@app.route('/planets/<int:planets_id>', methods=['DELETE'])
def delete_planet(id):
    planet1 = Planet.query.get(planets_id)
    if planet1 is None:
        raise APIException('planet not found', status_code=404)
    db.session.delete(planet1)
    db.session.commit()
    return f"The planet {request_planets['planet_name']} was removed sucessfully", 200

@app.route('/characters', methods=['GET'])
def handle_characters():
    characters =  Characters.query.all()
    character_list = list(map(lambda z: z.serialize(), characters))

    return jsonify(character_list), 200

@app.route('/characters/<int:characters_id>', methods=['GET'])
def handle_character(id):
    character = Planet.query.get(characters_id)
    return (characters.serialize())

@app.route('/characters', methods=['POST'])
def create_characters():
    request_characters = request.get_json()
    new_characters = Characters(character_name=request_characters['character_name'], mass=request_characters['mass'], hair_color=request_characters['hair_color'], skin_color=request_characters['skin_color'], eye_color=request_characters['eye_color'], gender=request_characters['gender'], height=request_characters['height'], homeworld=request_characters['homeworld'])
    db.session.add(new_characters)
    db.session.commit()
    return f"The character {request_characters['character_name']} was created sucessfully", 200

@app.route('/characters/<int:characters_id>', methods=['DELETE'])
def delete_character(id):
    character1 = Characters.query.get(characters_id)
    if character1 is None:
        raise APIException('character not found', status_code=404)
    db.session.delete(character1)
    db.session.commit()
    return f"The character {request_characters['character_name']} was removed sucessfully", 200

@app.route('/favorites', methods=['GET'])
def handle_favorites():
    favorites = Favorites.query.all()
    favorite_list = list(map(lambda z: z.serialize(), favorites))

    return jsonify(favorite_list), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
