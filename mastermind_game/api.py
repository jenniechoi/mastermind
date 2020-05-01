from django.template import loader
from django.conf import settings

import requests
from . import models
from . import forms

def start_game(difficulty_level:int, username:str):
    difficulty_level = str(difficulty_level[0])
    url = 'https://www.random.org/integers/?num='+difficulty_level+'&min=0&max=7&col=1&base=10&format=plain&rnd=new'
    r = requests.get(url)
    answer = r.text
    answer = answer.replace('\t', '').replace('\n', '')
    game = models.Game(answer=answer, current_guess=0, difficulty=difficulty_level, username=username)
    game.save()    

    try:
        user = models.User.objects.get(username=username)
    except:
        user = models.User(username = username)
        user.save()

    return(game.id)

def check_guess(game_id: str, guess:list, answer:str, guess_count:int):
    guess = ''.join(guess)
    guess_count += 1

    win = False

    if guess == answer:
        game_update = models.Game.objects.get(id=game_id)
        game_update.win = True
        correct_digits = len(answer)
        correct_position = len(answer)        
        game_update.save()

    else:
        guess_nums = {}
        for index in range(len(guess)):
            guess_nums[index] = guess[index]
        answer_nums = {}
        for index in range(len(answer)):
            answer_nums[index] = answer[index]
        
        unique_found_digits = []
        correct_position = 0
        correct_digits = 0

        for index in guess_nums:
            if guess_nums[index] in answer_nums.values():
                if guess_nums[index] not in unique_found_digits:
                    unique_found_digits.append(guess_nums[index])
        for number in unique_found_digits:
            number_found = 0
            if answer.count(number) == guess.count(number):
                number_found = answer.count(number)
            else:
                if answer.count(number) < guess.count(number):
                    number_found = answer.count(number)
                else:
                    number_found = guess.count(number)
            correct_digits += number_found

        for index in guess_nums:
            if guess_nums[index] in answer_nums.values():
                if guess_nums[index] == answer_nums[index]:
                    correct_position += 1
    guess_details = models.Guess(game_id=game_id, guess=guess, guess_num = guess_count, correct_digits = correct_digits, correct_position=correct_position)
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
        "win": game_update.win,
        "guess_count": guess_count,
        "guesses_remaining": guesses_remaining,
    }

def get_results(game_id: int):
    game_id = game_id
    game_results = models.Game.objects.get(pk=game_id)
    guess_results = models.Guess.objects.filter(game_id=game_id)
    username = game_results.username

    user_details = models.User.objects.get(username=username)
    total_wins = user_details.total_wins
    total_games = user_details.total_games
    average_guesses = user_details.average_guesses

    if game_results.win == True:
        total_wins += 1
    average_guesses = ((average_guesses * total_games) + len(guess_results))/(total_games+1)
    total_games += 1

    user_update = models.User.objects.get(username=username)
    user_update.total_games = total_games
    user_update.total_wins = total_wins
    user_update.average_guesses = average_guesses
    user_update.save()

    easy_wins = len(models.Game.objects.filter(difficulty=3, win=True))
    medium_wins = len(models.Game.objects.filter(difficulty=4, win=True))
    hard_wins = len(models.Game.objects.filter(difficulty=5, win=True))
    all_wins = len(models.Game.objects.filter(win=True))

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
        'user_update': user_update,
    }