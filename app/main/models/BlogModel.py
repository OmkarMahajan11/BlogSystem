from ..import db
from .import UserModel

class BlogModel(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete = 'CASCADE'), primary_key=True)
    created_at = db.Column(db.DateTime)
    db.UniqueConstraint("name", "author_id")

class CategoryModel(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    category = db.Column(db.String(50))

class blogToCatModel(db.Model):
    __tablename__ = "blogToCatMap"
    blog_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, primary_key=True)
    db.UniqueConstraint("blog_id", "cat_id")