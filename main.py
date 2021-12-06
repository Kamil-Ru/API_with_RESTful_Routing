from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random
from pprint import pprint

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

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    data = db.session.query(Cafe).all()
    random_data = random.choice(data)
    return jsonify(data=random_data.to_dict())

@app.route("/all")
def get_all_cafe():
    data = db.session.query(Cafe).all()
    list = []
    for cafe in data:
        list.append(cafe.to_dict())
    return jsonify(list)

@app.route("/search")
def search():
    loc = request.args.get('loc')
    data = db.session.query(Cafe).filter(Cafe.location.like(loc)).order_by(Cafe.id).all()
    if not data:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify([cafe.to_dict() for cafe in data])





    # random_cafe = movie_to_update = Cafe.query.get(movie_id)

    # print(random_cafe)

    # Movie.query.order_by(Movie.rating.desc()).all()


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
