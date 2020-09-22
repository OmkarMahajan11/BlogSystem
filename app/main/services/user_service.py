from ..models import UserModel
from ..import db

def add_user(name, email, password):
    try:
        user = UserModel(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return "user added"
    except Exception as e:
        return str(e)

def user_login(email, password):
    try:
        user = UserModel.query.filter_by(email=email)
        if not user:
            return "no such user"
        elif user.password == password:
            return "login successful"
        else:
            return "invalid credentials"        
    except Exception as e:
        return str(e)    

def search_user(name):
    return