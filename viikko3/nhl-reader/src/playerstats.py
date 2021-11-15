from datetime import datetime

class PlayerStats:
    def __init__(self, reader):
        self.lista = reader.get_players()
        self.palautus_lista = []

    def top_scorers_by_nationality(self, nationality):
        print(f"Players from {nationality} {datetime.now()}")
        print()
        for player in self.lista:
            if player.nationality == nationality:
                self.palautus_lista.append(player)
        return self.palautus_lista