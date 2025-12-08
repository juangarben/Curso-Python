"""
Gestión clinica Veterinaria en POO, con las siguientes especificaciones de la APP:

1. Registrar cliente
    
    Para registrar un cliente se requiere ingresar Nombre y Apellido del cliente. 
    Una vez ingresados los datos, se deben almacenar correctamente.
    
2. Agregar mascota a cliente

    Permite seleccionar un cliente existente e ingresar el Nombre de la mascota y el Tipo de animal (por ejemplo: perro, gato, pájaro). 
    Validar que los campos sean ingresados correctamente y actualizar la información del cliente con una nueva mascota.

3. Listar todos los clientes con sus mascotas

    Muestra en pantalla la lista de todos los clientes registrados y, para cada cliente, la información de sus mascotas, 
    incluyendo Nombre de la mascota y Tipo de animal.

4. Imprimir historial de visitas

    Permite seleccionar un cliente y generar un archivo de texto (.txt) con el historial de visitas de todas las mascotas asociadas a ese cliente. 
    Cada visita debe incluir la fecha y un breve resumen de la atención recibida.

5. Salir del Programa

Cada una de estas funcionalidades debe estar desarrollada en una función separada que se llame desde el programa principal. 
El programa debe continuar ejecutándose hasta que el usuario decida salir del programa.

"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os

class Clinica:
    
    def __init__(self,nombre):
        
        self.nombre=nombre
        self.lista_clientes=[]
        

    def registrar_cliente(self,cliente):
        
        self.cliente=cliente
        
        for c in self.lista_clientes:
            
            if c.nombre==self.cliente.nombre and c.apellidos==self.cliente.apellidos:
                print("Error: el cliente ya existe")
                return True
                
        self.lista_clientes.append(self.cliente)
        print("Cliente registrado correctamente")
        self.listar_clientes()
        
        
    def listar_clientes(self):
    
        for cliente in self.lista_clientes:
            print(cliente)
            
       
        
  
        
class Cliente:
    
    def __init__(self,nombre,apellidos):
    
        self.nombre=nombre
        self.apellidos=apellidos
    
    def __str__(self):
        return f"\n_______ Cliente _______\nNombre: {self.nombre}\tApellidos: {self.apellidos}\n"
        
    
        
        
    

class Mascota:
    
    def __init__(self,nombre,tipo):
        
        self.nombre=nombre
        self.tipo=tipo
    
    def comprobar_tipo(self):
        
        tipos_animales=["perro","gato","ave","conejo","reptil"]
        
        try:
            next(t for t in tipos_animales if t==self.tipo)
            return True
        except:
            print("Error: Tipo de animal incorrecto")
            return False
        

class Ejecutable:
    
    def __init__(self):
        
        miClinica=Clinica("Mis peluditos")
        
        lista_menu=["Registrar cliente","Agregar mascota a cliente","Listar clientes","Imprimir historial visitas"]
        
        salir=False
        
    
        while not salir:
            os.system('cls')
            opcion_elegida=Menu(f"Clinica Veterinaria {miClinica.nombre}",lista_menu).crear_menu()
            
            if opcion_elegida == 1: #Registrar cliente
                
                nombre=input("Introduce el nombre del cliente: ")
                apellidos=input("Introduce los apellidos del cliente: ")
                miClinica.registrar_cliente(Cliente(nombre,apellidos))
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==2: #Agregar mascota a cliente
                
                if (Mascota("Denver","perro").comprobar_tipo()):
                
                    print("Mascota agregada correctamente")
                
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==3: #Listar clientes
                
                miClinica.listar_clientes()
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida==4: # Imprimir historial visitas
                
                pass
        
            else:
                salir=True

###################################################################

Ejecutable()
    