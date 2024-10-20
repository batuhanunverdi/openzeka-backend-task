from src.dto.comment_request_dto import CommentRequestDto
from src.service.post_service import PostService
from src.repository.comment_repository import CommentRepository
from src.domain.comment import Comment
from sqlalchemy.exc import SQLAlchemyError
import logging

class CommentService:
    def __init__(self):
        self.comment_repository = CommentRepository()
        self.post_service = PostService()

    def create_comment(self, payload:CommentRequestDto):
        try:
            post = self.post_service.get_post_by_id(payload.postId)
            if isinstance(post, dict) and "error" in post:
                return post
            new_comment = Comment(
                postId=payload.postId,
                name=payload.name,
                email=payload.email,
                body=payload.body
            )
            self.comment_repository.create(new_comment)
            return new_comment.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating Comment: {e}")
            return {"error": "Database error occurred."}
    
    def get_all_comments(self):
        try:
            comments = self.comment_repository.get_all()
            return [comment.to_dict() for comment in comments]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting comments: {e}")
            return {"error": "Database error occurred."}
    
    def get_comment_by_id(self, comment_id):
        try:
            comment = self.comment_repository.get_by_id(comment_id)
            if comment:
                return comment.to_dict()
            return {"error": "Comment not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting comment by id: {e}")
            return {"error": "Database error occurred."}
        

    def get_comments_by_post_id(self, post_id):
        try:
            post = self.post_service.get_post_by_id(post_id)
            if isinstance(post, dict) and "error" in post:
                return post
            comments = self.comment_repository.get_by_post_id(post_id)
            return [comment.to_dict() for comment in comments]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Comments by post id: {e}")
            return {"error": "Database error occurred."}