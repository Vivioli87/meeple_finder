import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# create a new landing page but for now use games list page
@app.route("/")
@app.route("/get_games")
def get_games():
    games = mongo.db.games.find()
    return render_template("games.html", games=games)


@app.route("/get_game_detail/<game_id>")
def get_game_detail(game_id):

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    return render_template("game_detail.html", game=game)


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
