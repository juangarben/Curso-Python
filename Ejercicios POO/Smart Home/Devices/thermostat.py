from Devices.device import Device

class Thermostat(Device):
    def __init__(self, name,temperature=22):
        super().__init__(name)
        self.temperature=temperature
    
    def status(self):
        return {"device":self.name,
                "type":"Thermostat",
                "on":self._is_on,
                "temperature":self.temperature}