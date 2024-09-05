from ..model.user import User
from .. import db

def get_all_users():
    """Retrieve all users from the database"""
    return User.query.all()

def create_user(username, email):
    """Create a new user in the database"""
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
