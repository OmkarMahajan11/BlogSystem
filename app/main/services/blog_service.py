import datetime
from ..models import BlogModel, UserModel
from .. import db

def add_blog(name, description, content, author_id):
    try:
        blog = BlogModel(name=name, description=description, content=content, author_id=author_id, created_at=datetime.datetime.now())
        db.session.add(blog)
        db.session.commit()
        return "blog added"
    except Exception as e:
        return str(e)

def delete_blog(blog_id, user_id):
    blog = BlogModel.query.filter_by(id=blog_id).first()
    if not blog:
        return "no such blog"
    if blog.author_id != user_id:
        return "access denied"
    db.session.delete(blog)
    db.session.commit()
    return "blog deleted"        

def update_blog(blog_id, user_id, content):
    blog = BlogModel.query.filter_by(id=blog_id).first()
    if not blog:
        return "no such blog"
    if blog.author_id != user_id:
        return "access denied"
    blog.content=content
    db.session.commit()
    return "blog updated"    

def list_blogs():
    try:
        ls = []
        for blog in BlogModel.query.all():
            row = {}
            row["id"] = blog.id
            row["name"] = blog.name
            row["description"] = blog.description
            row["author"] = UserModel.query.filter_by(id=blog.author_id).first().id
            ls.append(row)
        return {"data":ls}
    except Exception as e:
        return str(e)                 

def searchByUser(username):
    try:
        user = UserModel.query.filter_by(name=username).first()
        if not user:
            return "no such author"
        ls = []
        blogs = BlogModel.query.filter_by(author_id=user.id).all()
        if not blogs:
            return "author has no blogs"
        for blog in blogs:
            row = {}
            row["name"] = blog.name
            row["description"] = blog.description
            row["author"] = user.name
            row["date"] = blog.created_at
            ls.append(row)
        return {"data":ls}    
    except Exception as e:
        return str(e)