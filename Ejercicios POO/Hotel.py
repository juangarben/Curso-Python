"""POO que simula la gestión de un hotel
"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os


class Cliente:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.numero_habitacion=0
        self.pension="AD" #puede ser AD,MP,PC
        self.fecha_entrada=""
        self.fecha_salida=""
    
    
        
    def __str__(self):
        return f"\nCliente: {self.nombre:<10}\tNº hab:{self.numero_habitacion}\t{self.pension}\tfecha_entrada:{self.fecha_entrada}\tfecha salida:{self.fecha_salida}\n"
    
class Habitacion:
    def __init__(self,numero,tipo,precio):
        
        self.numero=numero
        self.estado="libre" #puede ser "libre" u "ocupada"
        self.precio=precio
        
        if self.validar_tipo(tipo):
            self.tipo=tipo #puede ser individual,doble,suit
        else:
            self.tipo="doble"
    
    def validar_tipo(self,tipo):
        tipo=tipo.lower()
        if tipo=="individual" or tipo=="doble" or tipo=="suite":
            return True
        return False
    
    def __str__(self):
        return f"Habitación {self.tipo}\tnº {self.numero}\t{self.precio}€/noche\t{self.estado}\n"



class Hotel:
    def __init__(self,nombre):
        
        self.nombre=nombre
        self.lista_habitaciones=[]
        self.lista_clientes=[]
    
    def listar_habitaciones(self):
        for habitacion in self.lista_habitaciones:
            print(habitacion)
            
    def listar_clientes(self):
        for cliente in self.lista_clientes:
            print(cliente)
            
    
    def resevar_habitacion(self,nombre,tipo_hab):
        
        cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)[0]
        habitacion=self.asignar_habitacion(tipo_hab)
        if habitacion!=None:
            if cliente==None:
                
                miCliente=Cliente(nombre)
                miCliente.numero_habitacion=habitacion.numero
                self.lista_clientes.append(miCliente)
                
            else:
                print("Error cliente ya registrado en el hotel")
        else:
            print("Error no hay habitaciones disponibles")
   
            
    def cancelar_reserva(self):
        pass
    
    def asignar_habitacion(self,tipo_hab):
        #el método devuelve la habitación asignada
        habitacion=next((h for h in self.lista_habitaciones if h.tipo==tipo_hab and h.estado=="libre"),None)
        if habitacion !=None:
            habitacion.estado="reservada"
            print(f"La habitación nº{habitacion.numero} ha sido reservada")
            return habitacion
        return None
            
        
    def checkin(self,nombre):
        
        #registra la fecha de entrada y el tipo de pensión
        while True:
            try:
                fecha_entrada=input("Introduce la fecha de entrada (d-m-a): ")
                break
            except:
                print("Formato de fecha incorrecto. Inténtalo de nuevo")
                
        fecha_entrada=datetime.strptime(fecha_entrada, '%d-%m-%Y')
        pass
    
    def checkout(self,nombre):
        #registra la fecha de salida y el tipo de pensión
        #Genera la factura
        pass
    
    def liberar_habitacion(self,numero):
        
        habitacion=buscar_objeto(self.lista_habitaciones,"numero",numero)[0]
        #habitacion=next((h for h in self.lista_habitaciones if h.numero==numero),None)
        if habitacion!=None:
            habitacion.estado="libre"
            return True
        return False
            
    def agregar_hab(self,habitacion):
        
        if not buscar_objeto(self.lista_habitaciones,"numero",habitacion.numero)[1]:
        #if not next((h for h in self.lista_habitaciones if h.numero==habitacion.numero),None):
            self.lista_habitaciones.append(habitacion)
            return True
        
        print("Error no se ha podido añadir la habitación al hotel")
        return False
    
    def eliminar_hab(self,habitacion):
        
        if buscar_objeto(self.lista_habitaciones,"numero",habitacion.numero)[1]:
        #if next((h for h in self.lista_habitaciones if h.numero==habitacion.numero),None):
            self.lista_habitaciones.remove(habitacion)
            return True
        
        print("Error la habitación no existe")
        return False
        
            
    def Facturar(self,cliente):
        # Precio por hab/noche AD + 10%MP + 20%PC
        # Devuelve el importe de la factura
        pass        
    
        

class Ejecutable:
    pass

####################################################

def buscar_objeto(lista,dato,valor):
    
    try:
        
        objeto = next(
            (item for item in lista if getattr(item, dato) == valor),
            None
        )
    
    except:
        return None,False
        
    if objeto!=None:
        return objeto,True
    
    return None,False
    
        
#########################################################


miHotel=Hotel("Juanito's empire")
miHotel.agregar_hab(Habitacion(1,"doble",50))
miHotel.agregar_hab(Habitacion(2,"suite",100))
miHotel.agregar_hab(Habitacion(3,"individual",30))
miHotel.agregar_hab(Habitacion(4,"doble",50))
miHotel.agregar_hab(Habitacion(5,"suite",100))
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("juan","suite")
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("perico","doble")
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("andres","individual")
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("maria","suite")
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("eva","doble")
miHotel.listar_habitaciones()

miHotel.resevar_habitacion("ester","doble")
miHotel.listar_habitaciones()
miHotel.listar_clientes()

