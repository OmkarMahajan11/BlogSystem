from flask import Blueprint
from flask import request
import json
from ..services import add_blog

blog = Blueprint("blog", __name__)

@blog.route("/create", methods=["POST"])
def create():
    res = add_blog(request.json["name"], request.json["description"], request.json["content"], request.json["user_id"], request.json["categories"])
    return json.dumps({"result":res})