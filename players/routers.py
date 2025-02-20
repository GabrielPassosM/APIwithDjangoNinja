from uuid import UUID

from ninja import Router
from django.shortcuts import get_object_or_404

from players.models import Player
from players.serializers import PlayerResponse, PlayerCreate, PlayerIncrementStats

router = Router()


@router.get("/", response=list[PlayerResponse])
def get_players(request):
    return Player.objects.all()


@router.get("/{player_id}", response=PlayerResponse)
def get_player(request, player_id: UUID):
    player = get_object_or_404(Player, id=player_id)
    return player


@router.post("/", response=PlayerResponse)
def create_player(request, player_info: PlayerCreate):
    player = Player.objects.create(**player_info.dict())
    return player


@router.put("/{player_id}", response=PlayerResponse)
def update_player(request, player_id: UUID, player_info: PlayerCreate):
    player = get_object_or_404(Player, id=player_id)
    player_info = player_info.dict()

    # check if there is any change
    if all(getattr(player, attr) == value for attr, value in player_info.items()):
        return

    for attr, value in player_info.items():
        setattr(player, attr, value)

    player.save()
    return player


@router.put("/increment/{player_id}", response=PlayerResponse)
def increment_player_stats(
    request, player_id: UUID, increment_info: PlayerIncrementStats
):
    player = get_object_or_404(Player, id=player_id)

    for attr, value in increment_info.dict().items():
        setattr(player, attr, getattr(player, attr) + value)

    player.save()
    return player


@router.delete("/{player_id}")
def delete_player(request, player_id: UUID) -> None:
    player = get_object_or_404(Player, id=player_id)
    player.delete()
