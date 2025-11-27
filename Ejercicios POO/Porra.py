# Estando en un grupo de amigos, se planea hacer una porra de la liga de fútbol. 
# A nosotros se nos ocurre hacer un programa en POO para simular como podría desarrollarse la porra.

# Cada jugador de la porra, pone un 1 euro cada jornada y decide el resultado de los partidos acordados. -->OK
# Si nadie acierta en una jornada los resultados, el bote se acumula. -->OK
# En principio, deben acertar el resultado de dos partidos para llevarse el dinero del bote de la porra. -->OK
# Todos empiezan con un dinero inicial que será decidido por el programador (ya sea como parámetro o como constante).-->OK
# Si el jugador no tiene dinero en una jornada no podrá jugar la porra. 

# Para esta versión, entre jugadores podrán repetir resultados repetidos, -->OK
# por lo que el jugador que primero diga ese resultado (tal como estén de orden) se llevara primero el bote. -->OK
# Los resultados de la porra serán generados aleatoriamente, tanto los de jugador como los de los partidos -->OK
# (no es necesario nombre, solo resultados).
# Al final del programa, se deberá mostrar el dinero que tienen los jugadores y el número de veces que han ganado. 
# Para este ejercicio, recomiendo usar interfaces (no hablo de interfaces gráficas) para las constantes y métodos que sean necesarios.

import os,random
from abc import ABC, abstractmethod

os.system('cls')

class Jornada:
    def __init__(self,numero,bote=0):
        self.numero=numero
        self.bote=bote
        self.aciertos_jornada=0
        self.__generar_partidos()
        
        print(f"_______________ Partidos Jornada {self.numero} ______________________\n")
        print(self.partidos)
        print(f"\nBote de la jornada: {self.bote}€")
        print(f" __________________________________________________________________________\n")
        
    def __generar_partidos(self):
        
        self.partidos=[random.choice(["1","X","2"]) for i in range(5)]
       

class Jugador:
    def __init__(self,nombre,dinero=10):
        self.nombre=nombre
        self.dinero=dinero
        self.contador_aciertos=0
        
    def __generar_resultados(self):
        
        self.resultados=[random.choice(["1","X","2"]) for i in range(5)]
        print(f"Apuesta:{self.resultados}")
    
    def apostar(self,jornada):
        
        if self.dinero>0:
    
            self.__generar_resultados()
            self.dinero-=1
            jornada.bote+=1
            print(f"Bote de la jornada: {jornada.bote}€")
            
        else:
            print("Lo siento no tienes dinero para apostar")
            print("_______________________________________________________________________")
     
    def comprobar_resultados(self,jornada):
        #compobar resultados con los partidos de la jornada y si se aciertan 2 se lleva el dinero del bote de la jornada
        self.jornada=jornada
        index=0
        contador=0
        
        if self.dinero >0:
            
            print(f"\n_________________ Comprobación de resultados Jugador: {self.nombre} __________________\n")
            for i in self.resultados:
                
                if i==jornada.partidos[index]:
                    print("Has acertado: partido "+str(index+1))
                    contador+=1
                
                index+=1
                
            if (contador>=2 and jornada.aciertos_jornada==0):
                
                print(f"Enhorabuena!!. Te llevas la porra")
                self.dinero+=jornada.bote
                jornada.bote=0
                self.contador_aciertos+=1        
                jornada.aciertos_jornada+=1
            
            else:
                print("Lo siento, no te llevas la porra!!")
                
            
            print(f"Saldo_final: {self.dinero}€\nAciertos: {self.contador_aciertos}")
        
            
    def getAtributos(self):
        print(f"_______________ Jugador: {self.nombre} _____________________")
        print(f"Saldo Inicial: {self.dinero}€\nAciertos: {self.contador_aciertos}")
        
###################################################################
## Generar una clase Ejecutable que se le pase como parámetros:
# - la lista inicial de jugadores
# - la lista de jornadas
# Que llame a los siguientes métodos en orden:
# Para todos los jugadores en cada jornada:
# 1.- jugador_x.getAtributos()
# 2.- jugador_x.apostar(jornada_x)
# Para todos los jugadores:
# 1.- jugador_x.comprobar_resultados(jornada_x)
#print(f"\n%%%%%%%%%%%%%%%%%%% El bote para la próxima jornada es: {Jornada1.bote}€ %%%%%%%%%%%%%%%%%%%%%%%%\n")
#
#######################################################################

class Ejecutable:
    
    def __init__(self,lista_jornadas,lista_jugadores):
        self.lista_jornadas=lista_jornadas
        self.lista_jugadores=lista_jugadores
        
        index=0
        for i in range(len(lista_jornadas)):
            
            for jugador in lista_jugadores:
                jugador.getAtributos()
                jugador.apostar(lista_jornadas[index])
            
            for jugador in lista_jugadores:
                jugador.comprobar_resultados(lista_jornadas[index])
            
            print(f"\n%%%%%%%%%%%%%%%%%%% El bote para la próxima jornada es: {lista_jornadas[index].bote}€ %%%%%%%%%%%%%%%%%%%%%%%%\n")
            
            index+=1
            
            if index<len(lista_jornadas):
                lista_jornadas[index].bote=lista_jornadas[index-1].bote
            
            self.ranking()
        
    def ranking(self):
        #ordena los ganadores de mayor a menor número de aciertos y muestra los atributos
        lista_aciertos=[jugador.contador_aciertos for jugador in lista_jugadores]
        indice=lista_aciertos.index(max(lista_aciertos))
        print(f"El máximo acertante es:\n")
        self.lista_jugadores[indice].getAtributos()
        print(f"\n")
            
                                
####################################################################################            
        
Jornada1=Jornada(1,100)
Jornada2=Jornada(2)
Jornada3=Jornada(3)
Jornada4=Jornada(4)
Jornada5=Jornada(5)
Jornada6=Jornada(6)

lista_jornadas=[Jornada1,Jornada2,Jornada3,Jornada4,Jornada5,Jornada6]

Jugador1=Jugador("juan",120)
Jugador2=Jugador("pepe",100)
Jugador3=Jugador("luis",50)
Jugador4=Jugador("maria",0)
Jugador5=Jugador("eva",200)

lista_jugadores=[Jugador1,Jugador2,Jugador3,Jugador4,Jugador5]

Ejecutable(lista_jornadas,lista_jugadores)







