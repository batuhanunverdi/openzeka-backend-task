from src.dto.album_request_dto import AlbumRequestDto
from src.service.user_service import UserService
from src.repository.album_repository import AlbumRepository
from src.domain.album import Album
from sqlalchemy.exc import SQLAlchemyError
import logging

class AlbumService:
    def __init__(self):
        self.album_repository = AlbumRepository()
        self.user_service = UserService()

    def create_album(self, payload:AlbumRequestDto):
        try:
            user = self.user_service.get_user_by_id(payload.userId)
            if isinstance(user, dict) and "error" in user:
                return user
            new_album = Album(
                title=payload.title,
                userId=payload.userId
            )
            self.album_repository.create(new_album)
            return new_album.to_dict()
        except SQLAlchemyError as e:
            logging.error(f"Error in creating Album: {e}")
            return {"error": "Database error occurred."}
    
    def get_all_albums(self):
        try:
            Albums = self.album_repository.get_all()
            return [Album.to_dict() for Album in Albums]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Albums: {e}")
            return {"error": "Database error occurred."}
    
    def get_album_by_id(self, Album_id):
        try:
            Album = self.album_repository.get_by_id(Album_id)
            if Album:
                return Album.to_dict()
            return {"error": "Album not found."}
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Album by id: {e}")
            return {"error": "Database error occurred."}
        

    def get_albums_by_user_id(self, user_id):
        try:
            albums = self.album_repository.get_by_user_id(user_id)
            return [album.to_dict() for album in albums]
        except SQLAlchemyError as e:
            logging.error(f"Error in getting Albums by user id: {e}")
            return {"error": "Database error occurred."}