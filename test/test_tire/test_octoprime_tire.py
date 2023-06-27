import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoPrimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.9,0.9,0.9,0.6]
        tire = OctoprimeTire(sensor_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0.5,0.2,0.5,0.2]
        tire = OctoprimeTire(sensor_array)
        self.assertFalse(tire.needs_service())