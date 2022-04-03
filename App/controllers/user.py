from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError



def get_all_users():
    return User.query.all()

def create_user(username, email, password):
    newuser = User(username=username, email=email,password=password)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 'email or username already in use'
    return 'user created'
    




def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()