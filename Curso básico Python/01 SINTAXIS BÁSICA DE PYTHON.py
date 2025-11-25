import math #importamos la libería para usar las funciones de matemáticas

#########################################################################
# FUNCIONES
#########################################################################

def sum(n1,n2):
    return n1+n2

    #print(sum(1.5,5.2))

#########################################################################
# LISTAS --> Equivalente a los arrays en otros lenguajes de programación
##########################################################################

lista=["Maria","Pepe","Marta","Antonio"]
lista[:] #muestra todos los elementos de la lista
lista[2] #valor indice 2 (Marta)
lista[-1] #valor indice negativo empieza por el final de la lista -1 (Antonio)
lista[0:3] #muestra valores de los índices 0,1 y 2
lista[1:] #accede a partir del indice 1 (incluido) hasta el final de la lista
lista.append("Juan") #añade un elemento al final de la lista
lista.insert(2,"Sandra") #añade en el indice 2
lista.extend(["Ana","Lucia","Estefania"]) #añadimos varios elementos al final de la lista (concatenar)
lista.index("Antonio") #devuelve el índice de "Antonio" que es el 4
    #print("Pepe" in lista) #Comprobar si un elemento se encuentra en una lista --> devuelve True
lista.extend([True,5.6,8])# Las listas pueden almacenar distintos tipos de datos
lista.remove("Ana") #eliminar elementos de la lista o un indice
lista.pop() #elimina el último elemento de la lista

#sumar listas
lista2=["Jose","Javi"]
lista3=lista+lista2 #concatena las dos listas

#repetir listas con *
    #print(lista)
lista4=lista*3
    #print(lista4)

#########################################################################
# TUPLAS --> Son listas que no se pueden modificar, se usan como claves en un diccionario, son más eficientes en tiempos de ejecución
#########################################################################

tupla=("Juan",13,False)
    #print(tupla[0]) #Imprime el valor del índice 0 de la tupla "Juan"
    #print(tupla)
lista_convertida=list(tupla) #Convertir tuplas en listas
    #print(lista_convertida)
tupla_convertida=tuple(lista)#Convertir lista en tupla
    #print(lista)
    #print(tupla_convertida)
tupla.count("Juan") #Cuenta las veces que se encuentra ese elemento en la tupla (1)
len(tupla) #Indica el número de elementos de la tupla

#Desempaquetado de una tupla
mi_tupla=("Juan",25,4,1978)
nombre,dia,mes,agno=mi_tupla #guarda en cada variable los valores de la tupla en el orden de los indices
    #print(nombre,mes,agno,dia)

#########################################################################
# DICCIONARIOS --> Los datos se almacen como Clave:Valor, se pueden almacenar dentro listas, tuplas y otros diccionarios
#########################################################################

mi_diccionario={"Alemania":"Berlin","Francia":"Paris","España":"Madrid","Reino Unido":"Londres"}
    #print(mi_diccionario["España"])
mi_diccionario["Italia"]="Roma" #añade un nuevo elemento al final del diccionario
#NOTA: No pueden haber dos claves iguales en el diccionario
del mi_diccionario["Reino Unido"] #elimina el elemento con clave "Reino Unido"

mi_diccionario2={1:"Juan",2:"Pepe"} #El diccionario puede tener distintos tipos de datos
tupla_dic=("España","Francia","Alemania") #Usamos una tupla para crear las claves del diccionario
mi_diccionario3={tupla_dic[0]:"Madrid",tupla_dic[1]:"Paris",tupla_dic[2]:"Berlin"} #Creamos el diccionario con las claves formada por la tupla
    #print(mi_diccionario3)
tupla_anillos=("1991","1992","1993")
mi_diccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":tupla_anillos} #ponemos una tupla como valor de una clave en un elemento del diccionario
    #print(mi_diccionario4)
    #print(mi_diccionario4["Equipo"])
mi_diccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":tupla_anillos} } #Un diccionario dentro de otro diccionario
#print(mi_diccionario4.keys()) #imprime las claves
#print(mi_diccionario4.values()) #imprime los valores
#print(len(mi_diccionario4)) #imprime la longitud del diccionario

#########################################################################
# CONDICIONALES IF, ELSE, ELIF
#########################################################################

def evaluacion(nota):
    if nota>=00:
        if nota<5:
            calificacion= "INSUFICIENTE"
        elif nota==5:
            calificacion="SUFICIENTE"
        elif nota==6:
            calificacion="BIEN"
        elif 7<=nota<=8 : #Concatenación de operadores lógicos
            calificacion="NOTABLE"
        elif 9<=nota<=10:
            calificacion="SOBRESALIENTE"
        else:
            calificacion="ERROR LA NOTA NO PUEDE SER MAYOR DE 10"
    else:
        calificacion= "ERROR LA NOTA DEBE SER POSITIVA"
    return calificacion
        
#nota_alumno=int(input("Introduce la nota del alumno: "))
#print("La nota del alumno es un " + str(nota_alumno) + " Calificación " + evaluacion(nota_alumno))


#########################################################################
# BUCLE FOR (Determinado)
#########################################################################

"""for i in [1,2,3]:
    print(i)
    print("Hola")
"""

"""for i in range(5,12,2): #Tipo Range (es como un contador, lo que hace es generar una lista que empieza en el primer argumento,hasta el segundo argumento-1, en saltos del tercer argumento
    print(f"valor de la variable {i}") #notación de print para unir texto con variables
"""

#Ejemplo evaluar dirección de correo válida si tiene @ y . 
"""
email=False
contador=0
miEmail=input("Introduce el email: ")

for i in range(len(miEmail)):
    if miEmail[i]=="@" or miEmail[i]==".":
        contador=contador+1 #es lo mismo que contador+=1
if contador==2:
    email=True
    
if email:
    print("email correcto")
else:
    print("email incorrecto")
"""
    
#########################################################################
# BUCLE WHILE (Indeterminado)
#########################################################################
"""
i=0
while i<10:
    i=i+1
    print(i)
"""
"""
edad=int(input("Introduce la edad: ")) 
while edad<0 or edad>100:
    print("Edad incorrecta")
    edad=int(input("Introduce la edad: ")) 
"""
"""
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un número: "))
intentos=0 #número de intentos para salir del while
while numero <0:
    intentos=intentos+1
    print("No se puede hallar la raiz de un número negativo")
    
    if intentos==2:
        print("has excedido el número de intetos")
        break
        
    numero=int(input("Introduce un número: "))


solucion=math.sqrt(numero)
print("la raiz cuadrada de " + str(numero) + "= "+str(solucion))
"""
"""
for letra in "Python":
    if letra=="h":
        continue #ignora lo que hay a continuación y salta a la siguiente iteración del bucle
    print(letra)
"""

#########################################################################
# GENERADORES --> 'yield' se devuelven los valores de uno en uno cada vez que se llama a la función y se guardan dentro de un objeto generador iterable
#             --> son más eficientes y se usan con listas de valores infinitos
#########################################################################
"""
print("Programa que genera una lista de números pares:")

def generaPares(limite):
    num=1;
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista
    
print(generaPares(10))
"""
"""
def generaParesGenerador(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1
devuelvePares=generaParesGenerador(10) #guardamos el objeto iterable que devuelve la función
print(next(devuelvePares)) #next devuelve el siguientevalor del objeto generador
print("Aqui podría ir más código")
print(next(devuelvePares))
print("Aqui podría ir más código")
print(next(devuelvePares))
    """
"""
def devuelve_ciudades(*ciudades): # el * se refiere a un número indeterminado de argumentos en forma de tupla
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento #yield from devuelve el valor del bucle anidado

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
"""

#########################################################################
# EXCEPCIONES --> Error inesperado en tiempo de ejecución (por ejemplo división por cero)
#########################################################################
"""
def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"
    
while True:
    
    try:
        op1=int(input("Introduce operador1: "))
        op2=int(input("Introduce operador2: "))
        break
    except ValueError:
        print("Valor introducido incorrecto. Intentalo de nuevo")
 
  
print("El resultado de la división es: " + str(op1) + "/"+str(op2)+"= "+str(dividir(op1,op2)))
print("Uno o más valores introducidos no son correctos")
    
print("Aquí hay más líneas de código importante...")
"""
"""
def divide():
    #capturar varias excepciones consecutivamente
    try:
        op1=float(input("Introduce op1: "))
        op2=float(input("Introduce op2: "))
        print("La división es: "+str(op1/op2))
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("Error al dividir entre 0")
    finally: #esto se ejecuta siempre independientemente que se capture la excepción o no
        print("Cálculo finalizado")
    
divide()
"""
"""
def evaluaEdad(edad):
    
    if edad<0:
        raise TypeError("No se permiten edades negativas") #Lanzamiento de excepciones       
    elif edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."

print(evaluaEdad(15))
"""
def calculaRaiz(num1):
    if num1 <0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un numero: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("Aquí hay más código....")
    




















