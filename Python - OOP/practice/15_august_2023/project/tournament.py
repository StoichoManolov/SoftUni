from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    VALID_TEAMS = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):

        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type):

        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")

        equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):

        equipment = self.get_equip(equipment_type)
        team = self.get_team(team_name)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        team = self.get_team(team_name)

        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        equipment = [eq.increase_price() for eq in self.equipment if eq.TYPE == equipment_type]

        return f"Successfully changed {len(equipment)}pcs of equipment."

    def play(self, team_name1, team_name2):

        team1 = self.get_team(team_name1)
        team2 = self.get_team(team_name2)

        if not team1.__class__.__name__ == team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.sum_points()
        team2_points = team2.sum_points()

        if team1_points == team2_points:
            return "No winner in this game."
        elif team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        else:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)

        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]

        [result.append(t.get_statistics()) for t in sorted_teams]

        return '\n'.join(result)

    def get_equip(self, equipment_type: str):

        equipment = [eq for eq in self.equipment if eq.TYPE == equipment_type]
        return equipment[-1] if equipment else None

    def get_team(self, team_name: str):

        team = [t for t in self.teams if t.name == team_name]
        return team[0] if team else None

