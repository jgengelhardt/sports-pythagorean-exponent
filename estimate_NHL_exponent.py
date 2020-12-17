import json
import os
import pandas as pd
import requests

def get_season_exponents_NHL(league,startyear):
    # get franchise records from a given season
    yearid = int(f"{startyear}{startyear+1}")
    season_teams = []
    for element in league:
        if element['seasonId'] == yearid:
            season_teams.append(element)
    # only include regular season
    filtered_teams = []
    for team in season_teams:
        if team['gamesPlayed'] == season_teams[0]['gamesPlayed']:
            filtered_teams.append(team)
    # calculate exponent for each franchise in that season
    df = pd.DataFrame(columns=['year','team','exponent'])
    for team in filtered_teams:
        row = {}
        # get input row in dictionary format
        # key = col_name
        try:
            win_pct = (team['wins']+(team['ties']*.5))/team['gamesPlayed']
        except:
            continue
        exponent = find_pyth_exponent(win_pct,team['goals'],team['goalsAgainst'])
        row = {'year':startyear, 'team':team['teamName'], 'exponent':exponent}
        df = df.append(row, ignore_index=True)
    return df

def get_all_NHL_exponents():
    league_request = requests.get('https://records.nhl.com/site/api/franchise-season-results')
    league_json = league_request.json()
    NHL_alltime = league_json['data']
    df = pd.DataFrame(columns=['year','team','exponent'])
    print('Loaded NHL franchise season results from API')
    try:
        for i in range(1917,2022):
            score = pd.DataFrame(columns=['year','team','exponent'])
            score = get_season_exponents_NHL(NHL_alltime,i)
            print (f'Loaded NHL season {i}', end="\r", flush=True)
            df = df.append(score)
    finally:
        df = df[df['exponent'] != 'Error']
        csvFile = open('./results/NHL_exponents.csv', 'w', newline='')
        df.to_csv(csvFile, index=False)
        csvFile.close()
        print('\nNHL .csv written', flush=True)
        
# new_file_name = os.path.join(csv_folder, "results", f"{file.stem}-edited.csv")

get_all_NHL_exponents()
