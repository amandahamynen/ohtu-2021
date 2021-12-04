class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def get_score_names(self, score_number):
        score_names = {0: "Love", 
                       1: "Fifteen", 
                       2: "Thirty", 
                       3: "Forty"}
        return score_names[score_number]

    def won_point(self, player_name):
        if self.player1_name == player_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def winning(self):
        if self.m_score1 > self.m_score2:
            return self.player1_name
        else:
            return self.player2_name
    
    def answer(self, situation):
        if situation == 0:
            if self.m_score1 < 4:
                score_name = self.get_score_names(self.m_score1)
                return f"{score_name}-All"
            else:
                return "Deuce"

        else:
            if max(self.m_score1, self.m_score2) < 4:
                player1_score_name = self.get_score_names(self.m_score1)
                player2_score_name = self.get_score_names(self.m_score2)
                return f"{player1_score_name}-{player2_score_name}"
            elif situation == 1:
                winning = self.winning()
                return f"Advantage {winning}"
            else:
                winning = self.winning()
                return f"Win for {winning}"       

    def get_score(self):
        situation = abs(self.m_score1 - self.m_score2)
        return self.answer(situation)