from config import db

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    thumbnailUrl = db.Column(db.String(500), nullable=False)
    albumId = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'thumbnailUrl': self.thumbnailUrl,
            'albumId': self.albumId
        }