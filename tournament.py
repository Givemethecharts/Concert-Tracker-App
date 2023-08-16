from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    valid_equipment_types = ["KneePad", "ElbowPad"]
    valid_team_types = ["OutdoorTeam", "IndoorTeam"]
    all_team_names = []

    def __init__(self, name, capacity):
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
        if equipment_type not in Tournament.valid_equipment_types:
            raise Exception("Invalid equipment type!")
        if equipment_type == "KneePad":
            equipment = KneePad()
            self.equipment.append(equipment)
        elif equipment_type == "ElbowPad":
            equipment = ElbowPad()
            self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in Tournament.valid_team_types:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
            self.teams.append(team)
            Tournament.all_team_names.append(team_name)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)
            self.teams.append(team)
            Tournament.all_team_names.append(team_name)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        for index in range(len(self.equipment) - 1, -1, -1):
            current_equipment = self.equipment[index]
            if current_equipment.__class__.__name__ == equipment_type:
                for team in self.teams:
                    if team.name == team_name:
                        if current_equipment.price > team.budget:
                            raise Exception("Budget is not enough!")
                        else:
                            team.budget -= current_equipment.price
                            team.equipment.append(current_equipment)
                            self.equipment.remove(current_equipment)
                            return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        if team_name not in Tournament.all_team_names:
            raise Exception("No such team!")
        for team in self.teams:
            if team.name == team_name:
                if team.wins > 0:
                    raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
                else:
                    self.teams.remove(team)
                    return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):
        count_of_equipments_changed = 0
        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                count_of_equipments_changed += 1
                equipment.increase_price()
        return f"Successfully changed {count_of_equipments_changed}pcs of equipment."

    def play(self, team_name1, team_name2):
        first_team_sum = 0
        second_team_sum = 0

        global first_team, second_team
        for team in self.teams:
            if team.name == team_name1:
                first_team = team
            elif team.name == team_name2:
                second_team = team
        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        first_team_sum += first_team.advantage
        for equipment in first_team.equipment:
            first_team_sum += equipment.protection
        second_team_sum += second_team.advantage
        for equipment in second_team.equipment:
            second_team_sum += equipment.protection
        if first_team_sum > second_team_sum:
            first_team.win()
            return f"The winner is {first_team.name}."
        elif second_team_sum > first_team_sum:
            second_team.win()
            return f"The winner is {second_team.name}."
        elif first_team_sum == second_team_sum:
            return f"No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda team: team.wins, reverse=True)
        result = f"Tournament: {self.name}\n" \
                 f"Number of Teams: {len(self.teams)}\n" \
                 f"Teams:"
        for team in sorted_teams:
            result += f"\n{team.get_statistics()}"
        return result




t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))
print(t.get_statistics())
