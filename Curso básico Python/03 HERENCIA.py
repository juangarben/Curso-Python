"""
HERENCIA de clases:
    - Clase padre o superclase
    - Subclase
    - Sirve para reutilizar código en caso de crear objetos similares
    

"""

#Clase padre o superclase
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
        
#Creamos una clase hijo (por ejemplo Furgoneta) que hereda de la clase padre Vehículo por lo que tendrá todas las propiedades y métodos de la clase padre
class Furgoneta(Vehiculo):
    
    def carga(self,cargar):
        
        self.cargado=cargar
        
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
        

#Creamos una clase hijo (por ejemplo Moto) que hereda de la clase padre Vehículo por lo que tendrá todas las propiedades y métodos de la clase padre
class Moto(Vehiculo):
    
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self): #sobreescritura de método
        print("Marca: ", self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelara,"\nFrenando: ",self.frena,"\n",self.hcaballito)
        

class VElectricos(): #Esta clase no hereda de Vehiculos
    
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando=True
        
class BicicletaElectrica(VElectricos,Vehiculo): #Herencia Múltiple. Los parámetros del constructor son de la primera clase que heredemos en este caso VElectricos. 
                                                #Si hubiera más metodos que tuvieran el mismo nombre, se da preferencia a la primera clase que se hereda en este caso VElectricos
    pass
    
    
          

miMoto=Moto("Honda","CBR") #Hay que pasarle los parámetros del constructor de la clase padre
miMoto.caballito()
miMoto.estado()
print("-------------------------------------------------")
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("-------------------------------------------------")
miBici=BicicletaElectrica("Orbea","HJ500") #Al crear el objeto miBici instanciando la clase BicicletaElectrica no le pasamos parámetros de constructor porque está tomando la de VElectricos
miBici.estado()