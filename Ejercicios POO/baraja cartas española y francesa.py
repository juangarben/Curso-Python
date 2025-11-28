# Vamos a hacer una baraja de cartas españolas y francesas orientado a objetos.

# PalosBarEspañola:
# OROS
# COPAS
# ESPADAS
# BASTOS

# PalosBarFrancesa:
# DIAMANTES
# PICAS
# CORAZONES
# TREBOLES

# Si el palo es de tipo PalosBarFrancesa:

# La carta número 11 será Jota
# La carta numero 12 será Reina
# La carta numero 13 será Rey
# La carta numero 1 será As

# Si el palo es de tipo PalosBarEspañola:

# La carta numero 10 será Sota
# La carta numero 12 será Caballo
# La carta numero 13 será Rey
# La carta numero 1 será As

import os,random
from abc import ABC,abstractmethod
from colorama import init, Fore, Style # type: ignore

init(autoreset=True)
os.system('cls')

class carta:
        
    def __init__(self):
    
        self.PalosBarEspanola=["OROS","COPAS","ESPADAS","BASTOS"]
        self.PalosBarFrancesa=["DIAMANTES","PICAS","CORAZONES","TREBOLES"]
        
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
                return True
            except:
                False
        else:
            return False
            
                    
class baraja(ABC,carta): #Será la clase padre y abstracta
        
    def __init__(self):
        super().__init__()
        self.num_cartas_total=40 #valor inicial por defecto
        self.baraja=[]
        self.lista_descartes=[]  
      
    @abstractmethod
    def crearBaraja(self):
        pass
        
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
        if (cantidad>len(self.baraja)):
            print("Lo siento no hay suficientes cartas en la baraja")
        else:
            for i in range(cantidad):
                self.lista_descartes.append(self.siguiente_carta())

    def cartas_monton(self):
        # cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario
        for carta in self.lista_descartes:
             
            if carta[0]=="DIAMANTES" or carta[0]=="CORAZONES":
                
                print(Fore.RED+str(carta))
            else:
                print(carta)
        # print(f"\n{self.lista_descartes}\n")

    def mostrar_baraja(self):
        # mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, este no mostrara esa primera carta.
        #print(self.baraja)
        for carta in self.baraja:
             
            if carta[0]=="DIAMANTES" or carta[0]=="CORAZONES":
                
                print(Fore.RED+str(carta))
            else:
                print(carta)
            
# Creamos dos clases hijas:

class BarajaEspanola(baraja): #tendrá un atributo boolean para indicar si queremos jugar con las cartas 8 y 9 (total 48 cartas) o no (total 40 cartas).

    def __init__(self, jugar8y9=False):
        self.jugar8y9=jugar8y9
        super().__init__()


    def crearBaraja(self):
        
        if self.jugar8y9: #juegan 8 y 9 en total 48 cartas
            self.numeros_cartas=["AS",2,3,4,5,6,7,8,9,"SOTA","CABALLO","REY"]
        
        else: # No juegan 8 y 9 en total 40 cartas
            self.numeros_cartas=["AS",2,3,4,5,6,7,"SOTA","CABALLO","REY"]
        
        for palo in self.PalosBarEspanola:
            for numero in self.numeros_cartas:
                self.baraja.append([palo,numero])
        

class BarajaFrancesa(baraja): #no tendrá atributos, el total de cartas es 52 y el número de cartas por palo es de 13. 
    def __init__(self):
        super().__init__()
    
    def crearBaraja(self):
        
        self.numeros_cartas=["AS",2,3,4,5,6,7,8,9,10,"JOTA","REINA","REY"]
        
        for palo in self.PalosBarFrancesa:
            for numero in self.numeros_cartas:
                self.baraja.append([palo,numero])
        
#################################################################################################

print("########################## BARAJA FRANCESA ##########################################")

Mi_baraja_francesa=BarajaFrancesa()
Mi_baraja_francesa.crearBaraja()
Mi_baraja_francesa.mostrar_baraja()
print("\nBarajando.... \n")

Mi_baraja_francesa.accion_barajar()
Mi_baraja_francesa.mostrar_baraja()
Mi_baraja_francesa.cartas_disponibles()

print("Dame 5 cartas...\n")
Mi_baraja_francesa.dar_cartas(5)
print("Estas son las cartas en el montón de descartes...\n") 
Mi_baraja_francesa.cartas_monton()
print(" ______________________________________")
Mi_baraja_francesa.mostrar_baraja()
Mi_baraja_francesa.cartas_disponibles()

print("Dame 10 cartas....")
Mi_baraja_francesa.dar_cartas(10)
print("Estas son las cartas en el montón de descartes...") 
Mi_baraja_francesa.cartas_monton()
print(" ______________________________________")
Mi_baraja_francesa.mostrar_baraja()
Mi_baraja_francesa.cartas_disponibles()

print("########################## BARAJA ESPAÑOLA ##########################################")

Mi_baraja_española=BarajaEspanola(True)
Mi_baraja_española.crearBaraja()
Mi_baraja_española.mostrar_baraja()
print("Barajando.... \n")

Mi_baraja_española.accion_barajar()
Mi_baraja_española.mostrar_baraja()
Mi_baraja_española.cartas_disponibles()

print("Dame 5 cartas...")
Mi_baraja_española.dar_cartas(5)
Mi_baraja_española.mostrar_baraja()
Mi_baraja_española.cartas_disponibles()

print("Estas son las cartas en el montón de descartes...") 
Mi_baraja_española.cartas_monton()

print("Dame 10 cartas....")
Mi_baraja_española.dar_cartas(10)
print("Estas son las cartas en el montón de descartes...") 
Mi_baraja_española.cartas_monton()

Mi_baraja_española.mostrar_baraja()
Mi_baraja_española.cartas_disponibles()

############################################################################################################





