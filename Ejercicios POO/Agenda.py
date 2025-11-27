# Nos piden realizar una agenda telefónica de contactos.

# Un contacto está definido por un nombre y un teléfono (No es necesario de validar). Un contacto es igual a otro cuando sus nombres son iguales.

# Una agenda de contactos está formada por un conjunto de contactos (Piensa en que tipo puede ser)

import os,random

os.system('cls')

class contacto:
    def __init__(self,nombre,telefono):
        self.nombre=nombre
        self.telefono=telefono
    
    def getContacto(self):
        print(f"Nombre: {self.nombre}\nTeléfono: {self.telefono}")
        
class agenda:
    def __init__(self,tamano=10):
        
        self.tamano=tamano
        self.agenda={}
    
    def aniadirContacto(self,contacto):
    
    #aniadirContacto(Contacto c): Añade un contacto a la agenda, sino se pueden meter más a la agenda se indicara por pantalla. 
    # No se pueden meter contactos que existan, es decir, no podemos duplicar nombres, aunque tengan distinto teléfono.
        
        if (self.agendaLlena()==False and self.existeContacto(contacto.nombre)):
            self.agenda[contacto.nombre]=contacto.telefono
            print(f"___________________________________________\nContacto añadido correctmante a la agenda:\nNombre: {contacto.nombre}\nTeléfono: {contacto.telefono}\n___________________________________________")
            
        elif self.existeContacto(contacto.nombre)==False:
            print("Error no se puede añadir el contacto. Duplicado!")
        
        

    def existeContacto(self,nombre_contacto):
        # existeContacto(Conctacto c): indica si el contacto pasado existe o no.
        if self.agenda.get(nombre_contacto) is None:
            return True
        else:
            return False
     
    def listarContactos(self):
    # listarContactos(): Lista toda la agenda
        print(self.agenda)

    def buscaContacto(self,nombre):
    # buscaContacto(String nombre): busca un contacto por su nombre y muestra su teléfono.
        telefono=self.agenda.get(nombre)
        
        if  telefono is None:
            
            print("Contacto no encontrado!!")
        else:
            print(f"El teléfono de {nombre} es {telefono} ")
    
    def agendaLlena(self):
    # agendaLlena(): indica si la agenda está llena.
        if (len(self.agenda))>=self.tamano:
            print("agenda llena!!")
            return True
        else:
            return False
    
    def eliminarContacto(self,nombre):
    # eliminarContacto(Contacto c): elimina el contacto de la agenda, indica si se ha eliminado o no por pantalla
       try:
           print(f"____________________________________\nContacto eliminado de la agenda:\nNombre: {nombre}\nTeléfono: {self.agenda.pop(nombre)}\n____________________________________")
       except:
           print("El contacto no exsite en la agenda, por lo tanto no se puede eliminar!")
           
    def huecosLibres(self):
    # huecosLibres(): indica cuantos contactos más podemos meter.
    
        huecos=self.tamano - len(self.agenda)
            
        print(f"Quedan {huecos} libres en la agenda para añadir contactos")
       
    
class Ejecutable:
    
    def __init__(self):
        
        os.system('cls')
        
        self.salir=False
        
        while True:
            try:
                tamano=int(input("Bienvenido al programa AGENDA. Lo primero que vamos a hacer es especificar su tamaño: "))
                self.Agenda=agenda(tamano)
                print(f"Enhorabuena!. Has creado una agenda de {tamano} huecos")
                break
            except:
                print("Error: Tamaño incorrecto")
        
        self.Menu()
        
    def refrescar(self):
        
        os.system('cls')
        self.Menu()
        
    def Menu(self):
        # Crea un menú con opciones por consola para probar todas estas funcionalidades.
        
        print("__________________________ MENU AGENDA ______________________________\n")
        print("1. Listar contactos")
        print("2. Añadir contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Consultar huecos agenda")
        print("6. Salir")
        print("______________________________________________________________________\n")
        
        while self.salir==False:
            
            try:
                
                opcion=int(input("Elige una opcion: "))
                
                if opcion>0 and opcion<7:
                        
                    if (opcion==1):#Listar contactos
                        
                        self.Agenda.listarContactos()
                                                
                        input("Presiona Enter para continuar...")
                        self.refrescar()
            
                    if (opcion==2): #Añadir contacto
                        
                        nombre_contacto=input("Introduce el nombre: ")
                        telefono_contacto=input("Introduce el teléfono: ")
                        Contacto=contacto(nombre_contacto,telefono_contacto)
                        self.Agenda.aniadirContacto(Contacto)
                        
                        input("Presiona Enter para continuar...")
                        self.refrescar()
                        
                    if (opcion==3): #Eliminar contacto
                        
                        nombre_eliminar=input("Introduce el nombra a eliminar: ")
                        self.Agenda.eliminarContacto(nombre_eliminar)
                        
                        input("Presiona Enter para continuar...")
                        self.refrescar()
                    
                    
                    if (opcion==4): #Buscar contacto
                        
                        nombre_buscar=input("Introduce el nombre a buscar: ")
                        self.Agenda.buscaContacto(nombre_buscar)
                        
                        input("Presiona Enter para continuar...")
                        self.refrescar()
                            
                    if (opcion==5): #Consultar huecos agenda
                    
                        self.Agenda.huecosLibres()
                    
                        input("Presiona Enter para continuar...")
                        self.refrescar()
                            
                    if (opcion==6):
                    
                        print("Hasta pronto!!!")
                        input("Presiona Enter para continuar...")
                        self.salir=True
                
                else:
                    print("Error: Opción incorrecta.")
                    
                    input("Presiona Enter para continuar...")
                    self.refrescar()
            
            except:
                pass
    
#############################################################

Ejecutable()

