from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.battery import NubbinBattery



class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine_type = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery_type = NubbinBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Willoughby", "Spindler", current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_indicator_on: bool) -> Car:
        return Car("Sternman", "Spindler", current_date, last_service_date, warning_indicator_on)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Willoughby", "Nubbin", current_date, last_service_date, current_mileage, last_service_mileage)

    def  create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car("Capulet", "Nubbin", current_date, last_service_date, current_mileage, last_service_mileage)

    