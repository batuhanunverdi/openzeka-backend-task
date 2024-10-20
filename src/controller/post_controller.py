from src.dto.post_request_dto import PostRequestDto
from src.validator.post_request_dto_schema import PostRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

post_controller = Blueprint('post_controller', __name__, url_prefix='/api/posts')

@post_controller.route('/', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        post_request_dto_schema = PostRequestDtoSchema()
        validated_data = post_request_dto_schema.load(data)
        post_request_dto = PostRequestDto(
            user_id = validated_data['user_id'],
            title = validated_data['title'],
            content = validated_data['content']
        )
        post_service = current_app.post_service
        response_data,status_code = post_service.create_post(post_request_dto),201
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@post_controller.route('/', methods=['GET'])
def get_all_posts():
    try:
        post_service = current_app.post_service
        response_data,status_code =  post_service.get_all_posts(),200
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)


@post_controller.route('/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    try:
        post_service = current_app.post_service
        response_data, status_code = post_service.get_post_by_id(post_id),200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)


@post_controller.route('/user/<int:user_id>', methods=['GET'])
def get_posts_by_user_id(user_id):
    try:
        post_service = current_app.post_service
        response_data, status_code = post_service.get_posts_by_user_id(user_id), 200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

