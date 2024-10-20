from config import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(50), nullable=False)
    address = db.Column(db.JSON, nullable=False)
    company = db.Column(db.JSON, nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)
    posts = db.relationship('Post', backref='user', lazy=True)
    albums = db.relationship('Album', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "website": self.website,
            "address": self.address,
            "company": self.company
        }