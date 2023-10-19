import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_should_be_serviced_pass(self):
        today = date.today()
        last_service = today.replace(year=today.year - 5).replace(month=today.month - 1).replace(day=today.day - 4)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_service)
        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced_year(self):
        today = date.today()
        last_service = today.replace(year=today.year - 3).replace(month=today.month - 1).replace(day=today.day - 4)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_service)
        self.assertFalse(battery.needs_service())

    def test_nubbin_should_be_serviced_on_day_of_service(self):
        today = date.today()
        last_service = today.replace(year=today.year - 4)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_service)

        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced_month_not_passed(self):
        today = date.today()
        last_service = today.replace(year=today.year - 4).replace(month=today.month + 1)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_service)

        self.assertFalse(battery.needs_service())

    def test_nubbin_should_not_be_serviced_day_not_passed(self):
        today = date.today()
        last_service = today.replace(year=today.year - 4).replace(day=today.day + 7)
        battery = NubbinBattery(
            current_date=today, last_service_date=last_service)

        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_should_be_serviced_pass(self):
        today = date.today()
        last_service = today.replace(year=today.year - 3).replace(month=today.month - 1).replace(day=today.day - 4)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_service)
        self.assertTrue(battery.needs_service())

    def test_spindler_should_not_be_serviced_year(self):
        today = date.today()
        last_service = today.replace(year=today.year - 1).replace(month=today.month - 1).replace(day=today.day - 4)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_service)
        self.assertFalse(battery.needs_service())

    def test_spindler_should_be_serviced_on_day_of_service(self):
        today = date.today()
        last_service = today.replace(year=today.year - 3)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_service)

        self.assertTrue(battery.needs_service())

    def test_spindler_should_not_be_serviced_month_not_passed(self):
        today = date.today()
        last_service = today.replace(year=today.year - 2).replace(month=today.month + 1)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_service)

        self.assertFalse(battery.needs_service())

    def test_spindler_should_not_be_serviced_day_not_passed(self):
        today = date.today()
        last_service = today.replace(year=today.year - 2).replace(day=today.day + 7)
        battery = SpindlerBattery(
            current_date=today, last_service_date=last_service)

        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()