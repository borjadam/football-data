from dotenv import load_dotenv
import requests 
import os

# Load environment variables
load_dotenv()

# Check if the API key is loaded
api_key = os.getenv('API_KEY')
if api_key:
    print("API key is correctly set.")
else:
    print("API key is not set.")

competition_id = '2014'
fc_barcelona_id = '81'

def list_teams_in_competition(api_key, competition_id):
    url = f"https://api.football-data.org/v4/competitions/{competition_id}/teams"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for team in response.json().get('teams', []):
            print(f"ID: {team['id']}, Name: {team['name']}")
    else:
        print('Failed to fetch teams')

#list_teams_in_competition(api_key, competition_id)


def upcoming_matches_fc_barcelona(api_key):
    base_url = 'https://api.football-data.org/v4/'
    team_id = '81'
    headers = {'X-Auth-Token': api_key}

    # construct the URL to fetch matches
    matches_url = f"{base_url}/teams/{team_id}/matches?status=SCHEDULED"
    response = requests.get(matches_url, headers=headers)
    if response.status_code == 200:
        matches_data = response.json()
        print(f"Upcoming matches for F.C Barcelona:")
        for match in matches_data.get('matches', []):
            competition = match['competition']['name']
            date = match['utcDate']
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            print(f"{competition}: {home_team} vs {away_team} on {date}")
        else:
            print(f"failed to fecth matches. Status Code: {response.status_code}")

if __name__ == "__main__":
    upcoming_matches_fc_barcelona(api_key)
