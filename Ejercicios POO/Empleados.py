# Nos piden hacer una un programa que gestione empleados.

# Los empleados se definen por tener:

# Nombre
# Edad
# Salario
# También tendremos una constante llamada PLUS, que tendrá un valor de 300€

# Tenemos dos tipos de empleados: repartidor y comercial.

# El comercial, aparte de los atributos anteriores, tiene uno más llamado comisión (double).

# El repartidor, aparte de los atributos de empleado, tiene otro llamado zona (String).

# Crea sus constructores, getters and setters y toString (piensa como aprovechar la herencia).

# No se podrán crear objetos del tipo Empleado (la clase padre) pero si de sus hijas. --> Clase Abstracta

# Las clases tendrán un método llamado plus, que según en cada clase tendrá una implementación distinta. Este plus básicamente aumenta el salario del empleado.

# En comercial, si tiene más de 30 años y cobra una comisión de más de 200 euros, se le aplicara el plus.
# En repartidor, si tiene menos de 25 y reparte en la “zona 3”, este recibirá el plus.
# Puedes hacer que devuelva un booleano o que no devuelva nada, lo dejo a tu elección.

# Crea una clase ejecutable donde crees distintos empleados y le apliques el plus para comprobar que funciona.

from abc import ABC, abstractmethod
import os,random

os.system('cls')

class Empleado(ABC):
    
    @abstractmethod
    def __init__(self,nombre,edad,salario):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario
        self.plus=300
    
    @abstractmethod
    def getAtributos(self):
        pass
    
    @abstractmethod
    def Calculo_plus(self):
        pass
        
class Repartidor(Empleado):
    def __init__(self, nombre, edad, salario,zona):
        super().__init__(nombre, edad, salario)
        self.zona=zona
        
    def getAtributos(self):
        print(f"Nombre: {self.nombre}\t Edad: {self.edad}\tSalario: {self.salario}\tZona: {self.zona}")
    
    def Calculo_plus(self):
        # En repartidor, si tiene menos de 25 y reparte en la “zona 3”, este recibirá el plus.
        if self.edad<25 and self.zona=="zona 3":
            self.salario+=self.plus
        
        
class Comercial (Empleado):
    def __init__(self, nombre, edad, salario, comision):
        super().__init__(nombre, edad, salario)
        self.comision=comision
        
    def getAtributos(self):
        print(f"Nombre: {self.nombre}\t Edad: {self.edad}\tSalario: {self.salario}\tComisión: {self.comision}")
    
    def Calculo_plus(self):
        #En comercial, si tiene más de 30 años y cobra una comisión de más de 200 euros, se le aplicara el plus.
        if (self.edad>30 and self.comision>200):
           self.salario+=self.plus
         
            
class Ejecutable:
    # Crea una clase ejecutable donde crees distintos empleados y le apliques el plus para comprobar que funciona.
    def __init__(self):
        
        E1=Comercial("juan",35,40000,201)
        E2=Comercial("pepe",30,50000,201)
        R1=Repartidor("ivan",24,30000,"zona 3")
        R2=Repartidor("luis",19,20000,"zona 2")
    
        E1.getAtributos()
        E1.Calculo_plus()
        print(f"\n____________________________ Calculamos el plus _________________________\n")
        E1.getAtributos()
        print(f"\n##########################################################################\n")
        
        E2.getAtributos()
        E2.Calculo_plus()
        print(f"\n____________________________ Calculamos el plus _________________________\n")
        E2.getAtributos()
        print(f"\n##########################################################################\n")
    
        R1.getAtributos()
        R1.Calculo_plus()
        print(f"\n____________________________ Calculamos el plus _________________________\n")
        R1.getAtributos()
        print(f"\n##########################################################################\n")
        
        R2.getAtributos()
        R2.Calculo_plus()
        print(f"\n____________________________ Calculamos el plus _________________________\n")
        R2.getAtributos()
        print(f"\n##########################################################################\n")
    
    
#######################################################################################################################

Ejecutable()