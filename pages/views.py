from django.shortcuts import render
from django.apps import apps
from django.db import connection

PostModel = apps.get_model('posts', 'Post')
GameModel = apps.get_model('nba_games', 'Game')

def index(request):
    post_queryset = PostModel.objects.all()[:3]
    count = GameModel.objects.count() - 88

    game_queryset = GameModel.objects.all()[count:count+3]

    context = {
        "post_list": post_queryset,
        "game_list": game_queryset,
    }

    connection.close()

    return render(request, 'index.html', context)
