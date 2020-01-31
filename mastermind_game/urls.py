from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('results/<int:game_id>/', views.results, name="results"),
    path('game/<int:game_id>/', views.game, name="game")

]
