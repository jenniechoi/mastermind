from django.db import models


class Game(models.Model):
    answer = models.CharField(max_length=5)
    current_guess = models.IntegerField()
    result = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=0)


class Guess(models.Model):
    game_id = models.IntegerField(default=0)
    guess = models.CharField(max_length=4)
    guess_num = models.IntegerField(default=0)
    nums_right = models.IntegerField(default=0)
    places_right = models.IntegerField(default=0)

