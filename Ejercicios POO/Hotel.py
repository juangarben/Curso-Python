"""POO que simula la gestión de un hotel
"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os,math

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
        self.estado="libre" #puede ser "libre" o "reservada"
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
    
    def agregar_hab(self,habitacion):
        
        if not buscar_objeto(self.lista_habitaciones,"numero",habitacion.numero)[1]:
       
            self.lista_habitaciones.append(habitacion)
            return True
        
        print("Error no se ha podido añadir la habitación al hotel")
        return False
    
    def eliminar_hab(self,numero):
        
        try:
            habitacion=buscar_objeto(self.lista_habitaciones,"numero",numero)[0]
            if habitacion.estado!="reservada":
                self.lista_habitaciones.remove(habitacion)
                return True
        except: 
            pass
            
        print("Error: la habitación no existe o está reservada")
        return False
        
    
    def resevar_habitacion(self,nombre,tipo_hab):
        
        cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)[0]
        habitacion=self.asignar_habitacion(tipo_hab)
        if habitacion!=None:
            if cliente==None:
                
                miCliente=Cliente(nombre)
                miCliente.numero_habitacion=habitacion.numero
                self.lista_clientes.append(miCliente)
                return True
                
            print("Error: cliente ya registrado en el hotel")
            return False
        
        print("Error: no hay habitaciones disponibles")
        return False
       
    def cancelar_reserva(self,nombre):
        
        try:
            cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)[0]
            
            if cliente.fecha_entrada=="": #No se puede cancelar la reserva si hay un checkin hecho
            
                if self.liberar_habitacion(cliente.numero_habitacion):    
                    self.lista_clientes.remove(cliente)
                    print(f"La reserva a nombre de {cliente.nombre} se ha cancelado correctamente")
                    return True
            else:
                print("Error: No se puede cancelar la reserva porque ya hay un check-in")
        except:
            
            print("Error: No ha sido posible cancelar la reserva")
            return False
        
    
    def asignar_habitacion(self,tipo_hab):
        
        habitacion=next((h for h in self.lista_habitaciones if h.tipo==tipo_hab and h.estado=="libre"),None)
        if habitacion !=None:
            habitacion.estado="reservada"
            print(f"La habitación nº{habitacion.numero} ha sido reservada")
            return habitacion
        return None
    
    
    def liberar_habitacion(self,numero):
        
        habitacion=buscar_objeto(self.lista_habitaciones,"numero",numero)[0]
       
        if habitacion!=None:
            habitacion.estado="libre"
            return True
        return False
        
    def checkin(self,nombre):
        
        while True:
            
            cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)
            
            if cliente[1]:
                
                if cliente[0].fecha_entrada=="":
                    while True:
                        
                        try:
                            
                            fecha_entrada=input("Introduce la fecha de entrada (d-m-a): ")
                            fecha_entrada=datetime.strptime(fecha_entrada, '%d-%m-%Y')
                            break
                            
                        except:
                            print("Formato de fecha incorrecto. Inténtalo de nuevo")
                    
                    pension=input("Introduce el tipo de pensión (AD,MP,PC): ")
                    
                    while True:    
                    
                        if pension.lower()=="ad" or pension.lower()=="mp" or pension.lower()=="pc":
                            
                            cliente[0].pension=pension
                            cliente[0].fecha_entrada=fecha_entrada
                            print(f"Checkin a nombre de {cliente[0].nombre} realizado correctamente")
                            return True
                            
                        else:
                            print("Error: Tipo de pensión incorrecto. Inténtalo de nuevo")
                            
                else:
                    print(f"Error: El cliente {nombre} ya tiene un check-in hecho ")
                    return False
            
            else:
                print(f"Error: El cliente {nombre} no tiene una habitación reservada")
                return False
                
    
    def checkout(self,nombre):
        
        while True:
            
            cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)
            
            if cliente[1]:
                
                if cliente[0].fecha_entrada!="":
                    while True:
                        
                        try:
                            
                            fecha_salida=input("Introduce la fecha de entrada (d-m-a): ")
                            fecha_salida=datetime.strptime(fecha_salida, '%d-%m-%Y')
                            
                            if fecha_salida <= cliente[0].fecha_entrada:
                                print("Error: La fecha de salida debe ser posterior a la de entrada")
                                return False
                            
                            else:
                
                                cliente[0].fecha_salida=fecha_salida
                                noches = (cliente[0].fecha_salida - cliente[0].fecha_entrada).days
                            
                                print(f"Alojamiento de {noches} noches")
                                self.liberar_habitacion(cliente[0].numero_habitacion)                        
                                factura=self.Facturar(cliente[0].nombre,noches) #Si el checkout se ha realizado correctamente se genera la factura
                                self.lista_clientes.remove(cliente[0])
                                print(f"Checkout a nombre de {cliente[0].nombre} realizado correctamente\nTotal factura={factura}€\n")
                                return True
                                                        
                        except:
                            print("Formato de fecha incorrecto. Inténtalo de nuevo")
                                        
                else:
                    print(f"Error: El cliente {nombre} no tiene un check-in hecho ")
                    return False
            
            else:
                print(f"Error: El cliente {nombre} no tiene una habitación reservada")
                return False        
                
    def Facturar(self,nombre,noches):
        
        # Devuelve el importe de la factura
        
        cliente=buscar_objeto(self.lista_clientes,"nombre",nombre)
        
        if cliente[1]:
            pension=cliente[0].pension.lower()
            habitacion=buscar_objeto(self.lista_habitaciones,"numero",cliente[0].numero_habitacion)
            
            if habitacion[1]: # Precio por hab/noche AD + 10%MP + 20%PC
                total=habitacion[0].precio*noches
                if pension=="mp":
                    total*=1.10
                    total=round(total,3)
                    return total
                elif pension=="pc":
                    total*=1.20
                    total=round(total,3)
                    return total
                else:
                    total=round(total,3)
                    return total
                    
            else:
                print("Error: Habitación no encontrada")
                return 0
        else:
            print("Error: Cliente no encontrado")
            return 0
                
    
class Ejecutable:
    
    def __init__(self):
        
        miHotel=Hotel("Juanito's empire")
        
        lista_menu=[
                    "Listar habitaciones",
                    "Actualizar habitaciones",
                    "Listar clientes",
                    "Actualizar reserva",
                    "Actualizar check",
                    ]
        
        salir=False
    
        while not salir:
            os.system('cls')
            opcion_elegida=Menu(f"HOTEL {miHotel.nombre}",lista_menu).crear_menu()
        
            if opcion_elegida == 1: #Listar habitaciones
                
                miHotel.listar_habitaciones()
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida == 2: #Actualizar habitaciones
                while True:
                    try:
                        opcion=int(input(f"1. Añadir habitación\n2. Eliminar habitación\n3. Salir\n"))
                        if opcion>=1 and opcion<=3:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1:
                    
                    while True:
                        try:
                            numero=int(input(f"Introduce el número de habitación: "))
                            tipo=int(input(f"Introduce el número de habitación:\n1.individual\n2.doble\n3.suite\n"))
                            
                            if tipo==1:
                                tipo_habitacion="individual"
                            elif tipo==2:
                                tipo_habitacion="doble"
                            elif tipo==3:
                                tipo_habitacion="suite"
                                
                            precio=float(input(f"Introduce el precio por noche: "))
                            
                            if miHotel.agregar_hab(Habitacion(numero,tipo_habitacion,precio)):
                                print(f"La habitación nº {numero} se ha añadido correctamente")
                           
                            break
                            
                        except:
                            print("Error: El dato introducido no es correcto")
        
            
                elif opcion==2:
                    
                    while True:
                        
                        try:
                            numero=int(input(f"Introduce el número de habitación: "))
                            
                            if miHotel.eliminar_hab(numero):
                                print(f"La habitación nº {numero} se ha eliminado correctamente")
                            else:
                                print(f"Error: No ha sido posido eliminar la habitación {numero}")
                            break
                        
                        except:
                            print("Opción incorrecta")
                    
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 3: #Listar clientes
                       
                miHotel.listar_clientes()
                
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 4: #Actualizar reserva
                
                while True:
                    
                    try:
                        
                        opcion=int(input(f"1. Añadir reserva\n2. Cancelar reserva\n3. Salir\n"))
                        
                        if opcion>=1 and opcion<=3:
                            break
                        input("Opción incorrecta")
                    
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1:
                    
                    while True:
                    
                        try:
                            
                            nombre=input(f"Introduce el nombre del cliente: ")
                            tipo=int(input(f"Introduce el número de habitación:\n1.individual\n2.doble\n3.suite\n"))
                            
                            if tipo==1:
                                tipo_habitacion="individual"
                            elif tipo==2:
                                tipo_habitacion="doble"
                            elif tipo==3:
                                tipo_habitacion="suite"
                                
                            if miHotel.resevar_habitacion(nombre,tipo_habitacion):
                                print(f"La reserva a nombre de {nombre} se ha realizado correctamente")
                            
                            break
                        
                        except:
                            print("Error: No ha sido posible realizar la reserva. Inténtalo de nuevo")
        
            
                elif opcion==2:
                    
                    nombre=input(f"Introduce el nombre del cliente: ")
                    miHotel.cancelar_reserva(nombre)
                    
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 5: #Actualizar check
                
                while True:
                    
                    try:
                        opcion=int(input(f"1. Check-in\n2. Check-out\n3. Salir\n"))
                        
                        if opcion>=1 and opcion<=3:
                            break
                       
                        input("Opción incorrecta")
                  
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1: #check-in
                    
                    nombre=input(f"Introduce nombre del cliente: ")
                    miHotel.checkin(nombre)
                                            
                elif opcion==2: #check-out
                    nombre=input(f"Introduce nombre del cliente: ")
                    miHotel.checkout(nombre)
                    
                input("Presiona Enter para continuar...")
                                  
            else:
                salir=True
    

#########################################################

def buscar_objeto(lista,dato,valor):
    
    #Función que recibe una lista de objetos, el dato sería el atributo del objeto y el valor a buscar
    #Devuelve el objeto buscado y el bool del resultado de la búsqueda
    
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

Ejecutable()


