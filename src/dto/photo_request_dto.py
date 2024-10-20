
from dataclasses import dataclass


@dataclass
class PhotoRequestDto:
    title: str
    url: str
    thumbnailUrl: str
    albumId: int