import unittest
from home import SmartHome
from Devices.light import Light

class TestSmartHome(unittest.TestCase):
    
    def test_add_device(self):
        home=SmartHome()
        home.add_device(Light("Luz"))
        self.assertEqual(len(home.get_status()),1)