# Vamos a hacer el juego de la ruleta rusa 

import os,random

os.system('cls')

class Revolver:
    
    # Atributos:
    # posición actual (posición del tambor donde se dispara, puede que esté la bala o no)
    # posición bala (la posición del tambor donde se encuentra la bala)
    # Estas dos posiciones, se generaran aleatoriamente.
    def __init__(self):
        
        self.posicion_actual=random.randint(1, 8)
        self.posicion_bala=random.randint(1,8)
    
    def disparar(self):
    # devuelve true si la bala coincide con la posición actual
        if self.posicion_bala==self.posicion_actual:
            return True
        else:
            return False
    
    def siguienteBala(self):
        #cambia a la siguiente posición del tambor
        if (self.posicion_actual>7):
            self.posicion_actual=0
        else:
            self.posicion_actual+=1
        
    def getAtributos(self):
    # muestra información del revolver (posición actual y donde está la bala)
        print(f"\nPosicion actual: {self.posicion_actual}\tPosición Bala: {self.posicion_bala}\n")

class Jugador:
    # Atributos
    # id (representa el número del jugador, empieza en 1)
    # nombre (Empezara con Jugador más su ID, «Jugador 1» por ejemplo)
    # vivo (indica si está vivo o no el jugador)
    
    def __init__(self,id):
        self.id=id
        self.nombre=f"Jugador {self.id}"
        self.vivo=True
    
    def disparar(self,revolver):
        # disparar(Revolver r): el jugador se apunta y se dispara, si la bala se dispara, el jugador muere.
        revolver.siguienteBala()
        if(revolver.disparar()):
            self.vivo=False
        
class Juego:
    # Atributos:
    # Jugadores (conjunto de Jugadores)
    # Revolver
    def __init__(self,jugadores,revolver):
        self.jugadores=jugadores
        self.revolver=revolver
        
    
    def finJuego(self):
    # cuando un jugador muere, devuelve true
        for jugador in self.jugadores:
            if not jugador.vivo:
                print("Fin del juego!!!")
                return True
            
    def ronda(self): 
    #cada jugador se apunta y se dispara, se informara del estado de la partida (El jugador se dispara, no ha muerto en esa ronda, etc.)
        
        for jugador in self.jugadores:
            jugador.disparar(self.revolver)
            if jugador.vivo:
                print(f"{jugador.nombre}\tposición actual: {self.revolver.posicion_actual}\tPosición Bala: {self.revolver.posicion_bala}\tHas tenido suerte!!")
            else:
                print(f"{jugador.nombre}\tposición actual: {self.revolver.posicion_actual}\tPosición Bala: {self.revolver.posicion_bala}\tMuerto!!!")
                #self.finJuego()
                return True
                           
class Ejecutable:
    # El número de jugadores será decidido por el usuario, pero debe ser entre 1 y 6. Si no está en este rango, por defecto será 6.
    # En cada turno uno de los jugadores, dispara el revólver, si este tiene la bala  el jugador muere y el juego termina
    def __init__(self,juego):
        
        while not juego.finJuego():
            juego.ronda() 

###############################################################################################################

jugadores=[Jugador(i+1) for i in range(6)]

Ejecutable(Juego(jugadores,Revolver()))





