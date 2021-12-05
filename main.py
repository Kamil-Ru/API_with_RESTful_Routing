from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import pprint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    data = Cafe.query.all()
    random_data = random.choice(data)

    return jsonify(data=random_data.to)


        jsonify(data=jsonify(
        id=random_data.id,
        map_url=random_data.map_url,
        img_url=random_data.img_url,
        location=random_data.location,
        seats=random_data.seats,
        has_toilet=random_data.has_toilet,
        has_wifi=random_data.has_wifi,
        has_sockets=random_data.has_sockets,
        can_take_calls=random_data.can_take_calls,
        coffee_price=random_data.coffee_price
    ).json)

    # random_cafe = movie_to_update = Cafe.query.get(movie_id)

    # print(random_cafe)

    # Movie.query.order_by(Movie.rating.desc()).all()


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
