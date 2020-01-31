from django.contrib import admin
from django.urls import path, re_path, include

import mastermind_game.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mastermind_game.urls')),
    re_path(r'^game/(g-.)(.)(.)(.)$', mastermind_game.views.game, name="game"),
]