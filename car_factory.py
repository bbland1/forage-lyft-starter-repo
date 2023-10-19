from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery



class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine_type = CapuletEngine(current_mileage, last_service_mileage)
        battery_type = SpindlerBattery(current_date, last_service_date)
        return Car(engine_type, battery_type)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        battery_type = SpindlerBattery(current_date, last_service_date)
        return Car(engine_type, battery_type)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_indicator_on: bool) -> Car:
        engine_type = SternmanEngine(warning_indicator_on)
        battery_type = SpindlerBattery(current_date, last_service_date)
        return Car(engine_type, battery_type)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        battery_type = NubbinBattery(current_date, last_service_date)
        return Car(engine_type, battery_type)

    def  create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine_type = CapuletEngine(current_mileage, last_service_mileage)
        battery_type = NubbinBattery(current_date, last_service_date)
        return Car(engine_type, battery_type)

    