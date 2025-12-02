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
        self.puntos_acumulados=0
        self.preguntas=[]
        
        self.lista_valores=[]
        self.diccionario_preguntas={}
        self.diccionario_respuestas={}
        self.diccionario_puntuacion={}
       
    def cargarPreguntas(self):
       
        # cargarPreguntas(String fichero): carga todas las preguntas del fichero y las guarda en varios diccionarios (preguntas, respuestas y puntuación)
        
        with open(self.fichero, "r") as fichero:
            
            lista=fichero.readlines()
            
            for linea in lista:
                
                if ";P;" in linea:
                    clave=linea.strip()[5:]
                    
                elif "Opcion" in linea:
                    
                    self.lista_valores.append(linea.strip()[2:])
                    self.diccionario_preguntas[clave]=self.lista_valores
                
                elif ";R;" in linea:
                    
                    self.diccionario_respuestas[clave]=int(linea.strip()[5:])
                    self.lista_valores=[]
                    
                elif "Puntos" in linea:
                    
                    self.diccionario_puntuacion[clave]=int(linea.strip()[21:])
                    self.lista_valores=[]
                    
                else:        
                     self.lista_valores=[]
            
        # for clave, valor in self.diccionario_preguntas.items():
        #     print(f"{clave}: {valor}\n")
        
        # print("_________________Respuestas__________________________")
        # for clave, valor in self.diccionario_respuestas.items():
        #     print(f"{clave}: {valor}\n")
        
        # print("_________________Puntuacion__________________________")
        # for clave, valor in self.diccionario_puntuacion.items():
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
        self.preguntas=list(self.diccionario_preguntas.keys()) #lista de preguntas
        
        for i in range(len(self.diccionario_preguntas)):
            
            pregunta.mostrarPregunta(self,self.numero_pregunta)
            
            while True:
                try:
                    respuesta=int(input("Indica la opción correcta: "))
                    break
                except:
                    print("Error: Opcion incorrecta")
            
            
            if pregunta.comprobar_Respuesta(self,respuesta,self.preguntas[self.numero_pregunta-1]):
                print("Enhorabuena!. La respuesta es correcta")
                self.puntos_acumulados+=self.diccionario_puntuacion[self.preguntas[self.numero_pregunta-1]]
                
            else:
                print("Lo siento respuesta incorrecta")
            
            self.siguientePregunta()
        
        print(f"\n____________________ PUNTUACIÓN {self.puntos_acumulados} ______________________\n")
        pregunta.getAtributos(self)
        
                    
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
        
        
        print(f"\n{self.preguntas[self.num_pregunta]}\n")
        
        
        for item in self.diccionario_preguntas[self.preguntas[self.num_pregunta]]:
            print(opcion(self,item).texto_opcion)
                    
            
    def comprobar_Respuesta(self,respuesta_usuario,num_pregunta):
        #comprobarRespuesta(int respuestaUsuario): comprueba la respuesta del usuario si es correcta o no.
        if respuesta_usuario==self.diccionario_respuestas[num_pregunta]:
        
            return True
            
        else:
           
            return False
    
    def getAtributos(self):
        #Indica la pregunta, las opciones, la respuesta y los puntos. Mostramos cada diccionario
        print(f"Diccionario de preguntas y opciones:\n\n{self.diccionario_preguntas}\n")
        print(f"Diccionario de preguntas y respuestas:\n\n{self.diccionario_respuestas}\n")
        print(f"Diccionario de preguntas y puntos:\n\n{self.diccionario_puntuacion}\n")
        

class opcion(pregunta):
    # Una opción se compone de:
    # El texto de la opción (digamos la respuesta)
    # Es correcto o no
    
    def __init__(self,fichero,texto_opcion,correcto=False):
        super().__init__(fichero)
        self.texto_opcion=texto_opcion
        self.correcto=correcto
        
        
        
######################################################################################################################

miTest=test(r"C:\Users\Juan Antonio\Documents\curso phyton\Ejercicios POO\test.txt")

print(f"_______ Empezamos el test .... ________________\n")
miTest.realizarTest()
print("_______________________")





