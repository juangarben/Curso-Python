"""
    POO Que simula la gestión de una biblioteca
"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os,math

class Libro:
    
    def __init__(self,titulo,autor,isbn,editorial,año_publicacion):
        
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.editorial=editorial
        self.año_publicacion=año_publicacion
        self.disponible=True
        
    def actualizar_disponibilidad(self,disponible):
    
        if type(disponible) is not bool:
            raise TypeError("El parámetro 'disponible' debe ser de tipo bool")
        else:
            self.disponible=disponible
        
    def __str__(self):
        if self.disponible:
            disponible="SI"
        else:
            disponible="NO"
            
        return f"{self.titulo:<30}Autor: {self.autor:<15}ISBN:{self.isbn:<10}Editorial: {self.editorial:<10}Año: {self.año_publicacion:<10}Disponible: {disponible}"

    
class Usuario:
    
    def __init__(self,id_usuario,nombre,email):
        self.id=id_usuario
        self.nombre=nombre
        self.email=email
        self.libros_prestados=[]
        
    def prestar_libro(self,libro):
       
        #parámetro 'libro' es un objeto de la clase Libro
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        else:
            libro.actualizar_disponibilidad(False)
            self.libros_prestados.append(libro)
    
    def devolver_libro(self,libro):
        #parámetro 'libro' es un objeto de la clase Libro
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        else:
            libro.actualizar_disponibilidad(True)
            self.libros_prestados.remove(libro)
        
    def mostrar_usuario(self):
        print(f"ID:{self.id}\t{self.nombre}\temail: {self.email}\n\nLibros prestados:\n")
        for libro in self.libros_prestados:
            print(libro)
        
    
    
class Bibliotecario:
    def __init__(self,id_Bibliotecario,nombre):
        pass
    
    def añadir_libro(self):
        pass
    
    def eliminar_libro(self):
        pass
    
    def buscar_libro(self):
        #Se puede buscar por titulo,autor o isbn
        pass
    
    
class Biblioteca:
    def __init__(self):
        self.libros=[]
        self.usuarios=[]
        self.bibliotecarios=[]
        
    def registrar_usuario(self):
        pass
    
    def eliminar_usuario(self):
        pass
    
    def listar_libros(self):
        pass
    
    def listar_usuarios(self):
        pass
    #quizá deberíamos de tener un método para añadir y otro para eliminar bibliotecarios
    
class Prestamo:
    def __init__(self,id_prestamo,libro,usuario):
        
        self.fecha_prestamo=""
        self.fecha_devolucion=""
        
    def finalizar_prestamo(self):
        pass
    
class Ejecutable:
    def __init__(self):
        
        miBiblioteca=Biblioteca("Central")
        
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
            opcion_elegida=Menu(f"Biblioteca {miBiblioteca.nombre}",lista_menu).crear_menu()
        
            if opcion_elegida == 1: #Listar habitaciones
                
                
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida == 2: #Actualizar habitaciones
                
                input("Presiona Enter para continuar...")
                                  
            else:
                salir=True

##############################################################
libro_1=Libro("El señor de los anillos","JR Tolkien",12345,"Altaya",1980)
libro_2=Libro("Los pilares de la tierra","Ken Follet",6789,"perico",1995)
# print(libro_1)
# libro_1.actualizar_disponibilidad(False)
# print(libro_1)
# libro_1.actualizar_disponibilidad(True)
# print(libro_1)
# libro_1.actualizar_disponibilidad("adasd")
# print(libro_1)
# libro_1.actualizar_disponibilidad(False)
# print(libro_1)

u1=Usuario(1,"juan","juanito@gmail.com")
u1.prestar_libro(libro_1)
u1.mostrar_usuario()
print(f"\n##############################\n")
u1.prestar_libro(libro_2)
u1.mostrar_usuario()
print(f"\n##############################\n")
u1.devolver_libro(libro_1)
print(libro_1)
u1.mostrar_usuario()
    