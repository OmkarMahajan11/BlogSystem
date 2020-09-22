from flask import Blueprint
from flask import request
import json
from ..services import add_blog, delete_blog, update_blog, list_blogs, searchByUser

blog = Blueprint("blog", __name__)

@blog.route("/create", methods=["POST"])
def create():
    res = add_blog(request.json["name"], request.json["description"], request.json["content"], request.json["user_id"])
    return json.dumps({"result":res})

@blog.route("/delete", methods = ['DELETE'])
def remove():
    result =  delete_blog(request.json['blog_id'],request.json["author_id"])
    return json.dumps({"result": result})

@blog.route("/update", methods = ['POST'])
def update():
    result = update_blog(request.json['blog_id'], request.json['user_id'], request.json['content'])
    return json.dumps({"result": result})

@blog.route("/list", methods=["GET"])
def list():
    result = list_blogs()
    return {"result":result}

@blog.route("/searchbyuser/<username>")
def listbyuser(username):
    result = searchByUser(username)
    return {"result":result}