from game.components.power_ups.power_up import PowerUp
from game.utils.constants import AUTO_FIRE, AUTO_FIRE_TYPE

class AutoFire(PowerUp):
    TYPE = AUTO_FIRE_TYPE
    def __init__(self):
        super().__init__(AUTO_FIRE, AUTO_FIRE_TYPE)