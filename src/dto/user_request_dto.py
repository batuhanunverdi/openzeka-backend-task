from dataclasses import dataclass

@dataclass
class UserRequestDto:
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict