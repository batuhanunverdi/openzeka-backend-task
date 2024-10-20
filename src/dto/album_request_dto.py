from dataclasses import dataclass

@dataclass
class AlbumRequestDto:
    userId: int
    title: str
   