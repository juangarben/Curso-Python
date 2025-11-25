"""
MÓDULO: 

Es un archivo con extensión .py, .pvc (Python compilado) o un archivo escrito en C para CPython que posee su propio espacio de nombres
y que puede contener variables, funciones, clases e incluso otros módulos en su interior

Utilidad: Modularización y reutilización de código en distintas aplicaciones

PAQUETE:

- Carpetas donde se almacenarán módulos relacionados entre sí
- Sirven para organizar y reutilizar módulos
- En Python los paquetes se crean con un archivo __init__.py dentro de la carpeta donde tenemos los módulos que queremos usar en distintas carpetas
"""

from modulo_vehiculos import *

miVehiculo=Vehiculo("Mazda","MX5")
miVehiculo.estado()