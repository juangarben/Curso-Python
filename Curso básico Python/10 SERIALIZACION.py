"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
SERIALIZACIÓN

- Guardar en un fichero externo una lista, diccionario, objeto, colección, etc. en un fichero externo binario
- Libreria Python: Pickle (dump y load)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import pickle

# Guardamos un fichero binario con  una lista de nombres

lista_nombres=["Pedro","Ana","Maria","Isabel"]
fichero_binario=open("lista_nombres","wb") #escritura binaria
pickle.dump(lista_nombres,fichero_binario) #volcado de la lista en el fichero binario que acabamos de crear
fichero_binario.close()
del(fichero_binario) #debemos borrar el fichero de la memoria

# Leemos la información guardad en ek fichero binario

fichero_lectura=open("lista_nombres","rb") #lectura binaria
lista=pickle.load(fichero_lectura) #cargamos la información del fichero binario y la guardamos en una lista
print(lista)

# Guardamos una lista de objetos (colección)

class Vehiculo():
    
    def __init__(self,marca,modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelara=False
        self.frena=False
        
    def arrancar(self):
        
        self.enmarcha=True
    
    def acelearar(self):
        
        self.acelera=True
        
    def frenar(self):
        
        self.frena=True
        
    def estado(self):
        
        print("Marca: ", self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelara,"\nFrenando: ",self.frena)

coche1=Vehiculo("Mazda","MX5")
coche2=Vehiculo("Seat","Leon")
coche3=Vehiculo("Renault","Megane")

coches=[coche1,coche2,coche3] #lista de objetos Vehiculo

fichero=open("ListaCoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

#Vamos a recuperar la información de los objetos guardados en el fichero binario
ficheroApertura=open("ListaCoches","rb")
misCoches=pickle.load(ficheroApertura) #Lista de objetos
ficheroApertura.close()

for c in misCoches: #Recorremos la lista de objetos y llamamos al método estado
    print(c.estado())
