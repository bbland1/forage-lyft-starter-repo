import unittest
from datetime import date

from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

factory = CarFactory()


class TestCarFactory(unittest.TestCase):
    def test_creating_calliope(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tire_wear_sensor = [0.9, 0.1, 0.2, 0.5]

        calliope = factory.create_calliope(
            current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertIsInstance(calliope._engine, CapuletEngine)
        self.assertEqual(calliope._engine._current_mileage, current_mileage)
        self.assertEqual(calliope._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(calliope._battery, SpindlerBattery)
        self.assertEqual(calliope._battery._last_service_date,
                        last_service_date)
        self.assertEqual(calliope._battery._current_date, current_date)

        self.assertIsInstance(calliope._tire, CarriganTire)
        self.assertEqual(calliope._tire._tire_wear_sensors, tire_wear_sensor)

        self.assertTrue(calliope.needs_service())

    def test_creating_glissade(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tire_wear_sensor = [0.9, 0.1, 0.2, 0.5]

        glissade = factory.create_glissade(
            current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertIsInstance(glissade._engine, WilloughbyEngine)
        self.assertEqual(glissade._engine._current_mileage, current_mileage)
        self.assertEqual(glissade._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(glissade._battery, SpindlerBattery)
        self.assertEqual(glissade._battery._last_service_date,
                        last_service_date)
        self.assertEqual(glissade._battery._current_date, current_date)


        self.assertIsInstance(glissade._tire, OctoprimeTire)
        self.assertEqual(glissade._tire._tire_wear_sensors, tire_wear_sensor)

        self.assertTrue(glissade.needs_service())

    def test_creating_palindrome(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        warning_indicator_on = False
        tire_wear_sensor = [0.9, 0.1, 0.2, 0.5]

        palindrome = factory.create_palindrome(
            current_date, last_service_date, warning_indicator_on)

        self.assertIsInstance(palindrome._engine, SternmanEngine)
        self.assertEqual(palindrome._engine._warning_indicator_on, warning_indicator_on)

        self.assertIsInstance(palindrome._battery, SpindlerBattery)
        self.assertEqual(palindrome._battery._last_service_date,
                        last_service_date)
        self.assertEqual(palindrome._battery._current_date, current_date)


        self.assertIsInstance(palindrome._tire, CarriganTire)
        self.assertEqual(palindrome._tire._tire_wear_sensors, tire_wear_sensor)

        self.assertTrue(palindrome.needs_service())

    def test_creating_rorschach(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 2).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tire_wear_sensor = [0.9, 0.1, 0.2, 0.5]

        rorschach = factory.create_rorschach(
            current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertIsInstance(rorschach._engine, WilloughbyEngine)
        self.assertEqual(rorschach._engine._current_mileage, current_mileage)
        self.assertEqual(rorschach._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(rorschach._battery, NubbinBattery)
        self.assertEqual(rorschach._battery._last_service_date,
                        last_service_date)
        self.assertEqual(rorschach._battery._current_date, current_date)

        self.assertIsInstance(rorschach._tire, OctoprimeTire)
        self.assertEqual(rorschach._tire._tire_wear_sensors, tire_wear_sensor)

        self.assertFalse(rorschach.needs_service())

    def test_creating_thovex(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 2).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tire_wear_sensor = [0.9, 0.1, 0.2, 0.5]

        thovex = factory.create_thovex(
            current_date, last_service_date, current_mileage, last_service_mileage)

        self.assertIsInstance(thovex._engine, CapuletEngine)
        self.assertEqual(thovex._engine._current_mileage, current_mileage)
        self.assertEqual(thovex._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(thovex._battery, NubbinBattery)
        self.assertEqual(thovex._battery._last_service_date,
                        last_service_date)
        self.assertEqual(thovex._battery._current_date, current_date)


        self.assertIsInstance(thovex._tire, CarriganTire)
        self.assertEqual(thovex._tire._tire_wear_sensors, tire_wear_sensor)

        self.assertFalse(thovex.needs_service())
