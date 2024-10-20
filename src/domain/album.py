from config import db

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photos = db.relationship('Photo', backref='album', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'userId': self.userId,
        }