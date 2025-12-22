from Devices.light import Light
from Devices.thermostat import Thermostat
from Devices.camera import Camera
from home import SmartHome
from storage import save_state

home=SmartHome()
home.add_device(Light("luz cocina",80))
home.add_device(Thermostat("Termostato",23))
home.add_device(Camera("cámara entrada"))

home.turn_all_on()

for s in home.get_status():
    print(f"{s['device']} ({s['type']}): Encendido={s['on']}")


save_state(home)