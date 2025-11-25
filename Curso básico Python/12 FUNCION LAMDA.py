############ FUNCIONES LAMBDA ###########################################
#
# Es una función anónima
# Se usan para simplificar código
# Por ejemplo cuando hay que hacer cálculos o cambiar formatos de string
# No puede tener bucles ni condicionales
# SINTAXIS: lamda parametros:operacion
#
###33####################################################################


'''
def area_triangulo(base,altura):

    return (base*altura)/2

print(area_triangulo(5,7))
'''

area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(5,7))

al_cubo=lambda numero:numero**3
print(al_cubo(2))

potencia=lambda base,exponente:pow(base,exponente)
print(potencia(3,2))

destacar_valor=lambda valor:f"{valor} € !!!! "
print (destacar_valor(2500))