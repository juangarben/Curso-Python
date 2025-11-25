#Uso de la función super() y isintance()
class Persona():
    
    def __init__(self,nombre,edad,lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    
    def descripcion(self):
        print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.lugar_residencia)

class Empleado(Persona):
    
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado) #Llama al constructor de la clase padre (Persona)
        self.salario=salario
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion() #llama al método descripción de la clase padre (Persona)
        print("Salario: ",self.salario,"\nAntiguedad: ",self.antiguedad)

############################################
Manuel=Empleado(1500,15,"Manuel",55,"Colombia")
Manuel.descripcion()    
print(isinstance(Manuel,Empleado)) #devuelve True porque Manuel es una instancia de Empleado
print(isinstance(Manuel,Persona)) #devuelve True porque Manuel es una instancia de Persona ("es siempre una Persona")

############################################
Antonio=Persona("Antonio",40,"España")
print(isinstance(Antonio,Persona)) #devuelve True porque Antonio es una instancia de Persona ("es siempre una Persona")
print(isinstance(Antonio,Empleado)) #devuelve False porque Antonio es una instancia de Persona ("no es siempre un Empleado")





        