from src.domain import User
from src.repository import UserRepository
from sqlalchemy.exc import SQLAlchemyError
from src.dto import user_request_dto as UserRequestDto

import logging

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, payload:UserRequestDto):

        new_user = User(
            name=payload.name,
            username=payload.username,
            email=payload.email,
            phone=payload.phone,
            website=payload.website,
            address=payload.address,
            company=payload.company
        )
        try:
            self.user_repository.create(new_user)
            return new_user.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating user: {e}")
            return {"error": "Database error occurred."}
    def get_all_users(self):
        try:
            users = self.user_repository.get_all()
            return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting all users: {e}")
            return {"error": "Database error occurred."}
        
    def get_user_by_id(self, user_id):
        try:
            user = self.user_repository.get_by_id(user_id)
            if user:
                return user.to_dict()
            return {"error": "User not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting user by id: {e}")
            return {"error": "Database error occurred."}

