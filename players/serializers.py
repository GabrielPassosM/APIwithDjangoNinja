from typing import Final
from uuid import UUID

from ninja import Schema
from pydantic import field_validator

from players.models import PlayerPosition

DEFAULT_IMAGE_URL: Final = (
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKu1w7TulWMUKGszjJlb7PDtn0LVSJgGnrog&s"
)


class _PlayerStats(Schema):
    goals: int = 0
    assists: int = 0
    mvps: int = 0
    yellow_cards: int = 0
    red_cards: int = 0


class _PlayerBase(_PlayerStats):
    name: str
    shirt_number: int
    position: str  # PlayerPosition
    image_url: str | None = DEFAULT_IMAGE_URL


class PlayerCreate(_PlayerBase):
    @field_validator("position", mode="before")
    @classmethod
    def validate_position(cls, value):
        value = value.lower()
        try:
            PlayerPosition(value)
        except ValueError as e:
            raise e
        return value


class PlayerResponse(_PlayerBase):
    id: UUID


class PlayerIncrementStats(_PlayerStats):
    pass
