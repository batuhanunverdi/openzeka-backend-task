from dataclasses import dataclass

@dataclass
class TodoRequestDto:
    title: str
    completed: bool
    userId: int