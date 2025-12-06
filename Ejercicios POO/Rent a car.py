"""
Programa en POO que simula una agencia de alquier de coches

"""
from Modulo_Menu import Menu
from datetime import datetime,date
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
        self.historial_rentals=[]
    
    def add_rental(self,rental):
        
        self.historial_rentals.append(rental)
        
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
        self.vehiculo.km+=self.km
        self.vehiculo.disponibilidad=True
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
        
        try:
            self.fecha_inicio=datetime.strptime(fecha_inicio, '%d-%m-%Y')
            self.fecha_fin=datetime.strptime(fecha_fin, '%d-%m-%Y')
            cliente=next(c for c in self.lista_clientes if c.dni==dni)
            vehiculo=next(v for v in self.lista_vehiculos if v.matricula==matricula)
            self.lista_rentals.append(Rental(cliente,vehiculo,self.fecha_inicio,self.fecha_fin))
            vehiculo.disponibilidad=False
            print("Alquiler realizado correctamente")
        except:
            print("Error: No ha sido posible realizar el alquiler, datos incorrectos")
        
    def terminar_rental(self,rental,km):
        
        self.rental=rental
        self.km=km
        self.rental.terminar_rental(self.km)
        self.lista_rentals=[r for r in self.lista_rentals if r!=self.rental]
        
    def listar_vehiculos(self): 
        
        print(f"\n_______________ Vehiculos disponibles _________________\n")
        
        for vehiculo in self.lista_vehiculos:
            if vehiculo.disponibilidad:
                print(vehiculo)
        
        print(f"\n_______________ Vehiculos alquilados _________________\n")
        
        for vehiculo in self.lista_vehiculos:
            if not vehiculo.disponibilidad:
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
                
                try:
                    marca=input("Indica la marca: ")
                    modelo=input("Indica el modelo: ")
                    matricula=input("indica la matricula: ")
                    km=int(input("Indica los km: "))
                    precio_dia=float(input("Indica el precio por dia: "))
                    
                    miAgencia.add_vehiculos(Vehiculo(marca,modelo,matricula,km,precio_dia))
                except:
                    print("Error: Los datos introducidos son incorrectos")
                
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
                dni=input("Introduce el DNI del cliente: ")
                matricula=input("Introduce la matricula: ")
                fecha_inicio=input("Introduce la fecha de inicio: ")
                fecha_fin=input("Introduce la fecha de fin: ")
                miAgencia.add_rental(dni,matricula,fecha_inicio,fecha_fin) 
                input("Presiona Enter para continuar...")
                
            
            elif opcion_elegida==6: #Devolver vehiculo
                
                dni=input("Introduce el DNI del cliente: ")
                matricula=input("Introduce la matricula: ")
                
                try:
                    km=int(input("Indica los km: "))
                    cliente=next(c for c in miAgencia.lista_clientes if c.dni==dni)
                    vehiculo=next(v for v in miAgencia.lista_vehiculos if v.matricula==matricula)
                    miRental=next(r for r in miAgencia.lista_rentals if r.cliente==cliente and r.vehiculo==vehiculo)
                    miAgencia.terminar_rental(miRental,km)
                    print(f"Devolución del vehiculo {vehiculo} realizada correctamente")
                    
                except:
                    print("Error: Los datos introducidos son incorrectos")
                
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

"""Errores test:

Indicar el coste del alquiler cuando se alquila


"""

        
        
    