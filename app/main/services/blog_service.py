import datetime
from ..models import blogToCatModel, BlogModel, CategoryModel
from .. import db

def add_blog(name, description, content, author_id, categories):
    try:
        blog = BlogModel(name=name, description=description, content=content, author_id=author_id, created_at=datetime.datetime.now())
        db.session.add(blog)
        db.session.commit()

        invalid_categories = []
        blog_id = BlogModel.query.filter_by(name=name, author_id=author_id)
        for cat in categories:
            cat_id = CategoryModel.query.filter_by(category=cat)
            if not cat_id:
                invalid_categories.append(cat)
                continue
            addtocat = blogToCatModel(blog_id=blog_id, cat_id=cat_id)
            db.session.add(addtocat)
            db.session.commit()
        if not invalid_categories:    
            return "blog added"
        else:
            return f"blog added, invalid categories: {invalid_categories}"    
    except Exception as e:
        return str(e)