from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=500.0)

    def win(self):
        self.wins += 1
        self.advantage += 145
