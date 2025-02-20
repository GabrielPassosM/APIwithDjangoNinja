from enum import Enum
from uuid import uuid4

from django.db import models


class PlayerPosition(Enum):
    GOALKEEPER = "goalkeeper"
    DEFENDER = "defender"
    MIDFIELDER = "midfielder"
    FORWARD = "forward"


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    shirt_number = models.IntegerField(default=0)
    position = models.CharField(
        max_length=50,
        choices=[(position.value, position.name) for position in PlayerPosition],
    )
    image_url = models.CharField(max_length=500, null=True, blank=True, default=None)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    mvps = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    class Meta:
        db_table = "player"

    def __str__(self):
        return f"{self.name} - {self.shirt_number}"
