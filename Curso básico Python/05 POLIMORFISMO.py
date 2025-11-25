"""
POLIMORFISMO:
    - Un objeto cambia de forma (comportamiento) según el contexto en el que se utilice
    - En Python se usa de forma sencilla al ser un lenguaje de tipado dinámico
"""
class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")
        
class Camion():
    
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

########### POLIMORFISMO ##################

def desplazamiento_vehiculo(vehiculo): # Función donde el parametro vehiculo es un objeto general (puede pertener a cualquier clase
    vehiculo.desplazamiento() #aquí llamamos al método desplazamiento del objeto vehiculo que será el correspondiente al de la clase del objeto vehículo que le pasamos como parámetro a la función


miVehiculo=Moto()
desplazamiento_vehiculo(miVehiculo) #llamamos a la función de polimorfismo y ahora es una Moto

miVehiculo=Coche()
desplazamiento_vehiculo(miVehiculo) #llamamos a la función de polimorfismo y ahora es un Coche
    
miVehiculo=Camion()
desplazamiento_vehiculo(miVehiculo) #llamamos a la función de polimorfismo y ahora es un Camion



