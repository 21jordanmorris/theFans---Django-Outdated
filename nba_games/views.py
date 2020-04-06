from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Game

class GamesView(generic.ListView):
    model = Game
    template_name = 'games.html'

def game_detail(request, id=None):
    instance = get_object_or_404(Game, id=id)
    context = {
        "home_team": instance.home_team,
        "visitor_team": instance.visitor_team,
        "home_prob": instance.home_probability,
        "visitor_prob": instance.visitor_probability,
    }
    return render(request, "game_detail.html", context)