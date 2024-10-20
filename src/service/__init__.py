from .user_service import UserService
from .todo_service import TodoService
from .post_service import PostService
from .album_service import AlbumService
from .comment_service import CommentService
from .photo_service import PhotoService

services = {
    "user": UserService(),
    "todo": TodoService(),
    "post": PostService(),
    "album": AlbumService(),
    "comment": CommentService(),
    "photo": PhotoService(),
}

def register_services(app):
    for name, service in services.items():
        setattr(app, f"{name}_service", service)
    return app
