import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_args
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Pagination game limit
PER_PAGE = 8

TODAY = date.today().strftime("%d/%m/%y")

# Pagination functions


# Pagination - see code credit in readme
def paginated(games):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return games[offset: offset + PER_PAGE]


def pagination_args(games):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(games)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


# home/game page for users not logged in
@app.route("/")
@app.route("/games_non_user")
def games_non_user():
    games = list(mongo.db.games.find())
    games_paginated = paginated(games)
    pagination = pagination_args(games)
    return render_template("games_non_user.html",
                           games=games_paginated,
                           pagination=pagination)


# home/game page for users logged in
@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    games_paginated = paginated(games)
    pagination = pagination_args(games)
    username = session["user"]
    return render_template("games.html",
                           games=games_paginated,
                           username=username,
                           pagination=pagination)


# game detail page
@app.route("/get_game_detail/<game_id>")
def get_game_detail(game_id):

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    reviews = mongo.db.reviews.find({"id_of_game": str(game["_id"])})
    if reviews.count() == 0:
        reviews = []
    return render_template("game_detail.html",
                           game=game,
                           reviews=reviews)


# add/edit/delete review functions
@app.route("/add_review/<game_id>", methods=["GET", "POST"])
def add_review(game_id):
    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})

    if request.method == "POST":
        review = {
            "id_of_game": str(game["_id"]),
            "name": request.form.get("name"),
            "review_comments": request.form.get("review_comments"),
            "created_by": session["user"],
            "created_date": TODAY
        }

        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for('get_game_detail', game_id=game_id))

    return render_template("add_review.html", game=game)


@app.route("/edit_review/<game_id>/<review_id>", methods=["GET", "POST"])
def edit_review(game_id, review_id):
    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    if request.method == "POST":
        submit = {
            "id_of_game": review["id_of_game"],
            "name": review["name"],
            "review_comments": request.form.get("review_comments"),
            "created_by": review["created_by"],
            "created_date": review["created_date"]
        }

        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for('get_game_detail', game_id=game_id))

    return render_template("edit_review.html",
                           game=game,
                           review=review)


@app.route("/delete_review/<game_id>/<review_id>")
def delete_review(game_id, review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for('get_game_detail', game_id=game_id))


# add/edit/delete game functions
@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        if session["user"] == "admin":
            game = {
                "name": request.form.get("name"),
                "description": request.form.get("description"),
                "image": request.form.get("image"),
                "publisher": request.form.get("publisher"),
                "type": request.form.get("type"),
                "min_player": request.form.get("min_player"),
                "max_player": request.form.get("max_player"),
                "age": request.form.get("age"),
                "playing_time": request.form.get("playing_time"),
                "mechanisms": request.form.getlist("mechanisms"),
                "themes": request.form.getlist("themes")
                }
        else:
            game = {
                "name": request.form.get("name"),
                "description": request.form.get("description"),
                "image": "",
                "publisher": request.form.get("publisher"),
                "type": request.form.get("type"),
                "min_player": request.form.get("min_player"),
                "max_player": request.form.get("max_player"),
                "age": request.form.get("age"),
                "playing_time": request.form.get("playing_time"),
                "mechanisms": request.form.getlist("mechanisms"),
                "themes": request.form.getlist("themes")
                }

        mongo.db.games.insert_one(game)
        flash("Game Successfully Added")
        return redirect(url_for("get_games"))

    mechanisms = mongo.db.tags.find({"use": "mechanisms"}).sort("name", 1)
    themes = mongo.db.tags.find({"use": "themes"}).sort("name", 1)
    return render_template("add_game.html",
                           mechanisms=mechanisms,
                           themes=themes)


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):

    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "image": request.form.get("image"),
            "publisher": request.form.get("publisher"),
            "type": request.form.get("type"),
            "min_player": request.form.get("min_player"),
            "max_player": request.form.get("max_player"),
            "age": request.form.get("age"),
            "playing_time": request.form.get("playing_time"),
            "mechanisms": request.form.getlist("mechanisms"),
            "themes": request.form.getlist("themes")
            }

        mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
        flash("Game Succesfully Updated")
        return redirect(url_for("get_games"))

    username = session["user"]
    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    mechanisms = list(mongo.db.tags.find(
                                        {"use": "mechanisms"}).sort("name", 1))
    themes = list(mongo.db.tags.find({"use": "themes"}).sort("name", 1))

    # iterate through list of all mechanisms,
    # set selected if in game's mechanism list
    for mech in mechanisms:
        if mech["name"] in game["mechanisms"]:
            mech["selected"] = True

    # iterate through list of all themes,
    # set selected if in game's themes list
    for theme in themes:
        if theme["name"] in game["themes"]:
            theme["selected"] = True

    return render_template("edit_game.html", game=game,
                           mechanisms=mechanisms,
                           themes=themes,
                           username=username)


@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("get_games"))


# tag list and add/edit/delete tag functions
@app.route("/tag_list")
def tag_list():
    mechanisms = mongo.db.tags.find({"use": "mechanisms"})
    themes = mongo.db.tags.find({"use": "themes"})
    return render_template("tags.html",
                           mechanisms=mechanisms,
                           themes=themes)


@app.route("/add_tag", methods=["GET", "POST"])
def add_tag():
    if request.method == "POST":
        tag = {
            "name": request.form.get("name"),
            "use": request.form.get("use"),
            "description": request.form.get("description")
            }

        mongo.db.tags.insert_one(tag)
        flash("Tag Successfully Added")
        return redirect(url_for("tag_list"))

    mechanisms = mongo.db.tags.find({"use": "mechanisms"})
    themes = mongo.db.tags.find({"use": "themes"})
    return render_template("add_tag.html",
                           mechanisms=mechanisms,
                           themes=themes)


@app.route("/edit_tag/<tag_id>", methods=["GET", "POST"])
def edit_tag(tag_id):
    tag = mongo.db.tags.find_one({"_id": ObjectId(tag_id)})

    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "use": request.form.get("use"),
            "description": request.form.get("description")
        }

        mongo.db.tags.update({"_id": ObjectId(tag_id)}, submit)
        flash("Tag Successfully Updated")
        return redirect(url_for('tag_list'))

    return render_template("edit_tag.html", tag=tag)


@app.route("/delete_tag/<tag_id>")
def delete_tag(tag_id):
    mongo.db.tags.remove({"_id": ObjectId(tag_id)})
    flash("Tag Successfully Deleted")
    return redirect(url_for("tag_list"))


# register an account
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "my_collection": [],
            "my_wishlist": []
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for(
            "profile", username=session["user"]))

    return render_template("register.html")


# log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile",
                                        username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # grab the session user's profile from db...
    profile = mongo.db.users.find_one({"username": session["user"]})
    # ...and immediately drop password from result object for security
    del profile["password"]

    # finds all games with no explicit image
    # (the 'coming soon' image) for admin profile
    games = mongo.db.games.find({"image": ""})

    if session["user"]:
        return render_template("profile.html",
                               username=profile["username"],
                               collection=profile["my_collection"],
                               wishlist=profile["my_wishlist"],
                               games=games)

    return redirect(url_for("login"))


# generic functions for collection and wishlist actions to call on
def add_to_list(list_name, game_id):
    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})

    details = {
        "id": game["_id"],
        "image": game["image"],
        "name": game["name"],
        "date_added": TODAY
        }

    mongo.db.users.update_one({"username": session["user"]},
                              {"$push": {list_name: details}})


def remove_from_list(list_name, game_id):
    mongo.db.users.update_many({"username": session["user"]},
                               {"$pull": {list_name:
                                {"id": ObjectId(game_id)}}})


@app.route("/add_to_collection/<game_id>")
def add_to_collection(game_id):
    add_to_list("my_collection", game_id)
    flash("Game successfully added to your collection")
    return redirect(url_for("get_games"))


@app.route("/remove_from_collection/<game_id>")
def remove_from_collection(game_id):
    remove_from_list("my_collection", game_id)
    return redirect(url_for('profile', username=session['user']))


@app.route("/add_to_wishlist/<game_id>")
def add_to_wishlist(game_id):
    add_to_list("my_wishlist", game_id)
    flash("Game successfully added to your wishlist")
    return redirect(url_for("get_games"))


@app.route("/remove_from_wishlist/<game_id>")
def remove_from_wishlist(game_id):
    remove_from_list("my_wishlist", game_id)
    return redirect(url_for('profile', username=session['user']))


@app.route("/move_to_collection/<game_id>")
def move_to_collection(game_id):
    add_to_list("my_collection", game_id)
    remove_from_list("my_wishlist", game_id)
    flash("Game successfully moved to your collection")

    return redirect(url_for('profile', username=session['user']))


# log out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
