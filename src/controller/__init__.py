from .user_controller import user_controller
from .todo_controller import todo_controller
from .post_controller import post_controller
from .album_controller import album_controller
from .comment_controller import comment_controller
from .photo_controller import photo_controller

controllers = {
    "user": user_controller,
    "todo": todo_controller,
    "post": post_controller,
    "album": album_controller,
    "comment": comment_controller,
    "photo": photo_controller
}

def register_blueprints(app):
    for name, blueprint in controllers.items():
        app.register_blueprint(blueprint)
    return app
