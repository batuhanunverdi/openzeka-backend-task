from config import db
from src.domain.post import Post

class PostRepository:
    @staticmethod
    def create(post):
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def get_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def get_all():
        return Post.query.all()

    @staticmethod
    def get_by_user_id(user_id):
        return Post.query.filter_by(userId=user_id).all()