from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "shirt_number", "position", "goals", "assists")
    search_fields = ("name", "shirt_number")
    list_filter = ("position",)
