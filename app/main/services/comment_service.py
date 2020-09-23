from ..models import BlogModel, UserModel, CommentModel, CommentTree
from .. import db

def add_comment(user_id, blog_id, parent_id, comment):
    try:
        ls = set()
        cmt_list = CommentModel.query.all()
        for each in cmt_list:
            ls.add(each.id)

        new_comment = CommentModel(comment=comment, blog_id=blog_id, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()

        new_list = CommentModel.query.filter_by(user_id=user_id, blog_id=blog_id).all()
        new_id = None
        for each in new_list:
            if each.id not in ls:
                new_id = each.id
                break

        if not parent_id: # means it is not a reply to existing comment, but a new comment
            newToTree = CommentTree(ancestor=new_id, descendant=new_id, length=0)
            db.session.add(newToTree)
            db.session.commit()
            db.session.close()
            return "comment added"
        else:
            cmt_tree = CommentTree.query.filter_by(descendant=parent_id).all()
            for each in cmt_tree:
                ct = CommentTree(ancestor=each.ancestor, descendant=new_id, length=each.length+1)
                db.session.add(ct)
                db.session.commit()
            newToTree = CommentTree(ancestor=new_id, descendant=new_id, length=0)
            db.session.add(newToTree)
            db.session.commit()
            db.session.close()    
            return "comment added"
    except Exception as e:
        return str(e)            

def delete_comment(comment_id, user_id):
    comment = CommentModel.query.filter_by(id=comment_id).first()
    if user_id == comment.user_id:
        comm_desc = CommentTree.query.filter_by(ancestor=comment.id).all()
        
        for each in comm_desc:
            comm = CommentModel.query.filter_by(id=each.descendant).first()
            db.session.delete(comm)
            db.session.commit()
        return True
    else:
        return "user can not delete"

def searchByUser(user_id):
    try:
        ls = []
        comments = CommentModel.query.filter_by(user_id=user_id).all()
        for c in comments:
            row = {}
            row["id"] = c.id
            row["comment"] = c.comment
            row["user_id"] = c.user_id
            ls.append(row)
        return ls
    except Exception as e:
        return str(e)        

def searchByBlog(blog_id):
    try:
        #load only main comments
        l = []
        comments = CommentModel.query.filter_by(blog_id=blog_id).all()
        for each in comments:
            lev1 = CommentTree.query.filter_by(descendant=each.id, length=1).count()
            if lev1 == 0:
                row = {}
                row["id"] = each.id
                row["comment"] = each.comment
                row["author_id"] = each.user_id
                row["blog_id"] = each.blog_id
                l.append(row)
        return l        
    except Exception as e:
        return str(e)    