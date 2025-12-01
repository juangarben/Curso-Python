# Una academia nos pide hacer un programa para hacer un pequeño test a sus alumnos.

# Estas preguntas, para facilitar la inclusión, estarán escritas en un txt (incluido en la descarga del proyecto).


# El fichero de preguntas tiene el siguiente formato:

# ;P;Pregunta 1

# Opción 1 pregunta 1

# Opción 2 pregunta 1

# Opción 3 pregunta 1

# Opción 4 pregunta 1

# ;R;Numero opción correcta

# Puntos pregunta 1

# ;P;Pregunta 2

# Opción 1 pregunta 2

# Opción 2 pregunta 2

########################################################

import os,random

os.system('cls')

class test:
    
    # Un test está formado por un conjunto preguntas y los puntos acumulados. Piensa que debemos saber por cual pregunta vamos.
    # Sus métodos son:

    def __init__(self, fichero):
        self.fichero=fichero
        self.numero_pregunta=1
       
    def cargarPreguntas(self):
       
        # cargarPreguntas(String fichero): carga todas las preguntas del fichero
        
        self.lista_valores=[]
        self.diccionario_preguntas={}
        
        with open(self.fichero, "r") as fichero:
            
            lista=fichero.readlines()
            
            for linea in lista:
                
                if ";P;" in linea:
                    clave=linea.strip()[5:]
                    
                elif "Opcion" in linea:
                    
                    self.lista_valores.append(linea.strip()[2:])
                    self.diccionario_preguntas[clave]=self.lista_valores
                
                elif ";R;" in linea:
                    self.lista_valores.append(linea.strip()[5:])
                    self.diccionario_preguntas[clave]=self.lista_valores
                
                elif "Puntos" in linea:
                    self.lista_valores.append(linea.strip()[21:])
                    self.diccionario_preguntas[clave]=self.lista_valores
                    self.lista_valores=[]
                    
                else:        
                     self.lista_valores=[]
            
        # for clave, valor in self.diccionario_preguntas.items():
        #     print(f"{clave}: {valor}\n")
                    
                    
    
    def siguientePregunta(self):
        # siguientePregunta(): devuelve la siguiente pregunt
        self.numero_pregunta+=1
        
    
    def reiniciarTest(self):
        # reiniciarTest(): nos permite reiniciar el test.
        self.numero_pregunta=1
    
    def realizarTest(self):
        # realizarTest(): empieza el test y empieza a formular las preguntas
        
        self.cargarPreguntas()
        for i in range(len(self.diccionario_preguntas)):
            pregunta.mostrarPregunta(self,self.numero_pregunta)
            self.siguientePregunta()
        
                    
class pregunta(test):
    # Una pregunta consta de:

    # Pregunta (tendrá delante dos puntos y coma ;P;)
    # Opciones de la pregunta (entre 2 y 4)
    # Opción correcta (tendrá delante dos puntos y coma ;R;)
    # Puntos
    # La pregunta no será válida en los siguientes casos:

    # Las opciones no están entre 2 y 4.
    # La opción correcta esta entre el número de opciones y es un número.
    # Los puntos es un número entero.
    # Sus métodos son:
    
    def __init__(self, fichero):
        super().__init__(fichero)
        
    def mostrarPregunta(self,num_pregunta):
        # mostrarPregunta(): muestra la pregunta con sus opciones.
        self.num_pregunta=num_pregunta-1
        claves=list(self.diccionario_preguntas.keys())
        print(claves[self.num_pregunta])
        
    def comprobarRespuesta(self,respuesta_usuario):
        # comprobarRespuesta(int respuestaUsuario): comprueba la respuesta del usuario si es correcta o no.
        respuesta=int(input("Indica la opción correcta: "))
        
        pass
    
    def getAtributos(self):
        #Indica la pregunta, las opciones, la respuesta y los puntos
        pass

class opcion(pregunta):
    # Una opción se compone de:
    # El texto de la opción (digamos la respuesta)
    # Es correcto o no
    
    def __init__(self, fichero,texto_opcion,correcto=False):
        super().__init__(fichero)
        self.texto_opcion=texto_opcion
        self.correcto=correcto
        
        
######################################################################################################################

fichero=r"C:\Users\Juan Antonio\Documents\curso phyton\Ejercicios POO\test.txt"
miTest=test(fichero)
miTest.cargarPreguntas()
print(f"_______ Empezamos el test .... ________________\n")
miTest.realizarTest()
print("_______________________")

# mi_diccionario = {"manzana": "rojo", "banana": "amarillo", "uva": "morado"}

# # Convertir el diccionario a una lista de claves
# print(list(mi_diccionario.keys()))


