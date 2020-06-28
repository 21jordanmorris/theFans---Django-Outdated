from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
from basketball_reference_scraper.seasons import get_schedule
from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.injury_report import get_injury_report
from utils import *
import sys
import pandas as pd
import numpy as np
import datetime
pd.options.mode.chained_assignment = None

# TODO: 
#   - Get injury report
#   - Check if away team has anyone on the report
#   - Check if home team has anyone on the report
#   - If so, get the player and return his win shares
#   - Add up total missing win shares and create a column displaying that
#   - Standardize it

def convert_team_names(entire_schedule):
    team_abbreviations = {'Atlanta Hawks' : 'ATL', 
                        'Brooklyn Nets' : 'BRK', 
                        'Boston Celtics' : 'BOS',
                        'Charlotte Hornets' : 'CHO',
                        'Chicago Bulls' : 'CHI',
                        'Cleveland Cavaliers' : 'CLE',
                        'Dallas Mavericks' : 'DAL',
                        'Denver Nuggets' : 'DEN',
                        'Detroit Pistons' : 'DET',
                        'Golden State Warriors' : 'GSW',
                        'Houston Rockets' : 'HOU',
                        'Indiana Pacers' : 'IND',
                        'Los Angeles Clippers' : 'LAC',
                        'Los Angeles Lakers' : 'LAL', 
                        'Memphis Grizzlies' : 'MEM', 
                        'Miami Heat' : 'MIA', 
                        'Milwaukee Bucks' : 'MIL', 
                        'Minnesota Timberwolves' : 'MIN', 
                        'New Orleans Pelicans' : 'NOP', 
                        'New York Knicks' : 'NYK', 
                        'Oklahoma City Thunder' : 'OKC', 
                        'Orlando Magic' : 'ORL', 
                        'Philadelphia 76ers' : 'PHI', 
                        'Phoenix Suns' : 'PHO', 
                        'Portland Trail Blazers' : 'POR', 
                        'Sacramento Kings' : 'SAC', 
                        'San Antonio Spurs' : 'SAS', 
                        'Toronto Raptors' : 'TOR', 
                        'Utah Jazz' : 'UTA', 
                        'Washington Wizards' : 'WAS'}

    team_abbreviations_keys = list(team_abbreviations.keys())

    row = 0
    for home_team in entire_schedule['HOME']:
        for i in range(0, 30):
            if team_abbreviations_keys[i] in home_team:
                entire_schedule.at[row, 'HOME'] = team_abbreviations[team_abbreviations_keys[i]]
        row += 1
    row = 0
    for away_team in entire_schedule['VISITOR']:
        for i in range(0, 30):
            if team_abbreviations_keys[i] in away_team:
                entire_schedule.at[row, 'VISITOR'] = team_abbreviations[team_abbreviations_keys[i]]
        row += 1
    
    a = datetime.datetime(2020, 7, 30)
    b = datetime.datetime(2020, 7, 31)
    c = datetime.datetime(2020, 8, 1)
    d = datetime.datetime(2020, 8, 2)
    e = datetime.datetime(2020, 8, 3)
    f = datetime.datetime(2020, 8, 4)
    g = datetime.datetime(2020, 8, 5)
    h = datetime.datetime(2020, 8, 6)
    i = datetime.datetime(2020, 8, 7)
    j = datetime.datetime(2020, 8, 8)
    k = datetime.datetime(2020, 8, 9)
    l = datetime.datetime(2020, 8, 10)
    m = datetime.datetime(2020, 8, 11)
    n = datetime.datetime(2020, 8, 12)
    o = datetime.datetime(2020, 8, 13)
    p = datetime.datetime(2020, 8, 14)

    date = [a,a,b,b,b,b,b,b,c,c,c,c,c,d,d,d,d,d,d,e,e,e,e,e,e,f,f,f,f,f,f,g,g,g,g,g,g,h,h,h,h,h,h,i,i,i,i,i,i,j,j,j,j,j,k,k,k,k,k,k,k,l,l,l,l,l,m,m,m,m,m,m,m,n,n,n,n,o,o,o,o,o,o,o,p,p,p,p]
    #date = ['7/30/2020', '7/30/2020', '7/31/2020', '7/31/2020', '7/31/2020', '7/31/2020', '7/31/2020', '7/31/2020', '8/1/2020', '8/1/2020', '8/1/2020', '8/1/2020', '8/1/2020', '8/2/2020', '8/2/2020', '8/2/2020', '8/2/2020', '8/2/2020', '8/2/2020', '8/3/2020', '8/3/2020', '8/3/2020', '8/3/2020', '8/3/2020', '8/3/2020', '8/4/2020', '8/4/2020', '8/4/2020', '8/4/2020', '8/4/2020', '8/4/2020', '8/5/2020', '8/5/2020', '8/5/2020', '8/5/2020', '8/5/2020', '8/5/2020', '8/6/2020', '8/6/2020', '8/6/2020', '8/6/2020', '8/6/2020', '8/6/2020', '8/7/2020', '8/7/2020', '8/7/2020', '8/7/2020', '8/7/2020', '8/7/2020', '8/8/2020', '8/8/2020', '8/8/2020', '8/8/2020', '8/8/2020',
    #                            '8/9/2020', '8/9/2020', '8/9/2020', '8/9/2020', '8/9/2020', '8/9/2020', '8/9/2020', '8/10/2020', '8/10/2020', '8/10/2020', '8/10/2020', '8/10/2020', '8/11/2020', '8/11/2020', '8/11/2020', '8/11/2020', '8/11/2020', '8/11/2020', '8/11/2020', '8/12/2020', '8/12/2020', '8/12/2020', '8/12/2020', '8/13/2020', '8/13/2020', '8/13/2020', '8/13/2020', '8/13/2020', '8/13/2020', '8/13/2020', '8/14/2020', '8/14/2020', '8/14/2020', '8/14/2020']
    
    empty = [" "] * len(date)

    df1 = pd.DataFrame({'VISITOR' : ['UTA', 'LAC', 'ORL', 'MEM', 'PHO', 'BOS', 'SAC', 'HOU', 'MIA', 'UTA', 'NOP', 'PHI', 'LAL', 'WAS', 'POR', 'SAS', 'SAC', 'MIL', 'DAL', 'TOR', 'DEN', 'IND', 'MEM', 'SAS', 'LAL', 'BRK', 'DAL', 'PHO', 'ORL', 'BOS', 'HOU', 'MEM', 'PHI', 'DEN', 'OKC', 'TOR', 'BRK', 'NOP', 'MIA', 'IND', 'LAC', 'POR', 'LAL', 'UTA', 'OKC', 'SAC', 'ORL', 'WAS', 'BOS', 'LAC', 'UTA', 'LAL', 'PHO', 'MIL', 'WAS', 'MEM', 'SAS', 'ORL', 'PHI', 'HOU', 'BRK', 'OKC', 'DAL', 'TOR', 'IND', 'DEN', 'BRK', 'HOU', 'PHO', 'POR', 'BOS', 'NOP', 'MIL', 'IND', 'TOR', 'MIA', 'LAC', 'WAS', 'POR', 'SAC', 'MIL', 'NOP', 'DAL', 'SAS', 'PHI', 'MIA', 'OKC', 'DEN'],
                       'VISITOR_PTS': empty,
                       'HOME' : ['NOP', 'LAL', 'BRK', 'POR', 'WAS', 'MIL', 'SAS', 'DAL', 'DEN', 'OKC', 'LAC', 'IND', 'TOR', 'BRK', 'BOS', 'MEM', 'ORL', 'HOU', 'PHO', 'MIA', 'OKC', 'WAS', 'NOP', 'PHI', 'UTA', 'MIL', 'SAC', 'LAC', 'IND', 'MIA', 'POR', 'UTA', 'WAS', 'SAS', 'LAL', 'ORL', 'BOS', 'SAC', 'MIL', 'PHO', 'DAL', 'DEN', 'HOU', 'SAS', 'MEM', 'BRK', 'PHI', 'NOP', 'TOR', 'POR', 'DEN', 'IND', 'MIA', 'DAL', 'OKC', 'TOR', 'NOP', 'BOS', 'POR', 'SAC', 'LAC', 'PHO', 'UTA', 'MIL', 'MIA', 'LAL', 'ORL', 'SAS', 'PHI', 'DAL', 'MEM', 'SAC', 'WAS', 'HOU', 'PHI', 'OKC', 'DEN', 'BOS', 'BRK', 'LAL', 'MEM', 'ORL', 'PHO', 'UTA', 'HOU', 'IND', 'LAC', 'TOR'],
                       'HOME_PTS': empty,
                       'DATE' : date})

    entire_schedule = pd.concat([entire_schedule, df1], sort=False)

    return entire_schedule

def add_winner_column(entire_schedule):
    winner = []
    for index, row in entire_schedule.iterrows():
        if pd.isna(row['HOME_PTS']) or pd.isna(row['VISITOR_PTS']):
            winner.insert(index, float('Nan'))
        elif row['HOME_PTS'] > row['VISITOR_PTS']:
            winner.insert(index, 1)
        else:
            winner.insert(index, 0)
    entire_schedule["WINNER"] = winner
    return entire_schedule

def add_conference_game(entire_schedule):
    west_teams = [
        'DAL','DEN','GSW','HOU','LAC','LAL','MEM','MIN',
        'NOP','OKC','PHO','POR','SAC','SAS','UTA']
    east_teams = [
        'ATL','BRK','BOS','CHO','CHI','CLE','DET','IND',
        'MIA','MIL','NYK','ORL','PHI','TOR','WAS']
    conference_game = []
    for index, row in entire_schedule.iterrows():
        if (row['HOME'] in west_teams and row['VISITOR'] in west_teams) or (row['HOME'] in east_teams and row['VISITOR'] in east_teams):
            conference_game.insert(index, 1)
        else:
            conference_game.insert(index, 0)
    entire_schedule["CON_GAME"] = conference_game
    return entire_schedule

def add_team_stats(entire_schedule):
    team_misc_2020 = getTeamMisc(2020)
    team_misc_2019 = getTeamMisc(2019)
    last_year_win_percentage_home = []
    last_year_win_percentage_visitor = []
    count = 1
    for index, row in entire_schedule.iterrows():
        home = team_misc_2019.loc[team_misc_2019['TEAM'] == row['HOME'], 'W'].values[0]
        visitor = team_misc_2019.loc[team_misc_2019['TEAM'] == row['VISITOR'], 'W'].values[0]

        last_year_win_percentage_home.insert(index, home/82)
        last_year_win_percentage_visitor.insert(index, visitor/82)

        home_team_season_stats = team_misc_2020[team_misc_2020['TEAM'] == row['HOME']].add_prefix("HOME_")
        visitor_team_season_stats = team_misc_2020[team_misc_2020['TEAM'] == row['VISITOR']].add_prefix("VISITOR_")

        home_team_season_stats = home_team_season_stats[['HOME_NRtg', 'HOME_DRtg', 'HOME_ORtg', 'HOME_DRB%', 'HOME_SRS', 'HOME_MOV', 
            'HOME_PACE']]
        visitor_team_season_stats = visitor_team_season_stats[['VISITOR_NRtg', 'VISITOR_DRtg', 'VISITOR_ORtg', 'VISITOR_DRB%', 'VISITOR_SRS', 'VISITOR_MOV',
            'VISITOR_PACE']]
        
        if count == 1:
            home_team_stats = home_team_season_stats
            visitor_team_stats = visitor_team_season_stats
        else:
            home_team_stats = pd.concat([home_team_stats, home_team_season_stats])
            visitor_team_stats = pd.concat([visitor_team_stats, visitor_team_season_stats])
        count += 1

    entire_schedule = entire_schedule.reset_index(drop=True)
    home_team_stats = home_team_stats.reset_index(drop=True)
    visitor_team_stats = visitor_team_stats.reset_index(drop=True)
    entire_schedule = pd.concat([entire_schedule, home_team_stats, visitor_team_stats], axis=1, sort=True)
    entire_schedule["HOME_LAST_SEASON_W%"] = last_year_win_percentage_home
    entire_schedule["VISITOR_LAST_SEASON_W%"] = last_year_win_percentage_visitor
    entire_schedule["HOME_GAME"] = [1] * len(entire_schedule)
    entire_schedule["AWAY GAME"] = [0] * len(entire_schedule)
    return entire_schedule

def add_win_percentage(entire_schedule):
    teams = [
        'ATL','BRK','BOS','CHO','CHI','CLE','DAL','DEN',
        'DET','GSW','HOU','IND','LAC','LAL','MEM','MIA', 
        'MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO', 
        'POR','SAC','SAS','TOR','UTA','WAS']
    init = [0] * 30
    data = {'wins' : init, 'losses' : init}

    injury_report = get_injury_report()
    win_loss = pd.DataFrame(data, index=teams)
    home_win_percentage = []
    visitor_win_percentage = []
    for index, row in entire_schedule.iterrows():
        
        if (win_loss.loc[row['HOME'], 'wins'] + win_loss.loc[row['HOME'], 'losses']) == 0:
            if win_loss.loc[row['HOME'], 'wins'] > 0:
                home_win_per = 1
            else:
                home_win_per = 0
        else:
            home_wins = win_loss.loc[row['HOME'], 'wins']
            if get_first_no_result_date(entire_schedule) == row['DATE']:
                injury_account = get_missing_win_shares(injury_report, row['HOME'])
                home_wins += injury_account
            home_win_per = home_wins / (win_loss.loc[row['HOME'], 'wins'] + win_loss.loc[row['HOME'], 'losses'])

        if (win_loss.loc[row['VISITOR'], 'wins'] + win_loss.loc[row['VISITOR'], 'losses']) == 0:
            if win_loss.loc[row['VISITOR'], 'wins'] > 0:
                visitor_win_per = 1
            else:
                visitor_win_per = 0
        else:
            visitor_wins = win_loss.loc[row['VISITOR'], 'wins']
            if get_first_no_result_date(entire_schedule) == row['DATE']:
                injury_account = get_missing_win_shares(injury_report, row['VISITOR'])
                visitor_wins += injury_account
            visitor_win_per = visitor_wins / (win_loss.loc[row['VISITOR'], 'wins'] + win_loss.loc[row['VISITOR'], 'losses'])

        home_win_percentage.insert(index, home_win_per)
        visitor_win_percentage.insert(index, visitor_win_per)

        if row['WINNER'] == 1:
            win_loss.at[row['HOME'],'wins'] = win_loss.loc[row['HOME'],'wins'] + 1
            win_loss.at[row['VISITOR'],'losses'] = win_loss.loc[row['VISITOR'],'losses'] + 1
        elif row['WINNER'] == 0:
            win_loss.at[row['VISITOR'],'wins'] = win_loss.loc[row['VISITOR'],'wins'] + 1
            win_loss.at[row['HOME'],'losses'] = win_loss.loc[row['HOME'],'losses'] + 1

    entire_schedule["HOME_W%"] = home_win_percentage
    entire_schedule["VISITOR_W%"] = visitor_win_percentage
    return entire_schedule

def add_home_away_splits(entire_schedule):
    teams = [
        'ATL','BRK','BOS','CHO','CHI','CLE','DAL','DEN',
        'DET','GSW','HOU','IND','LAC','LAL','MEM','MIA', 
        'MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO', 
        'POR','SAC','SAS','TOR','UTA','WAS']
    init = [0] * 30
    data = {'home_wins' : init, 'home_losses' : init, 'road_wins': init, 'road_losses' : init}
    home_road_split = pd.DataFrame(data, index=teams)
    home_win_at_home = []
    visitor_win_on_road = []
    for index, row in entire_schedule.iterrows():
        if (home_road_split.loc[row['HOME'], 'home_wins'] + home_road_split.loc[row['HOME'], 'home_losses']) == 0:
            if home_road_split.loc[row['HOME'], 'home_wins'] > 0:
                home_win_per = 1
            else:
                home_win_per = 0
        else:
            home_wins = home_road_split.loc[row['HOME'], 'home_wins']
            home_win_per = home_wins / (home_road_split.loc[row['HOME'], 'home_wins'] + home_road_split.loc[row['HOME'], 'home_losses'])

        if (home_road_split.loc[row['VISITOR'], 'road_wins'] + home_road_split.loc[row['VISITOR'], 'road_losses']) == 0:
            if home_road_split.loc[row['VISITOR'], 'road_wins'] > 0:
                visitor_win_per = 1
            else:
                visitor_win_per = 0
        else:
            visitor_wins = home_road_split.loc[row['VISITOR'], 'road_wins']
            visitor_win_per = visitor_wins / (home_road_split.loc[row['VISITOR'], 'road_wins'] + home_road_split.loc[row['VISITOR'], 'road_losses'])

        home_win_at_home.insert(index, home_win_per)
        visitor_win_on_road.insert(index, visitor_win_per)

        if row['WINNER'] == 1:
            home_road_split.at[row['HOME'],'home_wins'] = home_road_split.loc[row['HOME'],'home_wins'] + 1
            home_road_split.at[row['VISITOR'],'road_losses'] = home_road_split.loc[row['VISITOR'],'road_losses'] + 1
        elif row['WINNER'] == 0:
            home_road_split.at[row['VISITOR'],'road_wins'] = home_road_split.loc[row['VISITOR'],'road_wins'] + 1
            home_road_split.at[row['HOME'],'home_losses'] = home_road_split.loc[row['HOME'],'home_losses'] + 1

    entire_schedule['HOME_W%_AT_HOME'] = home_win_at_home
    entire_schedule['VISITOR_W%_ON_ROAD'] = visitor_win_on_road
    return entire_schedule

def add_second_of_b2b(entire_schedule):
    teams_that_played_last_night = []
    teams_that_played_today = []
    home_team_b2b = []
    visitor_team_b2b = []
    last_night_day = "Monday"

    for index, row in entire_schedule.iterrows():
        day = pd.Timestamp.day_name(row['DATE'])
        
        if get_next_day(last_night_day) != day:
            teams_that_played_last_night = teams_that_played_today
            teams_that_played_today = []
            last_night_day = get_day_before(day)
        
        if get_next_day(last_night_day) == day:
            if row['HOME'] in teams_that_played_last_night:
                home_team_b2b.insert(index, 1)
            else:
                home_team_b2b.insert(index, 0)

            if row['VISITOR'] in teams_that_played_last_night:
                visitor_team_b2b.insert(index, 1)
            else:
                visitor_team_b2b.insert(index, 0)
        
        teams_that_played_today.append(row['HOME'])
        teams_that_played_today.append(row['VISITOR'])

    entire_schedule["HOME_B2B"] = home_team_b2b
    entire_schedule["VISITOR_B2B"] = visitor_team_b2b
    return entire_schedule

def add_last_twenty(entire_schedule):
    team_last_twenty = get_teams_last_twenty_init()
    home_last_twenty_percent = []
    visitor_last_twenty_percent = []
    for index, row in entire_schedule.iterrows():

        home_last_twenty_percent.append(get_win_loss_percentage_last_twenty(row['HOME'], team_last_twenty))
        visitor_last_twenty_percent.append(get_win_loss_percentage_last_twenty(row['VISITOR'], team_last_twenty))
        
        if not pd.isna(row['WINNER']):
            temp_home = team_last_twenty[row['HOME']]
            temp_home.pop(0)
            temp_visitor = team_last_twenty[row['VISITOR']]
            temp_visitor.pop(0)

            if row['WINNER'] == 1:
                temp_home.append('W')
                temp_visitor.append('L')
                team_last_twenty.update({row['HOME'] : temp_home})
                team_last_twenty.update({row['VISITOR'] : temp_visitor})
            elif row['WINNER'] == 0:
                temp_home.append('L')
                temp_visitor.append('W')
                team_last_twenty.update({row['HOME'] : temp_home})
                team_last_twenty.update({row['VISITOR'] : temp_visitor})

    entire_schedule["HOME_LAST_20"] = home_last_twenty_percent
    entire_schedule["VISITOR_LAST_20"] = visitor_last_twenty_percent
    return entire_schedule

def finalize_csv(name, year):
    entire_schedule = get_schedule(year, playoffs=False)
    entire_schedule = convert_team_names(entire_schedule)
    add_winner_column(entire_schedule)
    entire_schedule = add_win_percentage(add_team_stats(entire_schedule))
    entire_schedule = add_second_of_b2b(entire_schedule)
    entire_schedule = add_home_away_splits(entire_schedule)
    entire_schedule = add_last_twenty(entire_schedule)
    entire_schedule.to_csv(name, index=False)
    
    sys.stderr.write("[PROGRESS] CSV file creation completed!\n")
    sys.stderr.flush()
    
    return name