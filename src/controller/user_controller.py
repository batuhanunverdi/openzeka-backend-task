from src.dto.user_request_dto import UserRequestDto
from src.validator.user_request_dto_schema import UserRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

user_controller = Blueprint('user_controller', __name__, url_prefix='/api/users')

@user_controller.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user_request_dto_schema = UserRequestDtoSchema()
        validated_data = user_request_dto_schema.load(data)
        user_request_dto = UserRequestDto(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            address=validated_data['address'],  
            phone=validated_data['phone'],
            website=validated_data['website'],
            company=validated_data['company']
        )
        user_service = current_app.user_service
        response_data,status_code = user_service.create_user(user_request_dto),201
        print(response_data)
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@user_controller.route('/', methods=['GET'])
def get_all_users():
    try:
        user_service = current_app.user_service
        response_data,status_code =  user_service.get_all_users(),200
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@user_controller.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user_service = current_app.user_service
        response_data, status_code = user_service.get_user_by_id(user_id),200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)
