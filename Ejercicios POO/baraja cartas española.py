# Vamos a hacer una baraja de cartas españolas orientado a objetos.

# Las operaciones que podrá realizar la baraja son:




import os,random

os.system('cls')

class carta:
    # Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)
    
    def __init__(self):
    
        self.palo_carta=["espadas","bastos","oros","copas"]
        self.numero_carta=[1,2,3,4,5,6,7,10,11,12]
        
        
    def get_carta(self,palo,numero):
        
        self.carta=[]
        
        if (numero>0 and numero<8):
            try:
                self.carta=[self.palo_carta[self.palo_carta.index(palo)],self.numero_carta[numero-1]]
                return True
            except:
                return False
            
        elif (numero>9 and numero<13):
            try:
                self.carta=[self.palo_carta[self.palo_carta.index(palo)],self.numero_carta[numero-3]]
                #self.carta={self.palo_carta[self.palo_carta.index(palo)]:self.numero_carta[numero-3]}
                return True
            except:
                False
        else:
            return False
            
            
        
    
        
       

class baraja(carta):
    
    # La baraja estará compuesta por un conjunto de cartas, 40 exactamente.
    
    def __init__(self):
        
        super().__init__()
        self.baraja=[]
        
        for i in self.palo_carta:
            for j in self.numero_carta:
            
                self.baraja.append([i,j])
        
        
    def accion_barajar(self):
        
        # cambia de posición todas las cartas aleatoriamente
        random.shuffle(self.baraja)
        
    def siguiente_carta(self):
        # siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final, se indica al usuario que no hay más cartas.
        try:
            return self.baraja.pop()
        except:
            print("No hay más cartas disponibles en la baraja")
        
    def cartas_disponibles(self):
        # cartasDisponibles: indica el número de cartas que aún puede repartir
        print(f"\nPuedes repartir {len(self.baraja)} cartas\n")
    
    def dar_cartas(self,cantidad):
        # darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver). En caso de que haya menos cartas que las pedidas, no devolveremos nada pero debemos indicárselo al usuario.
        self.lista_descartes=[]
        if (cantidad>len(self.baraja)):
            print("Lo siento no hay suficientes cartas en la baraja")
        else:
            for i in range(cantidad):
                self.lista_descartes.append(self.siguiente_carta())

    def cartas_monton(self):
        # cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario
        print(f"\n{self.lista_descartes}\n")

    def mostrar_baraja(self):
        # mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, este no mostrara esa primera carta.
        print(self.baraja)

#################################################################################################
    
miBaraja=baraja()
print("Barajando.... \n")
miBaraja.accion_barajar()
miBaraja.mostrar_baraja()

miBaraja.cartas_disponibles()
miBaraja.dar_cartas(5)
miBaraja.mostrar_baraja()

miBaraja.cartas_disponibles()
miBaraja.cartas_monton()
miBaraja.dar_cartas(10)

miBaraja.cartas_monton()
miBaraja.mostrar_baraja()
miBaraja.cartas_disponibles()






