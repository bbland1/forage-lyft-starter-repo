from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensors: list[float]):
        self._tire_wear_sensor = tire_wear_sensors

    def needs_service(self) -> bool:
        wear_values_sum = sum(self._tire_wear_sensor)

        return wear_values_sum >= 0.9
