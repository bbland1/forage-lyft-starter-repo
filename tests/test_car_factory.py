import unittest
from datetime import date

from car_factory import CarFactory
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

factory = CarFactory()


class TestCarFactory(unittest.TestCase):
    def test_creating_calliope(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tires_wear_sensors = [0.9, 0.1, 0.2, 0.5]

        calliope = factory.create_calliope(
            current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_sensors)

        self.assertIsInstance(calliope._engine, CapuletEngine)
        self.assertEqual(calliope._engine._current_mileage, current_mileage)
        self.assertEqual(calliope._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(calliope._battery, SpindlerBattery)
        self.assertEqual(calliope._battery._last_service_date,
                        last_service_date)
        self.assertEqual(calliope._battery._current_date, current_date)

        self.assertIsInstance(calliope._tires, CarriganTires)
        self.assertEqual(calliope._tires._tires_wear_sensors, tires_wear_sensors)

        self.assertTrue(calliope.needs_service())

    def test_creating_glissade(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tires_wear_sensors = [0.9, 0.1, 0.2, 0.5]

        glissade = factory.create_glissade(
            current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_sensors)

        self.assertIsInstance(glissade._engine, WilloughbyEngine)
        self.assertEqual(glissade._engine._current_mileage, current_mileage)
        self.assertEqual(glissade._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(glissade._battery, SpindlerBattery)
        self.assertEqual(glissade._battery._last_service_date,
                        last_service_date)
        self.assertEqual(glissade._battery._current_date, current_date)

        self.assertIsInstance(glissade._tires, OctoprimeTires)
        self.assertEqual(glissade._tires._tires_wear_sensors, tires_wear_sensors)

        self.assertTrue(glissade.needs_service())

    def test_creating_palindrome(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 3).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        warning_indicator_on = False
        tires_wear_sensors = [0.9, 0.1, 0.2, 0.5]

        palindrome = factory.create_palindrome(
            current_date, last_service_date, warning_indicator_on, tires_wear_sensors)

        self.assertIsInstance(palindrome._engine, SternmanEngine)
        self.assertEqual(
            palindrome._engine._warning_indicator_on, warning_indicator_on)

        self.assertIsInstance(palindrome._battery, SpindlerBattery)
        self.assertEqual(palindrome._battery._last_service_date,
                        last_service_date)
        self.assertEqual(palindrome._battery._current_date, current_date)

        self.assertIsInstance(palindrome._tires, CarriganTires)
        self.assertEqual(palindrome._tires._tires_wear_sensors, tires_wear_sensors)

        self.assertTrue(palindrome.needs_service())

    def test_creating_rorschach(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 2).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tires_wear_sensors = [0.9, 0.1, 0.2, 0.5]

        rorschach = factory.create_rorschach(
            current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_sensors)

        self.assertIsInstance(rorschach._engine, WilloughbyEngine)
        self.assertEqual(rorschach._engine._current_mileage, current_mileage)
        self.assertEqual(rorschach._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(rorschach._battery, NubbinBattery)
        self.assertEqual(rorschach._battery._last_service_date,
                        last_service_date)
        self.assertEqual(rorschach._battery._current_date, current_date)

        self.assertIsInstance(rorschach._tires, OctoprimeTires)
        self.assertEqual(rorschach._tires._tires_wear_sensors, tires_wear_sensors)

        self.assertFalse(rorschach.needs_service())

    def test_creating_thovex(self):
        current_date = date.today()
        last_service_date = current_date.replace(year=current_date.year - 2).replace(
            month=current_date.month - 4).replace(day=current_date.day + 7)
        current_mileage = 23000
        last_service_mileage = 12450
        tires_wear_sensors = [0.8, 0.1, 0.2, 0.5]

        thovex = factory.create_thovex(
            current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_sensors)

        self.assertIsInstance(thovex._engine, CapuletEngine)
        self.assertEqual(thovex._engine._current_mileage, current_mileage)
        self.assertEqual(thovex._engine._last_service_mileage,
                        last_service_mileage)

        self.assertIsInstance(thovex._battery, NubbinBattery)
        self.assertEqual(thovex._battery._last_service_date,
                        last_service_date)
        self.assertEqual(thovex._battery._current_date, current_date)

        self.assertIsInstance(thovex._tires, CarriganTires)
        self.assertEqual(thovex._tires._tires_wear_sensors, tires_wear_sensors)

        self.assertFalse(thovex.needs_service())
