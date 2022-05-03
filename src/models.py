from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),  nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120),  nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(120),  nullable=False)
    mass = db.Column(db.Integer,  nullable=False)
    hair_color = db.Column(db.String(120),  nullable=False)
    skin_color = db.Column(db.String(120),  nullable=False)
    eye_color = db.Column(db.String(120),  nullable=False)
    gender = db.Column(db.String(120),  nullable=False)
    height = db.Column(db.Integer,  nullable=False)
    homeworld = db.Column(db.String(120),  nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "height": self.height,
            "homeworld": self.homeworld
            # do not serialize the password, its a security breach
        }
        
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planets = db.Column(db.String(120),  nullable=False)
    characters = db.Column(db.String(120),  nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "planets": self.planet_name,
            "Characters": self.characters,
            # do not serialize the password, its a security breach
        }