import json
import requests
import pandas as pd
import os

key = 'fc03e6f4788d46dd8e578880050ba639'
url = (f"https://api.football-data.org/v4/competitions/CL/matches")

headers = {
    'X-Auth-Token': key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    result = response.json()

    match_ids = []
    competition_names = []
    home_team_names = []
    home_team_ids = []
    home_team_crests = []
    away_team_names = []
    away_team_ids = []
    away_team_crests = []
    scores_home = []
    scores_away = []
    match_dates = []
    referee_names = []
    referee_nationalities = []

    for match in result['matches']:
        match_ids.append(match['id'])  
        competition_names.append(match['competition']['name'])  
        home_team_names.append(match['homeTeam']['name'])  
        home_team_ids.append(match['homeTeam']['id'])  
        away_team_names.append(match['awayTeam']['name']) 
        away_team_ids.append(match['awayTeam']['id']) 
        scores_home.append(match['score']['fullTime']['home']) 
        scores_away.append(match['score']['fullTime']['away']) 
        match_dates.append(match['utcDate'])  

        
        if match['referees']:
            referee_names.append(match['referees'][0]['name'])  
            referee_nationalities.append(match['referees'][0].get('nationality', 'Unknown'))  
        else:
            referee_names.append('Unknown')
            referee_nationalities.append('Unknown')

    match_data = {
        'Match ID': match_ids,
        'Competition Name': competition_names,
        'Home Team Name': home_team_names,
        'Home Team ID': home_team_ids,
        'Away Team Name': away_team_names,
        'Away Team ID': away_team_ids,
        'Home Team Score': scores_home,
        'Away Team Score': scores_away,
        'Match Date': match_dates,
        'Referee Name': referee_names,
        'Referee Nationality': referee_nationalities,
    }

    df = pd.DataFrame(match_data)
    print(df)
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, 'champions_league_matches.csv')
    df.to_csv(file_path, index=False)
    print(f'Data saved to {file_path}')
    


