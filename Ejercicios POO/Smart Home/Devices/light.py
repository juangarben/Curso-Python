from Devices.device import Device
from exceptions import InvalidValueError

class Light(Device):
    def __init__(self, name,brightness=50):
        super().__init__(name)
        self.brightness=brightness
        
    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self,value):
        if not 0<=value<=100:
            raise InvalidValueError("Brillo fuera de rango")
        self._brightness=value
        
    def status(self):
        return {"device":self.name,
                "type":"Light",
                "on":self._is_on,
                "brightness":self._brightness}
        