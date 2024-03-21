import requests
from settings import BASE_URL, API_KEY


def fetch_competitions():
    """ Fetch all competitions and filter for specific leagues """
    headers = {"X-Auth-Token": API_KEY}
    response = requests.get(f"{BASE_URL}competitions", headers=headers)
    if response.status_code == 200:
        competitions = response.json()
        return competitions
    else:
        print(f"Failed to fetch competitions. Status Code: {response.status_code}")
        return None

def find_competition_ids(competitions, league_names):
    """ Find competition IDs based on league names """
    ids = {}
    for competition in competitions['competitions']:
        name = competition['name']
        if name in league_names:
            ids[name] = competition['id']
    return ids

if __name__ == "__main__":
    league_names = ["Primera Division", "Ligue 1", "Premier League", "Bundesliga", "Serie A"]
    competitions = fetch_competitions()
    if competitions:
        league_ids = find_competition_ids(competitions, league_names)
        for league, id_ in league_ids.items():
            print(f"{league}: {id_}")