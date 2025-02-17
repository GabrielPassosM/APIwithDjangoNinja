from ninja import Schema

from players.models import PlayerPosition


class PlayerSchema(Schema):
    id: int
    name: str
    shirt_number: int
    position: PlayerPosition
    image_url: str | None = None
    goals: int
    assists: int
    mvps: int
    yellow_cards: int
    red_cards: int