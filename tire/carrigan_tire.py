from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_sensors: list[float]):
        self._tire_wear_sensor = tire_wear_sensors

    def needs_service(self) -> bool:
        if any(wear_value < 0 or wear_value > 1 for wear_value in self._tire_wear_sensor):
            raise ValueError("Check the tire sensor, one of the values was outside of the possible range.")
        
        if any(wear_value >= 0.9 for wear_value in self._tire_wear_sensor):
            return True
        else:
            return False
