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