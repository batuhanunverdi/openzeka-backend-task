from src.dto.photo_request_dto import PhotoRequestDto
from src.service.album_service import AlbumService
from src.repository.photo_repository import PhotoRepository
from src.domain.photo import Photo
from sqlalchemy.exc import SQLAlchemyError
import logging

class PhotoService:
    def __init__(self):
        self.photo_repository = PhotoRepository()
        self.album_service = AlbumService()

    def create_photo(self, payload:PhotoRequestDto):
        try:
            album = self.album_service.get_album_by_id(payload.albumId)
            if isinstance(album, dict) and "error" in album:
                return album
            new_photo = Photo(
                title=payload.title,
                url=payload.url,
                thumbnailUrl=payload.thumbnailUrl,
                albumId=payload.albumId,
            )
            self.photo_repository.create(new_photo)
            return new_photo.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating Photo: {e}")
            return {"error": "Database error occurred."}
    
    def get_all_photos(self):
        try:
            photos = self.photo_repository.get_all()
            return [photo.to_dict() for photo in photos]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Photos: {e}")
            return {"error": "Database error occurred."}
    
    def get_photo_by_id(self, photo_id):
        try:
            photo = self.photo_repository.get_by_id(photo_id)
            if photo:
                return photo.to_dict()
            return {"error": "Photo not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Photo by id: {e}")
            return {"error": "Database error occurred."}
        

    def get_photos_by_album_id(self, album_id):
        try:     
            album = self.album_service.get_album_by_id(album_id)
            if isinstance(album, dict) and "error" in album:
                return album
            photos = self.photo_repository.get_by_album_id(album_id)
            return [photo.to_dict() for photo in photos]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Photos by album id: {e}")
            return {"error": "Database error occurred."}