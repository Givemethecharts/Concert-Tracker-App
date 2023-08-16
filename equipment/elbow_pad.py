from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        ten_percent_of_the_price = self.price * 0.1
        self.price += ten_percent_of_the_price
