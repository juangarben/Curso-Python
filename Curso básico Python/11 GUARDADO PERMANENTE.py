# ************************************************************************************
# GUARDADO PERMANENTE:
    
# Ejemplo de código para guardar información binaria (lista de objetos) en un fichero permanente

# ************************************************************************************

import pickle

class Persona:
    
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de:",self.nombre)
        
    def __str__(self):
        # return "{} {} {}".format(self.nombre,self.genero,self.edad) 
        return f"{self.nombre} {self.genero} {self.edad}" # alternativa de código usando f-string a partir de python 3.6

class ListaPersonas:
    
    personas=[]
    
    def __init__(self): #Vamos a guardar miLista en un fichero externo        
    
        listaDePersonas=open("ficheroExterno","ab+") #ab=agregar información binaria
        listaDePersonas.seek(0) #Desplazamos el cursor al principio del fichero
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se ha cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
        
    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)
    
    
miLista=ListaPersonas()

p=Persona("Sandra","Femenino",29)
miLista.agregarPersonas(p)

p=Persona("Antonio","Masculino",39)
miLista.agregarPersonas(p)

miLista.mostrarInfoFicheroExterno()







    