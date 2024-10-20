from config import db
from src.domain.user import User

class UserRepository:
    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all():
        return User.query.all()

