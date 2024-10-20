from config import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    postId = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'body': self.body,
            'postId': self.postId
        }