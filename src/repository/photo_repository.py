from config import db
from src.domain.photo import Photo

class PhotoRepository:
    @staticmethod
    def create(photo):
        db.session.add(photo)
        db.session.commit()

    @staticmethod
    def get_by_id(photo_id):
        return Photo.query.get(photo_id)

    @staticmethod
    def get_all():
        return Photo.query.all()

    @staticmethod
    def get_by_album_id(album_id):
        return Photo.query.filter_by(albumId=album_id).all()
