class SmartHome:
    def __init__(self):
        self._devices=[]
        
    def add_device(self,device):
        self._devices.append(device)
    
    def turn_all_on(self):
        for d in self._devices:
            d.turn_on()
    
    def get_status(self):
        return [device.status() for device in self._devices]