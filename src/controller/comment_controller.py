from src.dto.comment_request_dto import CommentRequestDto
from src.validator.comment_request_dto_schema import CommentRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

comment_controller = Blueprint('comment_controller', __name__, url_prefix='/api/comments')

@comment_controller.route('/', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment_request_dto_schema = CommentRequestDtoSchema()
    validated_data = comment_request_dto_schema.load(data)
    comment_request_dto = CommentRequestDto(
        name= validated_data['name'],
        email= validated_data['email'],
        body= validated_data['body'],
        postId= validated_data['postId']
    )
    comment_service = current_app.comment_service
    response_data,status_code = comment_service.create_comment(comment_request_dto),201
    return make_response(jsonify(response_data),status_code)

@comment_controller.route('/', methods=['GET'])
def get_all_comments():
    comment_service = current_app.comment_service
    response_data,status_code =  comment_service.get_all_comments(),200
    return make_response(jsonify(response_data),status_code)

@comment_controller.route('/<int:comment_id>', methods=['GET'])
def get_comment_by_id(comment_id):
    comment_service = current_app.comment_service
    response_data, status_code = comment_service.get_comment_by_id(comment_id),200
    return make_response(jsonify(response_data), status_code)

@comment_controller.route('/post/<int:post_id>', methods=['GET'])
def get_comments_by_post_id(post_id):
    comment_service = current_app.comment_service
    response_data, status_code = comment_service.get_comments_by_post_id(post_id), 200
    return make_response(jsonify(response_data), status_code)
