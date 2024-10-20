from src.dto.post_request_dto import PostRequestDto
from src.service.user_service import UserService
from src.repository.post_repository import PostRepository
from src.domain.post import Post
from sqlalchemy.exc import SQLAlchemyError
import logging

class PostService:
    def __init__(self):
        self.post_repository = PostRepository()
        self.user_service = UserService()

    def create_post(self, payload:PostRequestDto):
        try:
            user = self.user_service.get_user_by_id(payload.userId)
            if isinstance(user, dict) and "error" in user:
                return user
            new_post = Post(
                title=payload.title,
                body=payload.body,
                userId=payload.userId
            )
            self.post_repository.create(new_post)
            return new_post.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating post: {e}")
            return {"error": "Database error occurred."}
    
    def get_all_posts(self):
        try:
            posts = self.post_repository.get_all()
            return [post.to_dict() for post in posts]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting posts: {e}")
            return {"error": "Database error occurred."}
    
    def get_post_by_id(self, post_id):
        try:
            post = self.post_repository.get_by_id(post_id)
            if post:
                return post.to_dict()
            return {"error": "Post not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting post by id: {e}")
            return {"error": "Database error occurred."}
        

    def get_posts_by_user_id(self, user_id):
        try:
            posts = self.post_repository.get_by_user_id(user_id)
            return [post.to_dict() for post in posts]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting posts by user id: {e}")
            return {"error": "Database error occurred."}