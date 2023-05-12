from dataclasses import dataclass


@dataclass
class Website:
    website: str
    popularity: int
    frontend: str
    backend: str
