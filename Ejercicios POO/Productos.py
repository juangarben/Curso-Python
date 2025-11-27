# Nos piden hacer que gestionemos una serie de productos.

# Los productos tienen los siguientes atributos:

# Nombre
# Precio
# Tenemos dos tipos de productos:

# Perecedero: tiene un atributo llamado días a caducar
# No perecedero: tiene un atributo llamado tipo

import os,random

os.system('cls')

class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
    def getAtributos(self):
        print(f"Nombre: {self.nombre}\tPrecio: {self.precio}€\n")
    
        

class Perecedero(Producto):
    def __init__(self, nombre, precio,dias_caducar):
        super().__init__(nombre, precio)
        self.dias_caducar=dias_caducar
    
    def getAtributos(self):
        print(f"Nombre: {self.nombre}\tPrecio: {self.precio}€\tDías para caducar:{self.dias_caducar}\n")

class No_Perecedero(Producto):
    def __init__(self, nombre, precio,tipo):
        super().__init__(nombre, precio)
        self.tipo=tipo
    
    def getAtributos(self):
        print(f"Nombre: {self.nombre}\tPrecio: {self.precio}€\tTipo:{self.tipo}\n")

class Ejecutable:
    # Crea una clase ejecutable y crea un array de productos y muestra el precio total de vender 5  productos de cada uno. 
    # Crea tú mismo los elementos del array.
    def __init__(self):
        
        p1=Perecedero("carne",1.5,2)
        p2=No_Perecedero("lejia",1.15,"Droguería")
        p3=Producto("Tele",124)
        p4=Perecedero("Yogur",0.5,1)
        p5=No_Perecedero("comida gato",5.43,"Animales")
        p6=Perecedero("leche",1.68,3)
        p7=Producto("carbon",6.73)
        p8=Producto("libros",5.43)
        p9=No_Perecedero("Lavavajillas",1.69,"Drogueria")
        p10=Perecedero("pizzas",3.47,1)
        p11=Perecedero("lasaña",2.51,2)
        p12=No_Perecedero("comida perro",5.43,"Animales")
        p13=No_Perecedero("comida peces",4.43,"Animales")
        p14=Producto("cuberteria",3.84)
        p15=Producto("servilletas",4.18)
        
        Array_productos=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]
        lista_perecederos=[]
        lista_no_perecederos=[]
        lista_productos=[]
        
        for producto in Array_productos:
            if isinstance(producto,Perecedero):
                lista_perecederos.append(producto)
            elif isinstance(producto,No_Perecedero):
                lista_no_perecederos.append(producto)
            else:
                lista_productos.append(producto)
        
        for i in lista_perecederos:
            i.getAtributos()
            print(f"Precio total de vender 5 productos perecederos: {Calcular(i,5)}€")
            print(f"\n____________________________________________________________________\n")
        
        for i in lista_no_perecederos:
            i.getAtributos()
            print(f"Precio total de vender 5 productos no perecederos: {Calcular(i,5)}€")
            print(f"\n____________________________________________________________________\n")
            
        for i in lista_productos:
            i.getAtributos()
            print(f"Precio total de vender 5 producto: {Calcular(i,5)}€")
            print(f"\n____________________________________________________________________\n")
                
        
        
def Calcular(objeto,cantidad) -> float:
    # Tendremos una función llamada calcular, que según cada clase hará una cosa u otra, 
    # a esta función le pasaremos un numero siendo la cantidad de productos
    # En Producto, simplemente seria multiplicar el precio por la cantidad de productos pasados.
    # En Perecedero, aparte de lo que hace producto, el precio se reducirá según los días a caducar:
    # Si le queda 1 día para caducar, se reducirá 4 veces el precio final.
    # Si le quedan 2 días para caducar, se reducirá 3 veces el precio final.
    # Si le quedan 3 días para caducar, se reducirá a la mitad de su precio final.
    # En NoPerecedero, hace lo mismo que en producto

    if isinstance(objeto,Perecedero):
            
        precio_total=objeto.precio*cantidad
            
        if(objeto.dias_caducar==1):
            precio_total=precio_total*0.75
        elif(objeto.dias_caducar==2):
            precio_total=precio_total*0.67
        elif(objeto.dias_caducar==3):
            precio_total=precio_total*0.5        
    
    elif isinstance(objeto,No_Perecedero) or isinstance(objeto,Producto):
            precio_total=objeto.precio*cantidad
            
    return precio_total
    
            
  #########################################################################################################################
 
Ejecutable()
  

        