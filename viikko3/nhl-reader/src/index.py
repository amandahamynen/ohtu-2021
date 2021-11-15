import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality']
        )

        players.append(player)
        
    players.sort(key = lambda x: x.get_score(), reverse=True)

    print(f"Players from FIN {datetime.now()}")
    print()

    for player in players:
        if player.nationality == 'FIN':
            print(player)

if __name__ == "__main__":
    main()
