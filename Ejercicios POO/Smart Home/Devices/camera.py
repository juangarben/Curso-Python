from Devices.device import Device

class Camera(Device):
    def __init__(self, name):
        super().__init__(name)
        self.recording=False
    
    def start_recording(self):
        if self.is_on:
            self.recording=True
    
    def status(self):
        return {"device":self.name,
                "type":"Camera",
                "on":self.is_on,
                "recording":self.recording}