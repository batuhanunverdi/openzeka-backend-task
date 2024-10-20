from src.dto.photo_request_dto import PhotoRequestDto
from src.validator.photo_request_dto_schema import PhotoRequestDtoSchema
from flask import Blueprint, request,current_app,make_response,jsonify

photo_controller = Blueprint('photo_controller', __name__, url_prefix='/api/photos')

@photo_controller.route('/', methods=['POST'])
def create_photo():
    data = request.get_json()
    photo_request_dto_schema = PhotoRequestDtoSchema()
    validated_data = photo_request_dto_schema.load(data)
    photo_request_dto = PhotoRequestDto(
        album_id = validated_data['album_id'],
        title = validated_data['title'],
        url = validated_data['url'],
        thumbnail_url = validated_data['thumbnail_url']
    )
    photo_service = current_app.photo_service
    response_data,status_code = photo_service.create_photo(photo_request_dto),201
    return make_response(jsonify(response_data),status_code)

@photo_controller.route('/', methods=['GET'])
def get_all_photos():
    photo_service = current_app.photo_service
    response_data,status_code =  photo_service.get_all_photos(),200
    return make_response(jsonify(response_data),status_code)

@photo_controller.route('/<int:photo_id>', methods=['GET'])
def get_photo_by_id(photo_id):
    photo_service = current_app.photo_service
    response_data, status_code = photo_service.get_photo_by_id(photo_id),200
    return make_response(jsonify(response_data), status_code)

@photo_controller.route('/album/<int:album_id>', methods=['GET'])
def get_photos_by_album_id(album_id):
    photo_service = current_app.photo_service
    response_data, status_code = photo_service.get_photos_by_album_id(album_id), 200
    return make_response(jsonify(response_data), status_code)
