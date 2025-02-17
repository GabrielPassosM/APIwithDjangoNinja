from ninja import Router

from players.models import Player
from players.serializers import PlayerSchema

router = Router()


@router.get("/", response=list[PlayerSchema])
def get_players(request):
    return Player.objects.all()
