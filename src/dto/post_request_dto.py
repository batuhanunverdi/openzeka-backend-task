from dataclasses import dataclass

@dataclass
class PostRequestDto:
    userId: int
    title: str
    body: str
   