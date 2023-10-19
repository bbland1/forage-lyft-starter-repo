from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensors: list[float]):
        self._tire_wear_sensor = tire_wear_sensors

    def needs_service(self) -> bool:
        if all(0 <= wear_value <= 1 for wear_value in self._tire_wear_sensor):
            wear_values_sum = sum(self._tire_wear_sensor)

            return wear_values_sum >= 0.9
        else:
            raise ValueError("Check the tire sensor, one of the values was outside of the possible range.")
