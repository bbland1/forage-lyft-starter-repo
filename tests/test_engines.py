import unittest

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=65000,
                            last_service_mileage=30000)
        self.assertTrue(engine.needs_service())

    def test_capulet_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=40000,
                            last_service_mileage=30000)
        self.assertFalse(engine.needs_service())

    def test_capulet_should_should_be_serviced_at_30000(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_should_be_serviced(self):
        engine = WilloughbyEngine(
            current_mileage=95000, last_service_mileage=30000)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        engine = WilloughbyEngine(
            current_mileage=40000, last_service_mileage=30000)
        self.assertFalse(engine.needs_service())

    def test_willoughby_should_should_be_serviced_at_30000(self):
        engine = WilloughbyEngine(
            current_mileage=60000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_should_be_serviced(self):
        engine = SternmanEngine(warning_indicator_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        engine = SternmanEngine(warning_indicator_on=False)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
