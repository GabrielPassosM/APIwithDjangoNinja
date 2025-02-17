from uuid import UUID

from ninja import Schema


class PlayerSchema(Schema):
    id: int | UUID
    name: str
    shirt_number: int
    position: str  # PlayerPosition
    image_url: str | None = None
    goals: int
    assists: int
    mvps: int
    yellow_cards: int
    red_cards: int