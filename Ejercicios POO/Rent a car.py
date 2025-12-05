"""
Programa en POO que simula una agencia de alquier de coches

"""
from Modulo_Menu import Menu
from datetime import date
import random,os

class Vehiculo:

    def __init__(self,marca,modelo,matricula,km,precio_dia):
        self.marca=marca
        self.modelo=modelo
        self.matricula=matricula
        self.km=km
        self.precio_dia=precio_dia
        self.disponibilidad=True
        
    def actualizar_km(self,km):
        self.km+=km
    
    def __str__(self):
        return f"\nMarca: {self.marca}\tModelo: {self.modelo}\tMatricula: {self.matricula}\tKm= {self.km}km\tPrecio/dia={self.precio_dia}€\n"
    
class Cliente:
    
    def __init__(self,nombre,edad,dni):
        
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.historial_retals=[]
    
    def add_rental(self,rental):
        
        self.historial_retals.append(rental)
        
    def __str__(self):
        return f"Nombre cliente: {self.nombre}\tEdad: {self.edad}años\tDNI: {self.dni}\n"
        
class Rental:
    
    def __init__(self,cliente,vehiculo,fecha_inicio,fecha_fin):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.coste_total=self.calcular_coste()
    
    def calcular_coste(self):
        dias_alquiler=(self.fecha_fin-self.fecha_inicio).days
        return dias_alquiler*self.vehiculo.precio_dia
    
    def terminar_rental(self,km):
        self.km=km
        self.vehiculo.disponibilidad=False
        self.vehiculo.km+=self.km
        self.cliente.historial_rentals.append(self)
        
    def __str__(self):
        return f"\n________ Información del rental___________\n{self.cliente}\n{self.vehiculo}\nFecha inicio: {self.fecha_inicio}\tFecha Fin: {self.fecha_fin}"
    
        
class Agencia:
    
    def __init__(self,nombre,direccion):
        
        self.nombre=nombre
        self.direccion=direccion
        self.lista_vehiculos=[]
        self.lista_clientes=[]
        self.lista_rentals=[]
    
    def add_vehiculos(self,vehiculo):
        self.vehiculo=vehiculo
        self.lista_vehiculos.append(vehiculo)
        self.vehiculo.disponibilidad=False
        
    def remove_vehiculo(self,matricula):
        
        self.matricula=matricula
        
        try:
            
            if next(vehiculo for vehiculo in self.lista_vehiculos if vehiculo.matricula!=self.matricula):
                self.lista_vehiculos=[vehiculo for vehiculo in self.lista_vehiculos if vehiculo.matricula!=self.matricula]
                print(f"Vehiculo con matricula: {self.matricula} eliminado correctamente")
        
        except:
            print("Error: Matrícula no encontrada")
        
    
    def add_customer(self,cliente):
        
        self.cliente=cliente
        self.lista_clientes.append(cliente)
        
    def remove_customer(self,dni):
        self.dni=dni
        
        try:
            if next(cliente for cliente in self.lista_clientes if cliente.dni!=self.dni):
                self.lista_clientes=[cliente for cliente in self.lista_clientes if cliente.dni!=self.dni]
                print(f"Cliente con DNI {self.dni} eliminado correctamente")
            
        except:
            print("Error: Cliente no encontrado")
        
    def add_rental(self,dni,matricula,fecha_inicio,fecha_fin):
        self.dni=dni
        self.matricula=matricula
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        cliente=next(c for c in self.lista_clientes if c.dni==dni)
        vehiculo=next(v for v in self.lista_vehiculos if v.matricula==matricula)
        self.lista_rentals.append(Rental(cliente,vehiculo,self.fecha_inicio,self.fecha_fin))
        
    def terminar_rental(self,rental,km):
        
        self.rental=rental
        self.km=km
        self.rental.terminar_rental(self.km)
        self.lista_rentals=[r for r in self.lista_rentals if r!=self.rental]
        
    def listar_vehiculos(self): 
        
        for vehiculo in self.lista_vehiculos:
            print(vehiculo)
                
    def listar_clientes(self): 
        
        for cliente in self.lista_clientes:
            print(cliente)
            
    def listar_rentals(self): 
        
        for rental in self.lista_rentals:
            print(rental)
    
    
            

class Ejecutable:
    
    def __init__(self):
        
        miAgencia=Agencia("JUANITOs RENTACAR","c/barrachina 1")
        
        lista_menu=["Dar de alta un vehiculo","Dar de baja un vehiculo","Dar de alta cliente","Dar de baja cliente","Alquilar vehiculo","Devolver vehiculo","Listar vehiculos disponibles","Listar clientes","Listar Rentals"]
        
        salir=False
        
    
        while not salir:
            os.system('cls')
            opcion_elegida=Menu(miAgencia.nombre,lista_menu).crear_menu()
            
            if opcion_elegida == 1: #Dar de alta un vehiculo
                
                marca=input("Indica la marca: ")
                modelo=input("Indica el modelo: ")
                matricula=input("indica la matricula: ")
                km=input("Indica los km: ")
                precio_dia=float(input("Indica el precio por dia: "))
                
                miAgencia.add_vehiculos(Vehiculo(marca,modelo,matricula,km,precio_dia))
                
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==2: #Dar de baja un vehiculo
                
                matricula=input("indica la matricula del vehiculo que quieres dar de baja: ")
                miAgencia.remove_vehiculo(matricula)                
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==3: #Dar de alta cliente
                nombre=input("Introduce el nombre del cliente: ")
                edad=input("Introduce la edad del cliente: ")
                dni=input("Introduce el DNI del cliente: ")
                miAgencia.add_customer(Cliente(nombre,edad,dni))
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==4: #Dar de baja cliente
                dni=input("Introduce el DNI del cliente que quieres dar de baja: ")
                miAgencia.remove_customer(dni)
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==5: #Alquilar vehiculo
                input("Presiona Enter para continuar...")
                
            
            elif opcion_elegida==6: #Devolver vehiculo
                input("Presiona Enter para continuar...")
                
            
            elif opcion_elegida==7: #Listar vehiculos disponibles
                miAgencia.listar_vehiculos()
                input("Presiona Enter para continuar...")
                
            elif opcion_elegida==8: #Listar clientes
                miAgencia.listar_clientes()
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida==9: #Listar rentals
                miAgencia.listar_rentals()
                input("Presiona Enter para continuar...")
            
            else:
                salir=True

###################################################################

Ejecutable()
        
        
        
        
        
    