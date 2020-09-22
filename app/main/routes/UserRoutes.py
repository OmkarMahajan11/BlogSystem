from flask import Blueprint
from flask import request
from ..services import *
import json

user = Blueprint("user", __name__)

@user.route("/register", methods=["POST"])
def register():
    res = add_user(request.json["name"], request.json["email"], request.json["password"])
    return json.dumps({"message":res})

@user.route("/login", methods=["GET"])
def login():
    res = user_login(request.json["email"], request.json["password"])
    return json.dumps({"message":str(res)})

@user.route("/usersearch/<username>", methods=["GET"])
def search(username):
    res = search_user(username)
    return json.dumps({"result":res})    