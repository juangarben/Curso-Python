# Haz una clase llamada Persona que siga las siguientes condiciones:

# Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo. Si quieres añadir algún atributo puedes hacerlo.
# Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números, cadena vacía para String, etc.). Sexo sera hombre por defecto, usa una constante para ello.

import math,os,random

os.system('cls')


class Persona:
    def __init__(self,nombre="",edad=0,sexo="H",peso=0,altura=1):
        self.__nombre=nombre
        self.__edad=edad
        self.DNI=0
        self.__sexo=sexo
        self.__peso=peso
        self.__altura=altura
        self.GeneraDNI()
        
    def calcularIMC(self):
        
    # calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2  en m)), 
    # si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, 
    # si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo de su 
    # peso ideal la función devuelve un 0  y si devuelve un valor mayor que 25 significa que tiene 
    # sobrepeso, la función devuelve un 1. Te recomiendo que uses constantes para devolver estos valores.
        
        IMC=(self.__peso)/(math.pow(self.__altura,2))
        
        if IMC < 20:
            return -1
        elif IMC >= 20 and IMC <=25:
            return 0
        else:
            return 1
    
    def esMayorDeEdad(self):
    # esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.    
        if self.__edad>=18:
            return True
        else:
            return False
        
    def comprobarSexo(self):
    # comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, sera H. No sera visible al exterior.
        if self.__sexo=="H" or self.__sexo=="F":
            return True
        else:
            self.__sexo="H"
            return False
        
    def getAtributos(self):
        # Devuelve toda la información del objeto.
        print(f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__DNI}\nsexo: {self.__sexo}\nPeso: {self.__peso}\nAltura: {self.__altura}\n")
    
    
    def GeneraDNI(self):
        
    # generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente.
    # Este método sera invocado cuando se construya el objeto. Puedes dividir el método para que te sea más fácil. No será visible al exterior.  
        numero_entero = random.randint(10000000, 99999999)
        modulo=numero_entero % 23
        diccionario_letras={0:"T",
                           1:"R",
                           2:"W",
                           3:"A",
                           4:"G",
                           5:"M",
                           6:"Y",
                           7:"F",
                           8:"P",
                           9:"D",
                           10:"X",
                           11:"B",
                           12:"N",
                           13:"J",
                           14:"Z",
                           15:"S",
                           16:"Q",
                           17:"V",
                           18:"H",
                           19:"L",
                           20:"C",
                           21:"K",
                           22:"E"
                           }
        self.__DNI=str(numero_entero)+diccionario_letras[modulo]
        
class Ejecutable:
    def __init__(self):
            
    #Ahora, crea una clase ejecutable que haga lo siguiente:

        # Pide por teclado el nombre, la edad, sexo, peso y altura.
    # Crea 3 objetos de la clase anterior:
    # el primer objeto obtendrá las anteriores variables pedidas por teclado
    # el segundo objeto obtendrá todos los anteriores menos el peso y la altura
    # el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
    # Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
    # Indicar para cada objeto si es mayor de edad.
    # Por último, mostrar la información de cada objeto.

        nombre=input("Introduce el nombre: ")
        edad=int(input("Introduce la edad: "))
        sexo=input("Introduce el sexo: ")
        peso=int(input("Introduce el peso: "))
        altura=int(input("Introduce la altura: "))
        
        listado_personas=[Persona(nombre,edad,sexo,peso,altura),Persona("Jose",58,"J",80,1.60),Persona("maria",23,"F",60,1.65)]
        
        for persona in listado_personas:
            
            print(f"\n____________________\n")
            persona.comprobarSexo()
            persona.getAtributos()
            
            if persona.esMayorDeEdad():
                print("Es mayor de edad")
            else:
                print("Es menor de edad")
            
            if persona.calcularIMC() == 0:
                print("Estás en tu peso ideal")
            elif persona.calcularIMC()==-1:
                print("Estás por debajo de tu peso ideal")
            else:
                print("Tienes sobrepeso. Cuídate!")
                        
                    
      
    ###########################################################################

Ejecutable()

