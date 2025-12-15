"""POO que simula la gestión de un hotel
"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os

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
        return f"\nHabitación {self.tipo} nº {self.numero}\n"

class Cliente:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.numero_habitacion=0
        self.pension="AD" #puede ser AD,MP,PC
        self.fecha_entrada=""
        self.fecha_salida=""
    
    
        
    def __str__(self):
        return f"\nNombre del cliente: {self.nombre}\tNº hab:{self.numero_habitacion}\t{self.pension}\tfecha_entrada:{self.fecha_entrada}\tfecha salida:{self.fecha_salida}\n"

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
        
        if not buscar_cliente(self.lista_clientes,"nombre",nombre):
        #if not next((c for c in self.lista_clientes if c.nombre==nombre),None):
            self.lista_clientes.append(Cliente(nombre))
            #asignar habitación
            print("Cliente registrado correctamente")
        else:
            print("Error: El cliente ya está registrado")
            
    def cancelar_reserva(self):
        pass
    
    def asignar_habitacion(self,tipo_hab):
        #el método devuelve la habitación asignada
        habitacion=next(h for h in self.lista_habitaciones if h.tipo==tipo_hab and h.estado=="libre")
        if habitacion !=None:
            print(f"La habitación nº{habitacion.numero} ha sido reservada")
            
        
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
        
        habitacion=next((h for h in self.lista_habitaciones if h.numero==numero),None)
        if habitacion!=None:
            habitacion.estado="libre"
            return True
        return False
            
    def agregar_hab(self,habitacion):
        
        if not next((h for h in self.lista_habitaciones if h.numero==habitacion.numero),None):
            self.lista_habitaciones.append(habitacion)
            return True
        
        print("Error habitación existente")
        return False
    
    def eliminar_hab(self,habitacion):
        
        if next((h for h in self.lista_habitaciones if h.numero==habitacion.numero),None):
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

def buscar_cliente(lista,dato,valor):
    
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
    
        
    

# lista_clientes=[Cliente("juan"),Cliente("perico"),Cliente("andres")]
# resultado=buscar_cliente(lista_clientes,"numero_habitacion",0)
# print(f"{resultado[0]}-{resultado[1]}")




# miHabitacion=Habitacion(1,"idsndividual")
# print(miHabitacion)