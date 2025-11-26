import os,random

os.system('cls')

class Electrodomestico: 
    # Crearemos una supeclase llamada Electrodomestico con las siguientes características:
    # Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso. Indica que se podrán heredar.
    # Por defecto, el color sera blanco, el consumo energético sera F, el precioBase es de 100 € y el peso de 5 kg. Usa constantes para ello.
    
    def __init__(self,precio_base=100,color="BLANCO",consumo="F",peso=5):
        self.precio_base=precio_base
        self.color=color
        self.consumo=consumo
        self.peso=peso
        
        if (self.__comprobarConsumoEnergetico(self.consumo)):
            self.consumo=consumo.upper()
        else:
             self.consumo="F"
             
        if (self.__comprobarColor(self.color)):
            self.color=color.upper()
        else:
             self.color="BLANCO"
        
    def __comprobarColor(self,color):
        #comprueba que el color es correcto, sino lo es usa el color por defecto. Se invocara al crear el objeto y no sera visible.
        # Los colores disponibles son blanco, negro, rojo, azul y gris. No importa si el nombre esta en mayúsculas o en minúsculas.
        
        colores_disponibles=["blanco","negro","rojo","azul","gris"]
        
        if color.casefold() in [palabra.lower() for palabra in colores_disponibles]:
            return True
        else:
            return False
    
    def get_atributos(self):
        print(f"Precio Base: {self.precio_base}€\nColor: {self.color}\nConsumo: {self.consumo}\nPeso: {self.peso}Kg\nPrecio Final: {self.precioFinal()}€\n") 
        
        
    def __comprobarConsumoEnergetico(self,letra):         
        # comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y no sera visible.
        
        letras_disponibles=["A","B","C","D","E","F"]
        
        if letra.casefold() in [palabra.lower() for palabra in letras_disponibles]:
            return True
        else:
            return False
        
    def precioFinal(self):
        # precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también. Esta es la lista de precios:

        # Letra	Precio
        # A	100 €
        # B	80 €
        # C	60 €
        # D	50 €
        # E	30 €
        # F	10 €
        
        # Tamaño	Precio
        # Entre 0 y 19 kg	10 €
        # Entre 20 y 49 kg	50 €
        # Entre 50 y 79 kg	80 €
        # Mayor que 80 kg	100 €
    
        dict_letra_precio={"A":100,"B":80,"C":60,"D":50,"E":30,"F":10}
        
        precio_final=self.precio_base + dict_letra_precio[self.consumo]

        if (self.peso>=0 and self.peso<=19):
            precio_final+=10
        elif (self.peso>=20 and self.peso<=49):
            precio_final+=50
        elif (self.peso>=50 and self.peso<=79):
            precio_final+=80
        elif (self.peso>=80):
            precio_final+=100
            
        return precio_final
        
            

class Lavadora(Electrodomestico): 
    
    # Crearemos una subclase llamada Lavadora con las siguientes características:
    # Su atributo es carga, ademas de los atributos heredados. -->OK
    # Por defecto, la carga es de 5 kg. Usa una constante para ello.-->OK

    
    def __init__(self,precio_base,color,consumo,peso,carga=5):
        self.carga=carga
        super().__init__(precio_base,color,consumo,peso)
    
    def getCarga(self):
        # Método get de carga. --> OK
        print(f"La carga de la lavadora es: {self.carga}Kg")

    def precioFinal(self):
        # precioFinal():, si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se incrementara el precio. --> OK
        # Llama al método padre y añade el código necesario. 
        # Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
        
        precio_final=super().precioFinal()
        
        if self.carga>30:
            precio_final+=50
        
        return precio_final 

        
class Television(Electrodomestico):

    # Crearemos una subclase llamada Television con las siguientes características:
    # Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), ademas de los atributos heredados.
    # Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false. --> OK
    
    def __init__(self,precio_base,color,consumo,peso,resolucion=20,sintonizador_TDT=False):#sintonizador_TDT):
        self.resolucion=resolucion
        self.sintonizador_TDT=sintonizador_TDT
        super().__init__(precio_base,color,consumo,peso)
        
    def get_resolucion_sintonizador(self):
        
        # Método get de resolución y sintonizador TDT.
        
        print(f"La resolución es de: {self.resolucion} pulgadas")
       
        if self.sintonizador_TDT:
            print("Lleva sintonizador TDT")
        else:
            print("No lleva sintonizador TDT")
            
    def precioFinal(self):
        
        # precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% 
        # y además si tiene un sintonizador TDT incorporado, aumentara 50 €. 
        # Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.

        precio_final=super().precioFinal()
        
        if self.resolucion>40:
            precio_final=precio_final*1.3
        
        if self.sintonizador_TDT:
            precio_final+=50
        
        return precio_final
        
    
class Ejecutable(Electrodomestico):
    # Ahora crea una clase ejecutable que realice lo siguiente:  
    def __init__(self):
        # Crea un array de Electrodomesticos de 10 posiciones. 
        # Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
    
        Lista_Electrodomesticos=[]
        Lista_Electrodomesticos.append(Electrodomestico(110,"blanco","A",20))
        Lista_Electrodomesticos.append(Television(100,"blanco","A",20,42,True))
        Lista_Electrodomesticos.append(Television(100,"blanco","A",20,50,False))
        Lista_Electrodomesticos.append(Lavadora(120,"blanco","A",20,7))
        Lista_Electrodomesticos.append(Lavadora(80,"blanco","A",20,7))
        Lista_Electrodomesticos.append(Television(100,"blanco","A",20,22,True))
        Lista_Electrodomesticos.append(Lavadora(150,"blanco","A",20,7))
        Lista_Electrodomesticos.append(Electrodomestico(200,"blanco","A",20))
        Lista_Electrodomesticos.append(Television(100,"blanco","A",20,32,False))
        Lista_Electrodomesticos.append(Lavadora(240,"blanco","A",20,7))
        
        Lista_Electrodomestico=[]
        Lista_precios_Electrodomestico=[]
        Lista_Lavadoras=[]
        Lista_precios_Lavadoras=[]
        Lista_Television=[]
        Lista_precios_Television=[]
        
        # Ahora, recorre este array y ejecuta el método precioFinal().
        # Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, 
        # el de las lavadoras por otro y la suma de los Electrodomesticos 
        # (puedes crear objetos Electrodomestico, pero recuerda que Television y Lavadora también son electrodomésticos). 
        # Recuerda el uso operador instance.        
        
        for i in Lista_Electrodomesticos:
            
            if isinstance(i,Lavadora):
                Lista_Lavadoras.append(i)
                Lista_precios_Lavadoras.append(i.precioFinal())
            elif isinstance(i,Television):
                Lista_Television.append(i)
                Lista_precios_Television.append(i.precioFinal())
            else:
                Lista_Electrodomestico.append(i)
                Lista_precios_Electrodomestico.append(i.precioFinal())
                
        #Mostramos los atributos y precios de cada tipo de electrodoméstico:
        
        print(" ____________________ LISTA LAVADORAS __________________________")
        for i in Lista_Lavadoras:
            i.get_atributos()
            i.getCarga()
            print("__________________________________________________________")
            
        TOTAL_LAVADORAS=sum([int(i) for i in Lista_precios_Lavadoras])
        print(f"\nTOTAL LAVADORAS= {TOTAL_LAVADORAS}€\n")

        print(" ____________________ LISTA TELEVISORES __________________________")
        for i in Lista_Television:
            i.get_atributos()
            i.get_resolucion_sintonizador()
            print("__________________________________________________________")
        
        TOTAL_TELEVISORES=sum([int(i) for i in Lista_precios_Television])
        print(f"\nTOTAL TELEVISORES = {TOTAL_TELEVISORES}€\n")

        print(" ____________________ LISTA OTROS ELECTRODOMÉSTICOS __________________________")
        for i in Lista_Electrodomestico:
            i.get_atributos()
            print("__________________________________________________________")
        
        TOTAL_ELECTRODOMESTICOS=sum([int(i) for i in Lista_precios_Electrodomestico])
        print(f"\nTOTAL OTROS ELECTRODOMÉSTICOS = {TOTAL_ELECTRODOMESTICOS}€\n")
        # Por ejemplo, si tenemos un Electrodomestico con un precio final de 300, una lavadora de 200 y una televisión de 500, 
        # el resultado final sera de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y 500 para televisión.         
        
        print(f"\n_________________________ PRECIO TOTAL FINAL= {TOTAL_ELECTRODOMESTICOS+TOTAL_LAVADORAS+TOTAL_TELEVISORES}€________________\n\n")


####################################################################################################

Ejecutable()


