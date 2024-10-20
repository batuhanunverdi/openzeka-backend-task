from src.dto.album_request_dto import AlbumRequestDto
from src.validator.album_request_dto_schema import AlbumRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

album_controller = Blueprint('album_controller', __name__, url_prefix='/api/albums')

@album_controller.route('/', methods=['POST'])
def create_album():
    try:
        data = request.get_json()
        album_request_dto_schema = AlbumRequestDtoSchema()
        validated_data = album_request_dto_schema.load(data)
        album_request_dto = AlbumRequestDto(
            user_id = validated_data['user_id'],
            title = validated_data['title']
        )
        album_service = current_app.album_service
        response_data,status_code = album_service.create_album(album_request_dto),201
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@album_controller.route('/', methods=['GET'])
def get_all_albums():
    try:
        album_service = current_app.album_service
        response_data,status_code =  album_service.get_all_albums(),200
        return make_response(jsonify(response_data),status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@album_controller.route('/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    try:
        album_service = current_app.album_service
        response_data, status_code = album_service.get_album_by_id(album_id),200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)

@album_controller.route('/user/<int:user_id>', methods=['GET'])
def get_albums_by_user_id(user_id):
    try:
        album_service = current_app.album_service
        response_data, status_code = album_service.get_albums_by_user_id(user_id), 200
        return make_response(jsonify(response_data), status_code)
    except Exception as e:
        return make_response(jsonify(str(e)),400)
