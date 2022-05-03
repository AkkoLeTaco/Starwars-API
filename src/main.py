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
    people_list = list(map(lambda x: x. serialize(), people))

    return jsonify(people_list), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def handle_person(id):
  pass

@app.route('/planets', methods=['GET'])
def handle_planets():
    planet = Planet.query.all()
    planet_list = list(map(lambda y: y. serialize(), planet))

    return jsonify(planet_list), 200

@app.route('/characters', methods=['GET'])
def handle_characters():
    characters =  Characters.query.all()
    character_list = list(map(lambda z: z. serialize(), characters))

    return jsonify(character_list), 200

@app.route('/favorites', methods=['GET'])
def handle_favorites():
    favorites = Favorites.query.all()
    favorite_list = list(map(lambda z: z. serialize(), favorites))

    return jsonify(favorite_list), 200


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
