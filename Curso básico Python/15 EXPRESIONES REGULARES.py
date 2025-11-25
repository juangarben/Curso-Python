####################### EXPRESIONES REGULARES o REGEX ####################################
#
# Son una secuencia de caracteres que forman un patrón de búsquedas normalmente de textos
#
##########################################################################################

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender",cadena))

textoBuscar="aprender"

if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")


textoEncontrado=re.search(textoBuscar,cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

textoBuscar="Python"

print(len(re.findall(textoBuscar,cadena)))

lista_nombres=["Sandra Gómez",
               "María Martin",
               "Sandra López",
               "Santiago Martin"
               ]

for elemento in lista_nombres:
    if re.findall("^Sandra",elemento): # ^significa que empieza por
        print(elemento)
    if re.findall("Martin$",elemento): # $significa que termina por
        print(elemento)
    if re.findall("[z]",elemento): # [] significa que contine
        print(elemento)
    if re.findall("[o-t]",elemento): # [] rango entre la o y la t
        print(elemento)

#NOTA Me he quedado en el vídeo 71


