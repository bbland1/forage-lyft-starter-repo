from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_wear_sensors: list[float]):
        self._tires_wear_sensors = tires_wear_sensors

    def needs_service(self) -> bool:
        if all(0 <= wear_value <= 1 for wear_value in self._tires_wear_sensors):
            wear_values_sum = sum(self._tires_wear_sensors)

            return wear_values_sum >= 3
        else:
            raise ValueError(
                "Check the tire sensor, one of the values was outside of the possible range.")
