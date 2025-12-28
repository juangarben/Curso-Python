"""
    Clase	Atributos principales	                                Métodos principales
    Vuelo	número, origen, destino, fecha, asientos_disponibles	mostrar_info(), reservar_asiento()
    Pasajero	nombre, documento, email	                        mostrar_info()
    Reserva	    pasajero, vuelo, asiento	                        mostrar_reserva()
    Aerolinea	nombre, vuelos[], reservas[]	                    agregar_vuelo(), crear_reserva(), mostrar_reservas()

"""
    
import json
from datetime import datetime

class Vuelo:
    def __init__(self,numero,origen,destino,fecha):
        self.numero=numero
        self.origen=origen
        self.destino=destino
        self.fecha=fecha
        self.asientos_disponibles=["A1","A2","A3","A4","A5"]
        self.asientos_reservados=list()
    
    def mostrar_info(self):
        print(f"####################################################\nVuelo Numero:{self.numero}\tOrigen:{self.origen}\tDestino:{self.destino}\nFecha:{self.fecha}\n####################################################")
        print(f"\nAsientos disponibles:\n")
        self.__mostrar_asientos_disponibles()
        print(f"\nAsientos reservados:\n")
        self.__mostrar_asientos_reservados()
    
    def __mostrar_asientos_disponibles(self):
        for asiento in self.asientos_disponibles:
            print(asiento)
            
    def __mostrar_asientos_reservados(self):
        for asiento in self.asientos_reservados:
            print(asiento)
                
    def reservar_asiento(self,numero_asiento:str) -> bool:
        
        if numero_asiento in self.asientos_disponibles:
            self.asientos_reservados.append(numero_asiento)
            self.asientos_disponibles.remove(numero_asiento)
            return True
        
        return False
            

class Pasajero:
    def __init__(self,nombre,ID,email):
        self.nombre=nombre
        self.ID=ID
        self.email=email
    
    def mostrar_info(self):
        print(f"\n======================================================\nNombre:{self.nombre}\tID:{self.ID}\temail:{self.email}\n======================================================\n")

class Reserva:
    
    def __init__(self,pasajero: Pasajero,vuelo: Vuelo,asiento):
        self.pasajero=pasajero
        self.vuelo=vuelo
        self.asiento=asiento
        
    
    def mostrar_info(self):
        
        if self.vuelo.reservar_asiento(self.asiento):
            print(f"Reserva realizada con éxito en el asiento: {self.asiento}\n")
            self.vuelo.mostrar_info()
        else:
            print("No ha sido posible realizar la reserva")
            
        
class Aerolinea:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.vuelos=list()
        self.reservas=list()
        
    def agregar_vuelo(self,vuelo:Vuelo):
        self.vuelos.append(vuelo)

    def agregar_reserva(self,reserva: Reserva):
        self.reservas.append(reserva)
    
    def mostrar_info(self):
        for vuelo in self.vuelos:
            vuelo.mostrar_info()
        
        for reserva in self.reservas:
            reserva.mostrar_info()
    
    #########################################################
    
#MEJORAS:
#Añadir asientos (disponibles como atributo para la clase vuelo)
#Menu 
#JSON

pasajero1=Pasajero("Juan",1,"juanito@gmail.com")
pasajero1.mostrar_info()
vuelo1=Vuelo(1,"Valencia","Londres","29-12-2025")
reserva1=Reserva(pasajero1,vuelo1,"A2")
a1=Aerolinea("RAYANAIR")    
a1.agregar_vuelo(vuelo1)
a1.agregar_reserva(reserva1)
a1.mostrar_info()
    