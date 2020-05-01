import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import api
from . import forms
from . import models

def genctx(request):
    return {}

def home(request):
    if request.method =='POST':
        form = forms.Difficulty(request.POST)
        if form.is_valid():
            difficulty_level = form.cleaned_data['difficulty']
            username = form.cleaned_data['username']
            game_id = api.start_game(difficulty_level, username)
            return HttpResponseRedirect(reverse('game', args=(game_id, )))
    return render(request, 'mastermind_game/index.html', {'form': forms.Difficulty})

def game(request, game_id:int):
    context = genctx(request)
    game_details = models.Game.objects.get(id=game_id)
    answer = game_details.answer
    guess_count = game_details.current_guess
    difficulty = game_details.difficulty

    if difficulty == 3:
        form = forms.EasyGuess
    elif difficulty == 4:
        form = forms.MediumGuess
    elif difficulty == 5:
        form = forms.HardGuess

    if request.method == 'POST':
        if difficulty == 3:
            form_posted = forms.EasyGuess(request.POST)
        elif difficulty == 4:
            form_posted = forms.MediumGuess(request.POST)
        elif difficulty == 5:
            form_posted = forms.HardGuess(request.POST)

        if form_posted.is_valid():
            guess = []
            for num in range(1, difficulty+1):
                guess.append(form_posted.cleaned_data['digit_'+str(num)])
            context.update(api.check_guess(str(game_id), guess, answer, guess_count))
            template = loader.get_template('mastermind_game/game.html')
            if context['win'] == True or context['guess_count'] >= 10:
                return HttpResponseRedirect(reverse('results', args=(game_id, )))
            else:
                return HttpResponse(template.render(context, request))
    return render(request, 'mastermind_game/game.html', {'form': form})

def results(request, game_id:int):
    context = genctx(request)
    context.update(api.get_results(game_id))
    template = loader.get_template('mastermind_game/results.html')
    if request.method =='POST':
        return HttpResponseRedirect(reverse('home'))
    return HttpResponse(template.render(context, request))