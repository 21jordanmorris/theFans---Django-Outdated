from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Game

class GamesView(generic.ListView):
    model = Game
    template_name = 'games.html'

@login_required
def game_detail(request, slug=None):
    instance = get_object_or_404(Game, slug=slug)

    if is_east_team(instance.home_team):
        home_user = "tboyle24_DFS"
    else:
        home_user = "gstroms99"
    
    if is_east_team(instance.visitor_team):
        visitor_user = "tboyle24_DFS"
    else:
        visitor_user = "gstroms99"

    context = {
        "instance" : instance,
        "home_team": instance.home_team,
        "visitor_team": instance.visitor_team,
        "home_prob": instance.home_probability,
        "visitor_prob": instance.visitor_probability,
        "home_twitter": convert_team_name(instance.home_team),
        "visitor_twitter": convert_team_name(instance.visitor_team),
        "home_user": home_user,
        "visitor_user": visitor_user,
        "room_name": slug,
    }
    return render(request, "game_detail.html", context)


def convert_team_name(team):
    switcher = {
        'ATL' : 'atlanta-hawks', 
        'BRK' : 'brooklyn-nets', 
        'BOS' : 'boston-celtics',
        'CHO' : 'charlotte-hornets',
        'CHI' : 'chicago-bulls',
        'CLE' : 'cleveland-cavaliers',
        'DAL' : 'dallas-mavericks',
        'DEN' : 'denver-nuggets',
        'DET' : 'detroit-pistons',
        'GSW' : 'golden-state-warriors',
        'HOU' : 'houston-rockets',
        'IND' : 'indiana-pacers',
        'LAC' : 'los-angeles-clippers',
        'LAL' : 'los-angeles-lakers', 
        'MEM' : 'memphis-grizzlies', 
        'MIA' : 'miami-heat', 
        'MIL' : 'milwaukee-bucks', 
        'MIN' : 'minnesota-timberwolves', 
        'NOP' : 'new-orleans-pelicans', 
        'NYK' : 'new-york-knicks', 
        'OKC' : 'oklahome-city-thunder', 
        'ORL' : 'orlando-magic', 
        'PHI' : 'philadelphia-76ers', 
        'PHO' : 'phoenix-suns', 
        'POR' : 'portland-trail-blazers', 
        'SAC' : 'sacramento-kings', 
        'SAS' : 'san-antonio-spurs', 
        'TOR' : 'toronto-raptors', 
        'UTA' : 'utah-jazz', 
        'WAS' : 'washington-wizards',
    }
    return switcher.get(team, "Invalid team name given.")

def is_east_team(team):
    east = ['ATL', 'BRK', 'BOS', 'CHO', 'CHI', 'CLE', 'DET', 'IND', 'MIA', 'MIL', 'NYK', 'ORL', 'PHI', 'TOR', 'WAS']
    if team in east:
        return True
    else:
        return False