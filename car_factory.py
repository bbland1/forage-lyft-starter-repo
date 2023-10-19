from datetime import date
from car import Car
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery
from batteries.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_wear_sensors: list[float]) -> Car:
        engine_type = CapuletEngine(current_mileage, last_service_mileage)
        battery_type = SpindlerBattery(current_date, last_service_date)
        tires_type = CarriganTires(tires_wear_sensors)
        return Car(engine_type, battery_type, tires_type)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_wear_sensors: list[float]) -> Car:
        engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        battery_type = SpindlerBattery(current_date, last_service_date)
        tires_type = OctoprimeTires(tires_wear_sensors)
        return Car(engine_type, battery_type, tires_type)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_indicator_on: bool, tires_wear_sensors: list[float]) -> Car:
        engine_type = SternmanEngine(warning_indicator_on)
        battery_type = SpindlerBattery(current_date, last_service_date)
        tires_type = CarriganTires(tires_wear_sensors)
        return Car(engine_type, battery_type, tires_type)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_wear_sensors: list[float]) -> Car:
        engine_type = WilloughbyEngine(current_mileage, last_service_mileage)
        battery_type = NubbinBattery(current_date, last_service_date)
        tires_type = OctoprimeTires(tires_wear_sensors)
        return Car(engine_type, battery_type, tires_type)

    def  create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_wear_sensors: list[float]) -> Car:
        engine_type = CapuletEngine(current_mileage, last_service_mileage)
        battery_type = NubbinBattery(current_date, last_service_date)
        tires_type = CarriganTires(tires_wear_sensors)
        return Car(engine_type, battery_type, tires_type)
