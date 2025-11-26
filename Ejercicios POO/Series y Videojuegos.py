import os,random
from abc import ABC, abstractmethod

os.system('cls')

class Entregable(ABC):
    
    #Interfaz Entregable con los siguientes métodos:

    # entregar(): cambia el atributo prestado a true.
    # devolver(): cambia el atributo prestado a false.
    # isEntregado(): devuelve el estado del atributo prestado.
    # Método compareTo (Object a), compara las horas estimadas en los videojuegos y en las series el numero de temporadas. 
    # Como parámetro que tenga un objeto, no es necesario que implementes la interfaz Comparable. Recuerda el uso de los casting de objetos.
    # Implementa los anteriores métodos en las clases Videojuego y Serie.
    

    def __init__(self):
        pass
    
    @abstractmethod
    def entregar(self):
        # entregar(): cambia el atributo prestado a true.
        # Este método debe ser implementado por las subclases.
        pass
        
    @abstractmethod    
    def devolver(self):
        #devolver(): cambia el atributo prestado a false.
        # Este método debe ser implementado por las subclases.
        pass
    @abstractmethod
    def isEntregado(self):
        # isEntregado(): devuelve el estado del atributo prestado.
        # Este método debe ser implementado por las subclases.
        pass

    def compareTo(objeto):
        #compareTo (Object a), compara las horas estimadas en los videojuegos y en las series el numero de temporadas. 
        #Como parámetro tiene un objeto.
        if all(isinstance(item, Videojuego) for item in objeto):
            indice_maximo=[i.horas_estimadas for i in objeto].index(max([i.horas_estimadas for i in objeto]))
            contador=0
            for i in objeto:
                if i.isEntregado():
                    contador+=1     
                    i.devolver()      
            print("El video juego con mayor número de horas estimadas es:\n")
            objeto[indice_maximo].getAtributos()
            print(f"\nSe han devuelto {contador} videojuegos. Gracias!\n")
            
        if all(isinstance(item, Serie) for item in objeto):
            indice_maximo=[i.num_temporadas for i in objeto].index(max([i.num_temporadas for i in objeto]))
            contador=0
            for i in objeto:
                if i.isEntregado():
                    contador+=1     
                    i.devolver()      
            print("La serie con mayor número de temporadas es:\n")
            objeto[indice_maximo].getAtributos()
            print(f"\nSe han devuelto {contador} series. Gracias!\n")
            
        
class Serie(Entregable):
    
    # Crearemos una clase llamada Serie con las siguientes características:
    # Sus atributos son titulo, numero de temporadas, entregado, genero y creador.
    # Por defecto, el numero de temporadas es de 3 temporadas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
    
    def __init__(self,titulo,genero,creador,num_temporadas=3,entregado=False):
        self.titulo=titulo
        self.genero=genero
        self.creador=creador
        self.num_temporadas=num_temporadas
        self.entregado=entregado

    def getAtributos(self):
        # Métodos get de todos los atributos, excepto de entregado.
        print(f"Título: {self.titulo}\nGenero: {self.genero}\nCreador: {self.creador}\nNúmero temporadas: {self.num_temporadas}")
        
    def setAtributos(self,titulo,genero,creador,num_temporadas):
        self.titulo=titulo
        self.genero=genero
        self.creador=creador
        self.num_temporadas=num_temporadas
        
    def entregar(self):
        self.entregado=True
    
    def devolver(self):
        self.entregado=False
    
    def isEntregado(self):
        return self.entregado
    

class Videojuego(Entregable):
    
    # Crearemos una clase Videojuego con las siguientes características:
    # Sus atributos son titulo, horas estimadas, entregado, genero y compañia.
    # Por defecto, las horas estimadas serán de 10 horas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
   
    def __init__(self,titulo,genero,compania,horas_estimadas=10,entregado=False):
        self.titulo=titulo
        self.genero=genero
        self.compania=compania
        self.horas_estimadas=horas_estimadas
        self.entregado=entregado

    def getAtributos(self):
        print(f"Título: {self.titulo}\nGenero: {self.genero}\nCompañía: {self.compania}\nHoras estimadas: {self.horas_estimadas}")
        
    def setAtributos(self,titulo,genero,compania,horas_estimadas):
        self.titulo=titulo
        self.genero=genero
        self.compania=compania
        self.horas_estimadas=horas_estimadas       
    def entregar(self):
        self.entregado=True
    
    def devolver(self):
        self.entregado=False
    
    def isEntregado(self):
        return self.entregado
    
        
######################################################################################################################################

# Ahora crea una aplicación ejecutable y realiza lo siguiente:

# Crea dos arrays, uno de Series y otro de Videojuegos, de 5 posiciones cada uno.
# Crea un objeto en cada posición del array, con los valores que desees, puedes usar distintos constructores.


VJ_1=Videojuego("FIFA2010","Deporte","EA SPORTS",10)
VJ_2=Videojuego("FIFA2011","Deporte","EA SPORTS",15)
VJ_3=Videojuego("FIFA2012","Deporte","EA SPORTS",50)
VJ_4=Videojuego("FIFA2013","Deporte","EA SPORTS",25)
VJ_5=Videojuego("FIFA2014","Deporte","EA SPORTS",30)
listado_VideoJuegos=[VJ_1,VJ_2,VJ_3,VJ_4,VJ_5]

SER_1=Serie("Stranger Things 1","Suspense","Ni idea",2)
SER_2=Serie("Stranger Things 2","Terror","Ni idea",4)
SER_3=Serie("Stranger Things 3","Intriga","Ni idea",8)
SER_4=Serie("Stranger Things 4","Acción","Ni idea",17)
SER_5=Serie("Stranger Things 5","Comedia","Ni idea",2)
listado_Series=[SER_1,SER_2,SER_3,SER_4,SER_5]

# Entrega algunos Videojuegos y Series con el método entregar().
VJ_1.entregar()
SER_2.entregar()
SER_3.entregar()
SER_4.entregar()

# Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos, devuélvelos.
# Por último, indica el Videojuego tiene más horas estimadas y la serie con mas temporadas. 
# Muestralos en pantalla con toda su información (usa el método toString()).

Entregable.compareTo(listado_VideoJuegos)
Entregable.compareTo(listado_Series)







