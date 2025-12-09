"""
Gestión clinica Veterinaria en POO, con las siguientes especificaciones de la APP:

1. Registrar cliente --> OK
    
    Para registrar un cliente se requiere ingresar Nombre y Apellido del cliente. 
    Una vez ingresados los datos, se deben almacenar correctamente.
    
2. Agregar mascota a cliente --> OK

    Permite seleccionar un cliente existente e ingresar el Nombre de la mascota y el Tipo de animal (por ejemplo: perro, gato, pájaro). 
    Validar que los campos sean ingresados correctamente y actualizar la información del cliente con una nueva mascota.
    
3. Dar de baja mascota a cliente --> OK

4. Listar todos los clientes con sus mascotas --> OK

    Muestra en pantalla la lista de todos los clientes registrados y, para cada cliente, la información de sus mascotas, 
    incluyendo Nombre de la mascota y Tipo de animal.
    
5. Registrar visita --> OK

6. Imprimir historial de visitas --> OK

    Permite seleccionar un cliente y generar un archivo de texto (.txt) con el historial de visitas de todas las mascotas asociadas a ese cliente. 
    Cada visita debe incluir la fecha y un breve resumen de la atención recibida.

7. Salir del Programa --> OK

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
        
        
    def validar_cliente(self):
        
        if len(self.lista_clientes)>0:
            nombre=input("Introduce el nombre del cliente: ")
            apellidos=input("Introduce los apellidos del cliente: ")
              
            for indice,cliente in enumerate(self.lista_clientes,1):
                
                    if cliente.nombre==nombre and cliente.apellidos==apellidos:
                        return cliente,True
                    
                    if indice==len(self.lista_clientes):
                        print("Error: El cliente no existe")
                        return None,False
        else:
            print("Error no hay clientes registrados")
            return False

    def registrar_cliente(self,cliente):
        
        self.cliente=cliente
        
        if len(self.lista_clientes)==0:
            self.lista_clientes.append(self.cliente)
            print("Cliente registrado correctamente")
            return True
        
        for c in self.lista_clientes:
            if c.nombre==self.cliente.nombre and c.apellidos==self.cliente.apellidos:
                print("Error: el cliente ya existe")
                return False     
            
        self.lista_clientes.append(self.cliente)
        print("Cliente registrado correctamente")
        return True
        
    def listar_clientes(self):
        if len(self.lista_clientes)>0:
            for cliente in self.lista_clientes:
                print(cliente)
        else:
            print("Error no hay clientes registrados")
            
    def registrar_visita(self,cliente,mascota):
        
        self.cliente=cliente
        self.mascota=mascota
        
        if (self.cliente.validar_mascota_cliente(self.mascota.nombre,self.mascota.tipo)[1]):
    
            fecha_hora=datetime.now()
            resumen_visita=input("Introduce el resumen de la visita: ")
            visita=f"\n_______________ HISTORIAL DE VISITAS ________________\nNombre cliente: {self.cliente.nombre} {self.cliente.apellidos}\n{self.mascota}\n{fecha_hora}\nResumen visita:\n{resumen_visita}\n"
            self.cliente.historial_visitas.append(visita)
            
        else:
                     
            print("Error: Mascota no encontrada")
        
                        
class Cliente:
    
    def __init__(self,nombre,apellidos):
    
        self.nombre=nombre
        self.apellidos=apellidos
        self.lista_mascotas=[]
        self.historial_visitas=[]
        
    def validar_mascota_cliente(self,nombre,tipo):
        
        #Comprueba si el nombre y tipo pasados como parámetros
        #se encuentran en la lista de mascotas del cliente, y en ese caso devuleve el índice la lista y True, 
        #en caso contrario devuelve índice None y False
        
        for i,m in enumerate(self.lista_mascotas):
            
            if m.nombre==nombre and m.tipo==tipo:
                
                return i,True
        
        return None,False
    
    def agregar_mascota_cliente(self,mascota):
        
        self.mascota=mascota
        
        if self.mascota.comprobar_tipo() and not self.validar_mascota_cliente(self.mascota.nombre,self.mascota.tipo)[1]:
            
            self.lista_mascotas.append(self.mascota)   
            print(f"La mascota se ha añadido correctamente al cliente {self.nombre} {self.apellidos}\n")
            return True
        else:
            print("Error: La mascota no se ha podido añadir al cliente")
            return False
    
    def eliminar_mascota_cliente(self,mascota):
        
        self.mascota=mascota
        
        indice,resultado=self.validar_mascota_cliente(self.mascota.nombre,self.mascota.tipo)
        
        if resultado:
            del self.lista_mascotas[indice]
            print("Mascota eliminada correctamente")
            
        else:
            print("Error: La mascota no existe")
             
    
    def __str__(self):
        
        str="_________________________________________"
        str+=f"\nCliente Nombre: {self.nombre}\tApellidos: {self.apellidos}\n"
        for mascota in self.lista_mascotas:
            str+=f"Mascota Nombre: {mascota.nombre}\tTipo: {mascota.tipo}\n"
        str+="_________________________________________"
        return str
       

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
    
    def set_mascota(self):
        
        self.nombre=input("Introduce el nombre de la mascota: ")
        self.tipo=input("Introduce el tipo de la mascota: ")
        return self
    
    def __str__(self):
        return f"Nombre mascota: {self.nombre} Tipo: {self.tipo}"

class Ejecutable:
    
    def __init__(self):
        
        miClinica=Clinica("Mis peluditos")
        
        lista_menu=["Registrar cliente","Agregar mascota a cliente","Dar de baja mascota a cliente","Listar clientes","Registrar visita","Imprimir historial visitas"]
        
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
                
                cliente,resultado=miClinica.validar_cliente()
                
                if resultado:

                    cliente.agregar_mascota_cliente(Mascota(self,self).set_mascota())
                                        
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida==3: #Dar de baja mascota a cliente
                
                cliente,resultado=miClinica.validar_cliente()
                
                if resultado:
                    
                    cliente.eliminar_mascota_cliente(Mascota(self,self).set_mascota())
                 
                input("Presiona Enter para continuar...")
                
            elif opcion_elegida==4: #Listar clientes
                
                miClinica.listar_clientes()
                input("Presiona Enter para continuar...")
            
            
            elif opcion_elegida==5: # Registrar visita
                
                cliente,resultado=miClinica.validar_cliente()
                
                if resultado:
                 
                    miClinica.registrar_visita(cliente,Mascota(self,self).set_mascota())
                    
                input("Presiona Enter para continuar...")
                
                
            elif opcion_elegida==6: # Imprimir historial visitas
                
                cliente,resultado=miClinica.validar_cliente()
                
                if resultado:
        
                    with open(f'{cliente.nombre}_{cliente.apellidos}_historial.txt', 'w', encoding='utf-8') as fichero:
                        for v in cliente.historial_visitas:
                            fichero.write(v)
                    print(f"Se ha generado correctamente el fichero: {cliente.nombre}_{cliente.apellidos}_historial.txt")
    
                input("Presiona Enter para continuar...")
                
            else:
                salir=True

###################################################################

Ejecutable()
#MEJORAS:
#Añadir la opción de dar de baja un cliente
#Documentar


    