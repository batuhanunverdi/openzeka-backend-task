from config import db
from src.domain.album import Album

class AlbumRepository:
    @staticmethod
    def create(album):
        db.session.add(album)
        db.session.commit()

    @staticmethod
    def get_by_id(album_id):
        return Album.query.get(album_id)

    @staticmethod
    def get_all():
        return Album.query.all()
    
    @staticmethod
    def get_by_user_id(user_id):
        return Album.query.filter_by(userId=user_id).all()

