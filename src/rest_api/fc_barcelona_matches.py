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

competition_id = 2014

def list_teams_in_competition(api_key, competition_id):
    url = f"https://api.football-data.org/v4/competitions/{competition_id}/teams"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for team in response.json().get('teams', []):
            print(f"ID: {team['id']}, Name: {team['name']}")
    else:
        print('Failed to fetch teams')


list_teams_in_competition(api_key, competition_id)

# ID: 81, Name: FC Barcelona