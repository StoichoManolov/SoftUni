from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    BUDGET = 1000.0
    ADVANTAGE_PER_WIN = 115

    def __init__(self, name: str, country: str, advantage: int):

        super().__init__(name,country,advantage,budget=self.BUDGET)

    def win(self):

        self.advantage += self.ADVANTAGE_PER_WIN
        self.wins += 1
