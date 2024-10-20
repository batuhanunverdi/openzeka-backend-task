from dataclasses import dataclass

@dataclass
class CommentRequestDto:
    postId: int
    name: str
    email: str
    body: str