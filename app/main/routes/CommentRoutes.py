from flask import Blueprint
from flask import request
import json

from ..models import BlogModel, UserModel
from ..services import add_comment, delete_comment, searchByUser, searchByBlog

comment = Blueprint("comment", __name__)

@comment.route("/add", methods=["POST"])
def addComment():
    res = add_comment(request.json["user_id"], request.json["blog_id"], request.json["parent_id"], request.json["comment"])
    return {"result":res}

@comment.route("/delete", methods=["DELETE"])
def del_comment():
    res = delete_comment(request.json["comment_id"], request.json["user_id"])
    return {"result":res}

@comment.route("/byblog/<blog_id>")
def byblog(blog_id):
    res = searchByBlog(blog_id)
    return {"result":res}

@comment.route("/byuser/<username>")
def byuser(username):
    res = searchByUser(username)
    return {"result":res}

