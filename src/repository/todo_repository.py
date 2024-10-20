from config import db
from src.domain.todo import Todo

class TodoRepository:
    @staticmethod
    def create(todo):
        db.session.add(todo)
        db.session.commit()

    @staticmethod
    def get_by_id(todo_id):
        return Todo.query.get(todo_id)

    @staticmethod
    def get_all():
        return Todo.query.all()
    
    @staticmethod
    def get_by_user_id(user_id):
        return Todo.query.filter_by(userId=user_id).all()
