import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        tire = CarriganTire(tire_wear_sensors=[0.1, 0.5, 0, 0.4])
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
