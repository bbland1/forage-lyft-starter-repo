import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTire(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        tire = CarriganTires(tires_wear_sensors=[0.1, 0.5, 0.9, 0.4])
        self.assertTrue(tire.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        tire = CarriganTires(tires_wear_sensors=[0.1, 0.1, 0.1, 0.1])
        self.assertFalse(tire.needs_service())

    def test_value_issue_error(self):
        with self.assertRaises(ValueError):
            tire = CarriganTires(tires_wear_sensors=[1, 0, 2, 0.5])
            tire.needs_service()


class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime__should_be_serviced(self):
        tire = OctoprimeTires(tires_wear_sensors=[1, 0.9, 0.9, 0.4])
        self.assertTrue(tire.needs_service())

    def test_octoprime__should_not_be_serviced(self):
        tire = OctoprimeTires(tires_wear_sensors=[0.1, 0.1, 0.1, 0.1])
        self.assertFalse(tire.needs_service())

    def test_value_issue_error(self):
        with self.assertRaises(ValueError):
            tire = OctoprimeTires(tires_wear_sensors=[1, 0, 2, 0.5])
            tire.needs_service()


if __name__ == '__main__':
    unittest.main()
