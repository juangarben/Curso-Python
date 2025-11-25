# Vamos a realizar una clase llamada Raices, donde representaremos los valores de una ecuación de 2º grado.
# Tendremos los 3 coeficientes como atributos, llamémosles a, b y c.
# Hay que insertar estos 3 valores para construir el objeto.
# Las operaciones que se podrán hacer son las siguientes:

# obtenerRaices(): imprime las 2 posibles soluciones
# obtenerRaiz(): imprime única raíz, que será cuando solo tenga una solución posible.
# getDiscriminante(): devuelve el valor del discriminante (double), el discriminante tiene la siguiente formula, (b^2)-4*a*c
# tieneRaices(): devuelve un booleano indicando si tiene dos soluciones, para que esto ocurra, el discriminante debe ser mayor o igual que 0.
# tieneRaiz(): devuelve un booleano indicando si tiene una única solución, para que esto ocurra, el discriminante debe ser igual que 0.
# calcular(): mostrara por consola las posibles soluciones que tiene nuestra ecuación, en caso de no existir solución, mostrarlo también.
# Formula ecuación 2º grado: (-b±√((b^2)-(4*a*c)))/(2*a)
# Solo varia el signo delante de -b
import math

class RaicesEcuacion:
    
    def __init__(self):
        
        self.raiz1=0.0
        self.raiz2=0.0
        self.__discriminante=0.0

        print(f"Programa que calcula las raices de una ecuación de segundo grado\n\na·(x^2)+b·(x)+c=0\n\n")
        
        while True:
            
            try:
                self.a=float(input("Ingresa el coeficiente a: "))
                break
            except:
                print("El número introducido no es válido, por favor inténtalo de nuevo")
                
        while True:
            
            try:
                self.b=float(input("Ingresa el coeficiente b: "))
                break
            except:
                print("El número introducido no es válido, por favor inténtalo de nuevo")
        
        while True:
            
            try:
                self.c=float(input("Ingresa el coeficiente c: "))
                break
            except:
                print("El número introducido no es válido, por favor inténtalo de nuevo")
        
                
            
        print(f"\n La ecuación a calcular es:\n{self.a}·(x^2)+{self.b}·(x)+{self.c}=0\n\n")
        
    
    def obtenerRaices(self):
        
        print(f"El valor de la raiz_1 es {self.raiz1} \nEl valor de la raiz_2 es {self.raiz2}\n")
        if (self.raiz1>=0):
            signo1="-"
        
        else:
            signo1="+"
        
        if (self.raiz2>=0):
            signo2="-"
        
        else:
            signo2="+"
            
    
        print(f"Descomponiento en factores la ecuación queda del siguiente modo:\n(x{signo1}{abs(self.raiz1)})·(x{signo2}{abs(self.raiz2)})=0")
            
    def obtenerRaiz(self):
        
        print(f"El valor de la única raiz (doble) es {self.raiz1}\n")
        if (self.raiz1>=0):
            signo1="-"
        
        else:
            signo1="+"
        
        print(f"Descomponiento en factores la ecuación queda del siguiente modo:\n(x{signo1}{abs(self.raiz1)})^2)=0")
        
        
    def getDiscriminante(self): # devuelve el valor del discriminante (double), el discriminante tiene la siguiente formula, (b^2)-4*a*c
        
        self.__discriminante=pow(self.b,2)-(4*self.a*self.c)
        return self.__discriminante
        
    def tieneRaices(self):
        
        if(self.getDiscriminante()>0):
            print("La ecuación de segundo grado tiene dos raices\n")
            return True
        else:
            return False
            
    
    def tieneRaiz(self):
        
        if(self.getDiscriminante()==0):
            print("La ecuación de segundo grado tiene una raiz doble\n")
            return True
        else:
            return False
    
    def calcular(self):
        
        if (self.tieneRaices()):
            
            self.raiz1= (-self.b + (math.sqrt(self.getDiscriminante())))/(2*self.a)
            self.raiz2= (-self.b - (math.sqrt(self.getDiscriminante())))/(2*self.a)   
            self.obtenerRaices()
            
        elif (self.tieneRaiz()):
            
            self.raiz1= (-self.b + (math.sqrt(self.__discriminante)))/(2*self.a)
            self.obtenerRaiz()
            
        else:
            print("La ecuación no tiene raices")

    
miEcuacion=RaicesEcuacion()
miEcuacion.calcular()