from src.dto.todo_request_dto import TodoRequestDto
from src.validator.todo_request_dto_schema import TodoRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

todo_controller = Blueprint('todo_controller', __name__, url_prefix='/api/todos')

@todo_controller.route('/', methods=['POST'])
def create_todo():
    try:
        data = request.get_json()
        todo_request_dto_schema = TodoRequestDtoSchema()
        validated_data = todo_request_dto_schema.load(data)
        todo_request_dto = TodoRequestDto(
            title=validated_data['title'],
            completed=validated_data['completed'],
            userId=validated_data['userId']
        )
        todo_service = current_app.todo_service
        response_data,status_code = todo_service.create_todo(todo_request_dto),201
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@todo_controller.route('/', methods=['GET'])
def get_all_todos():
    try:
        todo_service = current_app.todo_service
        response_data,status_code =  todo_service.get_all_todos(),200
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@todo_controller.route('/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    try:
        todo_service = current_app.todo_service
        response_data, status_code = todo_service.get_todo_by_id(todo_id),200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)


@todo_controller.route('/user/<int:user_id>', methods=['GET'])
def get_todos_by_user_id(user_id):
    try:
        todo_service = current_app.todo_service
        response_data, status_code = todo_service.get_todos_by_user_id(user_id), 200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)
