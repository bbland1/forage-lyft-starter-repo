from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires_wear_sensors):
        self._tires_wear_sensors = tires_wear_sensors

    def needs_service(self) -> bool:
        if any(wear_value < 0 or wear_value > 1 for wear_value in self._tires_wear_sensors):
            raise ValueError(
                "Check the tire sensor, one of the values was outside of the possible range.")

        if any(wear_value >= 0.9 for wear_value in self._tires_wear_sensors):
            return True
        else:
            return False
