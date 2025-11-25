########## FUNCIÓN FILTER #############################################
#
# Verificar que los elementos de una secuencia cumnplen una condición 
# devolviendo un iterador con los elementos que cumplen dicha condición
#
########################################################################

# Ejemplo de una función que devuelva los números pares de una lista

def numero_par(num):
    if num %2==0:
        return True
    else:
        return False

numeros=[17,24,7,39,8,51,92]
print(list(filter(numero_par,numeros))) #Nota hay que hacer un type cast (list) porque filter devuelve un objeto genérico y le estamos pasando como parámetro una lista de números

# Usando la función lamda
print(list(filter(lambda numero_par:numero_par%2==0,numeros)))

# Uso de filter para filtrar objetos en base a un criterio

class Empleado:
    def __init__(self, nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def  __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de {self.salario}€"
    

listaEmpleados=[
    
    Empleado("Juan","Director",75000),
    Empleado("Ana","Presidenta",85000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","Secretaria",27000),
    Empleado("Mario","Botones",21000),
]

salarios_altos=filter(lambda empleado:empleado.salario>50000,listaEmpleados)

for empleado_salario in salarios_altos:
    print(empleado_salario)
    
