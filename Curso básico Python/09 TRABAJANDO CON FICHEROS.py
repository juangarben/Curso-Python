################### TRABAJANDO CON FICHEROS DE TEXTO EXTERNOS ###################
#################################################################################

import io #importamos la libreria io de Python para trabajar con ficheros

#####   ESCRITURA ######
archivo_texto=open("archivo.txt","w")
Frase="Esto es una frase de prueba\n para ver que estoy incluyendo texto en el archivo"
archivo_texto.write(Frase)
#archivo_texto.writelines(lista) #agrega una lista al texto
archivo_texto.close()

##### LECTURA #####
archivo_texto=open("archivo.txt","r")
#texto=archivo_texto.read()
#print(texto)
lineas_texto=archivo_texto.readlines() #guarda cada linea de texto en una lista
archivo_texto.close()
#print(lineas_texto[0])
#print(lineas_texto[1])

##### LECTURA Y ESCRITURA #####
#archivo_texto=open("archivo.txt","r+")

##### AGREGAR (APPEND) text a un archivo existente #####

archivo_texto=open("archivo.txt","a")
archivo_texto.write("\nEsto es una nueva línea")
archivo_texto.close()

##### PUNTEROS (posición del cursor) de texto, por defecto cuando abrimos el archivo la posición es la primnera y cuando lo cerramos es la última posición

archivo_texto=open("archivo.txt","r")
#archivo_texto.seek(11) #muestra el texto a partir del caracter 11
print(archivo_texto.read(11)) #muestra el texto hasta la posición del caracter 11



