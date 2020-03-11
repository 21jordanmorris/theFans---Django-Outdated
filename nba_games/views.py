from django.shortcuts import render
from django.views import generic
from .models import Game

class GamesView(generic.ListView):
    model = Game
    template_name = 'games.html'