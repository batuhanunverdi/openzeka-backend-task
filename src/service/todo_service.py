from src.dto.todo_request_dto import TodoRequestDto
from src.service.user_service import UserService
from src.repository.todo_repository import TodoRepository
from src.domain.todo import Todo
from sqlalchemy.exc import SQLAlchemyError
import logging

class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()
        self.user_service = UserService()

    def create_todo(self, payload:TodoRequestDto):
        try:
            user = self.user_service.get_user_by_id(payload.userId)
            if isinstance(user, dict) and "error" in user:
                return user
            new_todo = Todo(
                title=payload.title,
                completed=payload.completed,
                userId=payload.userId
            )
            self.todo_repository.create(new_todo)
            return new_todo.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating todo: {e}")
            return {"error": "Database error occurred."}
    
    def get_all_todos(self):
        try:
            todos = self.todo_repository.get_all()
            return [todo.to_dict() for todo in todos]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting todos: {e}")
            return {"error": "Database error occurred."}
    
    def get_todo_by_id(self, todo_id):
        try:
            todo = self.todo_repository.get_by_id(todo_id)
            if todo:
                return todo.to_dict()
            return {"error": "Todo not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting todo by id: {e}")
            return {"error": "Database error occurred."}
    def get_todos_by_user_id(self, user_id):
        try:
            todos = self.todo_repository.get_by_user_id(user_id)
            return [todo.to_dict() for todo in todos]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting todos by user id: {e}")
            return {"error": "Database error occurred."}