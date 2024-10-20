from config import db
from src.domain.comment import Comment

class CommentRepository:
    @staticmethod
    def create(comment):
        db.session.add(comment)
        db.session.commit()

    @staticmethod
    def get_by_id(comment_id):
        return Comment.query.get(comment_id)

    @staticmethod
    def get_all():
        return Comment.query.all()

    @staticmethod
    def get_by_post_id(post_id):
        return Comment.query.filter_by(postId=post_id).all()