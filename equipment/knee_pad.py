from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        twenty_percent_of_the_price = self.price * 0.2
        self.price += twenty_percent_of_the_price
