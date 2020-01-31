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
    try:
        if request.method =='POST':
            form = forms.Difficulty(request.POST)
            if form.is_valid():
                answer_num = form.cleaned_data['difficulty']
                game_id = api.start_game(answer_num)
                return HttpResponseRedirect(reverse('game', args=(game_id, )))
        return render(request, 'mastermind_game/index.html', {'form': forms.Difficulty})
    except:
        return HttpResponse(status=404)

def game(request, game_id:int):
    context = genctx(request)
    game_details = models.Game.objects.get(id=game_id)
    answer = game_details.answer
    guess_count = game_details.current_guess
    difficulty = game_details.difficulty
    
    if game_details.result == True or guess_count >= 10:
        return HttpResponseRedirect(reverse('results', args=(game_id, )))

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

        try:
            if form_posted.is_valid():
                guess = []
                for num in range(1, difficulty+1):
                    guess.append(form_posted.cleaned_data['digit_'+str(num)])
                context.update(api.check_guess(str(game_id), guess, answer, guess_count))
                template = loader.get_template('mastermind_game/game.html')
                if context['game_result'] == True or context['guess_count'] >= 10:
                    return HttpResponseRedirect(reverse('results', args=(game_id, )))
                else:
                    return HttpResponse(template.render(context, request))
        except:
            return HttpResponse(status=404)
    return render(request, 'mastermind_game/game.html', {'form': form})

def results(request, game_id:int):
    context = genctx(request)
    try:
        if request.method =='POST':
            return HttpResponseRedirect(reverse('home'))
        context.update(api.get_results(game_id))
        template = loader.get_template('mastermind_game/results.html')
        return HttpResponse(template.render(context, request))
    except:
        return HttpResponse(status=404)