from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from players.routers import router as players_router


api = NinjaAPI()


@api.get("/")
def index(request):
    return "Hello, World!"


api.add_router("/players", players_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
]
