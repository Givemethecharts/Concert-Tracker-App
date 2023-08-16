from abc import ABC, abstractmethod
from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class BaseTeam(ABC):
    def __init__(self, name, country, advantage, budget):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    def get_statistics(self):
        total_equipment_price = 0
        average_protection = 0
        result = f"Name: {self.name}\n" \
                 f"Country: {self.country}\n" \
                 f"Advantage: {self.advantage} points\n" \
                 f"Budget: {self.budget:.2f}EUR\n" \
                 f"Wins: {self.wins}\n"
        for equipment in self.equipment:
            total_equipment_price += equipment.price
            average_protection += equipment.protection
        if len(self.equipment) > 0:
            average_protection = round(average_protection / len(self.equipment))
        result += f"Total Equipment Price: {total_equipment_price:.2f}\n" \
                  f"Average Protection: {average_protection}"
        return result
