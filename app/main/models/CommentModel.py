from ..import db
from .import UserModel
from .import BlogModel

class CommentModel(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.integer, primary_key=True)
    comment = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))    
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id', ondelete = "CASCADE"))

class CommentTree(db.Model):
    __tablename__ = "commentsTree"
    ancestor = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete="CASCADE"))
    descendant = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete="CASCADE"))
    length = db.Column(db.Integer, nullable=False)