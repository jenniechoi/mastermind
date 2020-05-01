from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    total_wins = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    average_guesses = models.IntegerField(default=0)

class Game(models.Model):
    answer = models.CharField(max_length=5)
    current_guess = models.IntegerField()
    win = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=0)
    username = models.CharField(max_length=25, default="user")


class Guess(models.Model):
    game_id = models.IntegerField(default=0)
    guess = models.CharField(max_length=4)
    guess_num = models.IntegerField(default=0)
    correct_digits = models.IntegerField(default=0)
    correct_position = models.IntegerField(default=0)

