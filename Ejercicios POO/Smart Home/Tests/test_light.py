import unittest
from Devices.light import Light
from exceptions import InvalidValueError

class TestLight(unittest.TestCase):
    
    def test_turn_on(self):
        light=Light("Test Light")
        light.turn_on()
        self.assertTrue(light.is_on)
    
    def test_brightness_valid(self):
        ligth=Light("Test Light",70)
        self.assertEqual(ligth.brightness,70)
    
    def test_brightness_invalid(self):
        with self.assertRaises(InvalidValueError):
            Light("Test Light",150)
            