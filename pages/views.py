from django.shortcuts import render
from django.apps import apps

PostModel = apps.get_model('posts', 'Post')
GameModel = apps.get_model('nba_games', 'Game')

def index(request):
    post_queryset = PostModel.objects.all()[:3]
    game_queryset = GameModel.objects.all()[971:974]

    context = {
        "post_list": post_queryset,
        "game_list": game_queryset,
    }

    return render(request, 'index.html', context)
