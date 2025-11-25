# Uso de métodos de cadenas de caracteres (string) --> Esto es muy habitual en cualquier lenguaje de progranación
# Consulta documentación de phyton: https://docs.python.org/3/
"""
nombreUsuario=input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario.upper()) #Lo pasa a mayúsculas
print("El nombre es: ", nombreUsuario.lower()) #Lo pasa a minúsculas
print("El nombre es: ", nombreUsuario.capitalize()) #Primera letra en maýusculas

edad=input("Introduce la edad: ")
print(edad.isdigit()) #Devuelve True o False depediendo si introducimos un número o no
"""
##############  EJERCICIO #####################################
# Enunciado: Comprobar si la dirección de email es OK o NOK dependiendo de las siguientes condiciones:
# Si tiene una @ es OK siempre y cuando:
# Si tiene más de una @ NOK
# Si no tiene @ NOK
# Si la @ está al comienzo de la dirección de email NOK
# Si la @ está al final de la direción de email NOK
################### SOLUCION ##################################

email=input("Introduce tu dirección de email: ")
      
if (email.count("@")==1 and email.find("@")!=0 and email.rfind("@")!=len(email)-1 ):
    print("email CORRECTO")
else:
    print("email INCORRECTO")
    

        


