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
        
    def prestar_libro(self,libro,prestamo):
       
        #parámetro 'libro' es un objeto de la clase Libro
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        if type(prestamo) is not Prestamo:
            raise TypeError("El parámetro 'prestamo' debe ser un objeto de la clase Prestamo")
        
        libro.actualizar_disponibilidad(False)
        self.libros_prestados.append(prestamo)

    def devolver_libro(self,libro,id_prestamo,fecha_devolucion):
        #parámetro 'libro' es un objeto de la clase Libro
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        
        libro.actualizar_disponibilidad(True)
        prestamo=buscar_objeto(self.libros_prestados,"id",id_prestamo)
        if prestamo[1]:
            prestamo[0].fecha_devolucion=fecha_devolucion
            print(f"Préstamo devuelto correctamente\n{prestamo[0]}")
            self.libros_prestados.remove(prestamo[0])
            return True
        print("Error: No se ha encontrado el id préstamo")
        return False
        
        
    def mostrar_usuario(self):
        print(f"ID:{self.id}\t{self.nombre}\temail: {self.email}\n\nLibros prestados:\n")
        for prestamo in self.libros_prestados:
            print(prestamo)
        
    
    
class Bibliotecario:
    
    def __init__(self,id_Bibliotecario,nombre):
        
        self.id=id_Bibliotecario
        self.nombre=nombre
    
    def añadir_libro(self,biblioteca,libro):
        #Si el libro ya tiene un isbn existente no lo añade
        
        if type(biblioteca) is not Biblioteca:
            raise TypeError("El parámetro 'biblioteca' debe ser un objeto de la clase Biblioteca")
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        
        if not self.buscar_libro(biblioteca,"isbn",libro.isbn)[1]:
            biblioteca.libros.append(libro)
            print("Libro añadido correctamente")
            return True
          
        print("Error:El libro ya existe. No se puede añadir a la biblioteca")
        return False
                    
            
    def eliminar_libro(self,biblioteca,libro):
        #Si el libro no tiene un id existente no lo elimina
        
        if type(biblioteca) is not Biblioteca:
            raise TypeError("El parámetro 'biblioteca' debe ser un objeto de la clase Biblioteca")
        
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
            
        if self.buscar_libro(biblioteca,"isbn",libro.isbn)[1]:
            
            biblioteca.libros.remove(libro)
            print("Libro eliminado correctamente")
            return True
        
        print("Error:El libro no existe. No se puede eliminar de la biblioteca")
        return False
        
    
    def buscar_libro(self,biblioteca,criterio,valor):
        #Se puede buscar por titulo,autor o isbn
        
        if type(biblioteca) is not Biblioteca:
            raise TypeError("El parámetro 'biblioteca' debe ser un objeto de la clase Biblioteca")
                
        if criterio=="titulo":
            libro_buscado=buscar_objeto(biblioteca.libros,"titulo",valor)
            
        elif criterio=="autor":
            libro_buscado=buscar_objeto(biblioteca.libros,"autor",valor)
        
        elif criterio=="isbn":
            libro_buscado=buscar_objeto(biblioteca.libros,"isbn",valor)
        
        if libro_buscado[1]:
            return libro_buscado[0],True
        
        return None,False
    
class Biblioteca:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]
        self.usuarios=[]
    #   self.bibliotecarios=[]
        
    def registrar_usuario(self):
        
        while True:
            try:
                id=int(input("Introduce el id: "))        
                if not buscar_objeto(self.usuarios,"id",id)[1]:
                    nombre=input("Introduce el nombre: ")
                    email=input("Introduce el email: ")
                    self.usuarios.append(Usuario(id,nombre,email))
                    print("Usuario añadido correctamente")
                    return True
                    
                else:
                    respuesta=input(f"Error: El id ya está registrado.\nInténtalo de nuevo ENTER para continuar o S para salir")
                    if respuesta.lower()=="s":
                        return False
            except:
                print("Error: Dato de entrada incorrecto")        
                
    
    def eliminar_usuario(self):
        while True:
            try:
                id=int(input("Introduce el id: "))
                usuario=buscar_objeto(self.usuarios,"id",id)
            
                if usuario[1]:
                    self.usuarios.remove(usuario[0])
                    print(f"Usuario con id {id} eliminado correctamente")
                    return True
            
                respuesta=input(f"Error: El usuario no existe, no se ha podido eliminar\nInténtalo de nuevo ENTER para continuar o S para salir")
                if respuesta.lower()=="s":
                    return False
        
            except:
                print("Error: Datos de entrada incorrectos, debe ser un número entero")
                    
  
    
    def listar_libros(self):
        
        for libro in self.libros:
            print(libro)
        
    
    def listar_usuarios(self):
         
         for usuario in self.usuarios:
            usuario.mostrar_usuario()
        
    #Podríamos incluir un método para añadir y otro para eliminar bibliotecarios (opcional)
    
class Prestamo:
    def __init__(self,id_prestamo,biblioteca,libro,usuario):
        
        self.id=id_prestamo
        self.biblioteca=biblioteca
        self.libro=libro
        self.usuario=usuario
        self.fecha_prestamo=""
        self.fecha_devolucion=""
        
        if type(biblioteca) is not Biblioteca:
            raise TypeError("El parámetro 'biblioteca' debe ser un objeto de la clase Biblioteca")
        if type(libro) is not Libro:
            raise TypeError("El parámetro 'libro' debe ser un objeto de la clase Libro")
        if type(usuario) is not Usuario:
            raise TypeError("El parámetro 'usuario' debe ser un objeto de la clase Usuario")
       
    def iniciar_prestamo(self):
        
        self.fecha_prestamo=input("Introduce la fecha de inicio prestamo (d-m-a): ")
        self.fecha_prestamo=datetime.strptime(self.fecha_prestamo, '%d-%m-%Y')
        miPrestamo=Prestamo(self.id,self.biblioteca,self.libro,self.usuario)
        miPrestamo.fecha_prestamo=self.fecha_prestamo
        self.usuario.prestar_libro(self.libro,miPrestamo)
    
    def finalizar_prestamo(self):
        
        self.fecha_devolucion=input("Introduce la fecha de finalización del prestamo (d-m-a): ")
        self.fecha_devolucion=datetime.strptime(self.fecha_devolucion, '%d-%m-%Y')
        self.usuario.devolver_libro(self.libro,self.id,self.fecha_devolucion)
        
    def __str__(self):
        return f"Id: {self.id}\tTitulo: {self.libro}\nFecha prestamo: {self.fecha_prestamo}\tFecha devolucion: {self.fecha_devolucion}\n"
        
    
class Ejecutable:
    def __init__(self):
        
        miBiblioteca=Biblioteca("Central")
        
        miBibiotecario=Bibliotecario(1,"juan")
        
        """Lista menu:
        1. Gestionar Biblioteca
            1.1 Añadir libros biblioteca
            1.2 Eliminar libros biblioteca
            1.3 Listar libros biblioteca
            1.4 Buscar libro
        2. Gestionar Usuarios
            2.1 Registrar usuario
            2.2 Dar de baja usuario
            2.3 Listar usuarios
        3. Gestionar prestamos
            3.1 Iniciar prestamo
            3.2 Finalizar prestamo
            3.3 Listar prestamos
        4. Salir
        """
        lista_menu=[
                    "Gestionar biblioteca",
                    "Gestionar usuarios",
                    "Gesionar préstamos",
                    ]
        
        salir=False
    
        while not salir:
            os.system('cls')
            opcion_elegida=Menu(f"Biblioteca {miBiblioteca.nombre}",lista_menu).crear_menu()
        
            if opcion_elegida == 1: #Gestionar biblioteca
                
                while True:
                    while True:
                        try:
                            opcion=int(input(f"1. Añadir libros\n2. Eliminar libros\n3. Listar libros\n4. Buscar Libros\n5. Salir\n"))
                            if opcion>=1 and opcion<=5:
                                break
                            input("Opción incorrecta")
                        except:
                            print("Opción incorrecta")
                            
                    if opcion==1: # 1. Añadir libros
                        
                        titulo=input("Introduce el título: ")
                        autor=input("Introduce el autor: ")
                        editorial=input("Introduce la editorial: ")
                        
                        while True:               
                            try:
                                isbn=int(input("Introduce el isbn: "))
                                año_publicacion=int(input("Introduce el año de publicación: "))    
                                miBibiotecario.añadir_libro(miBiblioteca,Libro(titulo,autor,isbn,editorial,año_publicacion))            
                                break
                                
                            except:
                                print("Error: Entrada de datos incorrecta. Inténtalo de nuevo")
                        
                        input("Presiona Enter para continuar...")
                        os.system('cls')        
                    
                    elif opcion==2: #Eliminar libros
                        
                        while True:
                            try:
                                isbn=int(input("Introduce el isbn del libro: "))
                                libro_encotrado=miBibiotecario.buscar_libro(miBiblioteca,"isbn",isbn)
                            
                                if libro_encotrado[1]:
                                    miBibiotecario.eliminar_libro(miBiblioteca,libro_encotrado[0])
                                else:
                                    print("Libro no encontrado")
                                break
                            
                            except:
                                print("Error: el isbn debe ser un número entero")
                    
                        input("Presiona Enter para continuar...")
                        os.system('cls')        
                    

                    elif opcion==3: #Listar libros
                        
                        miBiblioteca.listar_libros()
                        input("Presiona Enter para continuar...")
                        os.system('cls')        
                        
                    
                    elif opcion==4: #Buscar libros
                        
                        while True:
                            try:
                                
                                criterio=int(input(f"Introduce el criterio de búsqueda:\n1.Autor\n2.Título\n3.ISBN\n4.Salir\n"))
                                
                                if criterio>=1 and criterio<=4:
                                    break
                                    
                                input("Opción incorrecta")
                            
                            except:
                                print("Error: Debes introducir un número entre 1 y 4")
                
                        
                        if criterio==1: #Búsqueda por Autor
                        
                            autor=input("Introduce el nombre del autor: ")
                            libro_encotrado=miBibiotecario.buscar_libro(miBiblioteca,"autor",autor)
                        
                            if libro_encotrado[1]:
                                print(libro_encotrado[0])
                            else:
                                print("Libro no encontrado")
                            
                            input("Presiona Enter para continuar...")
                            os.system('cls')       
                    
                        elif criterio==2: #Búsqueda por Título
                            
                            titulo=input("Introduce el título del libro: ")
                            libro_encotrado=miBibiotecario.buscar_libro(miBiblioteca,"titulo",titulo)
                            
                            if libro_encotrado[1]:
                                print(libro_encotrado[0])
                            else:
                                print("Libro no encontrado")
                            
                            input("Presiona Enter para continuar...")
                            os.system('cls')       
                        
                        elif criterio==3: #Búsqueda por ISBN
                            
                            while True:
                                try:
                                    isbn=int(input("Introduce el título del libro: "))
                                    libro_encotrado=miBibiotecario.buscar_libro(miBiblioteca,"isbn",isbn)
                                
                                    if libro_encotrado[1]:
                                        print(libro_encotrado[0])
                                    else:
                                        print("Libro no encontrado")
                                    break
                                
                                except:
                                    print("Error: el isbn debe ser un número entero")
                            
                            input("Presiona Enter para continuar...")
                            os.system('cls')       
                                
                    else:
                        break
                    
                input("Presiona Enter para continuar...")
                
            
            elif opcion_elegida == 2: # 2. Gestionar usuarios
                
                while True:
                    try:
                        opcion=int(input(f"1. Registrar Usuario\n2. Dar de baja Usuario\n3. Listar Usuarios\n4. Salir\n"))
                        if opcion>=1 and opcion<=4:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                            
                if opcion==1:
                    pass
                
                elif opcion==2:
                    pass
                
                elif opcion==3:
                    pass
                
                
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida == 3: # 3. Gestionar préstamos
                
                while True:
                    try:
                        opcion=int(input(f"1. Iniciar préstamo\n2. Finalizar préstamo\n3. Listar Préstamos\n4. Salir\n"))
                        if opcion>=1 and opcion<=4:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                            
                if opcion==1:
                    pass
                
                elif opcion==2:
                    pass
                
                elif opcion==3:
                    pass
                
                
                input("Presiona Enter para continuar...")
                                  
            else:
                salir=True

############################ FUNCIONES #################################################
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


#######################################################################################

Ejecutable()

# libro_1=Libro("El señor de los anillos","JR Tolkien",12345,"Altaya",1980)
# libro_2=Libro("Los pilares de la tierra","Ken Follet",6789,"perico",1995)

# u1=Usuario(1,"juan","juanito@gmail.com")
# u2=Usuario(2,"mario","marianico@gmail.com")

# miBiblioteca=Biblioteca()

# miBibiotecario=Bibliotecario(1,"juan")

# miBibiotecario.añadir_libro(miBiblioteca,libro_1)
# miBibiotecario.añadir_libro(miBiblioteca,libro_2)
# miBiblioteca.listar_libros()
# # # resultado_busqueda=miBibiotecario.buscar_libro(miBiblioteca,"isbn","1234")
# # # for resultado in resultado_busqueda:
# # #     print(resultado)
# # print(miBibiotecario.eliminar_libro(miBiblioteca))
# # miBiblioteca.listar_libros()
# print("prestamos libro 1")
# p1=Prestamo("p1",miBiblioteca,libro_1,u1)
# p1.iniciar_prestamo()
# u1.mostrar_usuario()
# print("prestamos libro 2")
# p2=Prestamo("p1",miBiblioteca,libro_2,u2)
# p2.iniciar_prestamo()
# u2.mostrar_usuario()
# print("############## LIBROS BIBLIOTECA ##########")
# miBiblioteca.listar_libros()
# print("devolvemos libro 1")
# p1.finalizar_prestamo()
# print("############## LIBROS BIBLIOTECA ##########")
# miBiblioteca.listar_libros()

