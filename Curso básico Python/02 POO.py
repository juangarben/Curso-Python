""" 
    DEFINICIONES:
    
    1.- CLASE
    - Es un modelo donde se definen las caraterísticas comunes de un grupo de objetos
    - Por ejemplo el chasis y las ruedas de un coche
    
    2.- EJEMPLAR DE CLASE (INSTANCIA DE CLASE, OBJETO PERTENECIENTE A UNA CLASE):
    - Son los objetos por ejemplo coches (de distintos fabricantes) que comparten las características de la clase (chasis y ruedas)
    
    3.- MODULARIZACIÓN:
    - Aplicación compuesta por varias clases
    - Por ejemplo las antiguas cadenas musicales (compuestos por módulos de audio)
    - Ventajas: cada módulo funciona de forma independientemente, se pueden reutilizar, facil mantenimiento, mayor robustez
    
    4.- ENCAPSULACIÓN:
    - Cada módulo tiene un funcionamiento interno protegido del resto
    
    5.- METODOS DE ACCESO:
    - Conectar unas clases con otras pero sólo a ciertas características de las clases 
    
    
    
    
"""
    
class Coche(): 
    
    #Constructor
    def __init__(self):
    
        #características comunes (propiedades)
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #encapsulamos la propiedad (la protegemos para que no se pueda modificar desde fuera de la clase)
        self.__enmarcha=False
    
    #comportamientos comunes (métodos)
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        
        else:
            return "El coche esta parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis," y un largo de ",
        self.__largoChasis)        
        
    def __chequeo_interno(self): #método encapsulado para que no se pueda acceder desde fuera de la clase
        print("realizando chequeo interno...")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        

miCoche=Coche() #Construcción Ejemplar de clase (Instanciar o crear un objeto)
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------- A continuación creamos el segundo objeto ------------------")

miCoche2=Coche() ##Construcción Ejemplar de clase (Instanciar o crear un objeto)
print(miCoche2.arrancar(False))
#miCoche2.__ruedas=5 #Aunque modifiquemos el valor desde fuera de la clase como la propiedad rueda está encapsulada, no se modifica
miCoche2.estado()

    
        
        
        