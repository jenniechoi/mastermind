from django.template import loader
from django.conf import settings

import requests
from . import models
from . import forms

def start_game(answer_num:int):
    answer_num = str(answer_num[0])
    url = 'https://www.random.org/integers/?num='+answer_num+'&min=0&max=7&col=1&base=10&format=plain&rnd=new'
    r = requests.get(url)
    answer = r.text
    answer = answer.replace('\t', '').replace('\n', '')
    game = models.Game(answer=answer, current_guess=0, difficulty=answer_num)
    game.save()    
    return(game.id)

def check_guess(game_id: str, guess:list, answer:str, guess_count:int):
    guess = ''.join(guess)
    guess_count += 1

    result = False

    if guess == answer:
        game_update = models.Game.objects.get(id=game_id)
        game_update.result = True
        right_nums = len(answer)
        right_spot = len(answer)        
        game_update.save()
    else:
        guess_nums = {}
        for index in range(len(guess)):
            guess_nums[index] = guess[index]
        answer_nums = {}
        for index in range(len(answer)):
            answer_nums[index] = answer[index]
        
        found_nums = []
        right_spot = 0
        right_nums = 0

        for index in guess_nums:
            if guess_nums[index] in answer_nums.values():
                if guess_nums[index] not in found_nums:
                    found_nums.append(guess_nums[index])
        for number in found_nums:
            number_found = 0
            if answer.count(number) == guess.count(number):
                number_found = answer.count(number)
            else:
                if answer.count(number) < guess.count(number):
                    number_found = answer.count(number)
                else:
                    number_found = guess.count(number)
            right_nums += number_found

        for index in guess_nums:
            if guess_nums[index] in answer_nums.values():
                if guess_nums[index] == answer_nums[index]:
                    right_spot += 1
    guess_details = models.Guess(game_id=game_id, guess=guess, guess_num = guess_count, nums_right = right_nums, places_right=right_spot)
    guess_details.save()

    game_update = models.Game.objects.get(id=game_id)
    game_update.current_guess = guess_count
    game_update.save()

    if game_update.difficulty == 3:
        form = forms.EasyGuess
    elif game_update.difficulty == 4:
        form = forms.MediumGuess
    elif game_update.difficulty == 5:
        form = forms.HardGuess
    past_guesses = models.Guess.objects.filter(game_id=game_id)
    guesses_remaining = 10-guess_count
    
    return{
        "past_guesses": past_guesses,
        "form": form,
        "game_result": game_update.result,
        "guess_count": guess_count,
        "guesses_remaining": guesses_remaining,
    }

def get_results(game_id: int):
    game_id = game_id
    game_results = models.Game.objects.get(pk=game_id)
    guess_results = models.Guess.objects.filter(game_id=game_id)

    easy_wins = len(models.Game.objects.filter(difficulty=3, result=True))
    medium_wins = len(models.Game.objects.filter(difficulty=4, result=True))
    hard_wins = len(models.Game.objects.filter(difficulty=5, result=True))
    all_wins = len(models.Game.objects.filter(result=True))

    all_easy = len(models.Game.objects.filter(difficulty=3))
    all_medium = len(models.Game.objects.filter(difficulty=4))
    all_hard = len(models.Game.objects.filter(difficulty=5))
    all_games = len(models.Game.objects.all())

    return{
        'game_results': game_results,
        'guess_results': guess_results,
        'easy_wins': easy_wins,
        'medium_wins': medium_wins,
        'hard_wins': hard_wins,
        'all_wins': all_wins,
        'all_easy': all_easy,
        'all_medium': all_medium,
        'all_hard': all_hard,
        'all_games': all_games,
    }