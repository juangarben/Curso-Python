# Nos piden hacer un almacén, vamos a usar programación orientado a objetos.

# En un almacén se guardan un conjunto de  bebidas.

# Estos productos son bebidas como agua mineral y refrescos (coca-cola, fanta, etc). De los productos nos interesa saber su identificador (cada uno tiene uno distinto), cantidad de litros, precio y marca.

# Si es agua mineral nos interesa saber también el origen (manantial tal sitio o donde sea).

# Si es una bebida azucarada queremos saber el porcentaje que tiene de azúcar y si tiene o no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).

# En el almacén iremos almacenado estas bebidas por estanterías (que son las columnas de la matriz).

# Puedes usar un main para probar las funcionalidades (añade productos, calcula precios, muestra información, etc)

import os,random

os.system('cls')

class Almacen: # En el almacén iremos almacenado estas bebidas por estanterías (que son las columnas de la matriz).
    
    def __init__(self):
        
        self.estanteria_agua_mineral=[]
        self.estanteria_refrescos=[]
        
    
    def Cacular_Precio_Total_Almacen(self): # Calcular precio de todas las bebidas: calcula el precio total de todos los productos del almacén.
        
        precio_total_almacen=sum([bebida.precio for bebida in self.estanteria_agua_mineral]) + sum([bebida.precio for bebida in self.estanteria_refrescos])
        print(f"El precio de las bebidas del almacén es: {precio_total_almacen}€")
    
    def Calcular_Precio_Total_Marca(self,marca): # Calcular el precio total de una marca de bebida: dada una marca, calcular el precio total de esas bebidas.
        
        lista_marca_especifica=[]
        
        if marca in [item.marca for item in self.estanteria_agua_mineral]: #Lo primero a qué tipo de bebida pertene la marca (Agua mineral o Refresco)
            for item in self.estanteria_agua_mineral:#A continuación guardamos en una lista las bebidas almacenadas de la marca específica y sumamos el precio total de la estantería
                if item.marca==marca:
                    lista_marca_especifica.append(item)    

        elif marca in [item.marca for item in self.estanteria_refrescos]: #Lo primero a qué tipo de bebida pertene la marca (Agua mineral o Refresco)
            for item in self.estanteria_refrescos:#A continuación guardamos en una lista las bebidas almacenadas de la marca específica y sumamos el precio total de la estantería
                if item.marca==marca:
                    lista_marca_especifica.append(item)    
        
        print(f"El precio total de la marca {marca} es: {sum([item.precio for item in lista_marca_especifica])}€")
        
    
    def Calcular_Precio_Total_Estanteria(self): # Calcular el precio total de una estantería: dada una estantería (columna) calcular el precio total de esas bebidas.
        
        
        precio_total_agua_mineral=sum([bebida.precio for bebida in self.estanteria_agua_mineral])
        print(f"El precio total de la estanteria de Agua Mineral es: {precio_total_agua_mineral} €")
        
        precio_total_refrescos=sum([bebida.precio for bebida in self.estanteria_refrescos])
        print(f"El precio total de la estanteria de Refrescos es: {precio_total_refrescos} €")
        
    
    def Agregar_Productos(self,bebida):
        # Agregar producto: agrega un producto en la primera posición libre, 
        # si el identificador esta repetido en alguno de las bebidas, no se agregará esa bebida.
        
        self.bebida=bebida
        
        if isinstance(self.bebida,AguaMineral):
        
            if not bebida.ID in [bebida.ID for bebida in miAlmacen.estanteria_agua_mineral]:
                self.estanteria_agua_mineral.append(bebida)   
            else:
                print(f"Error: El ID: {bebida.ID} ya está en la estantería. No se puede repetir.")
        
        if isinstance(self.bebida,Refrescos):
        
            if not bebida.ID in [bebida.ID for bebida in miAlmacen.estanteria_refrescos]:
                self.estanteria_refrescos.append(bebida)   
            else:
                print(f"Error: El ID: {bebida.ID} ya está en la estantería. No se puede repetir.")
        
    
    def Eliminar_Producto(self,ID): # Eliminar un producto: dado un ID, eliminar el producto del almacén.
        
        lista_ID_agua_mineral=[bebida.ID for bebida in self.estanteria_agua_mineral]
        lista_ID_refrescos=[bebida.ID for bebida in self.estanteria_refrescos]
        
        
        if ID in lista_ID_agua_mineral:
    
            del self.estanteria_agua_mineral[lista_ID_agua_mineral.index(ID)]
                    
        
        elif ID in lista_ID_refrescos:
    
            del self.estanteria_refrescos[lista_ID_refrescos.index(ID)]
            
        else:
            print("Error: El ID no existe y por lo tanto no se puede eliminar de la estantería")
        
        
    def Mostrar_Informacion(self,bebida): # Mostrar información: mostramos para cada bebida toda su información.
        
        self.bebida=bebida  
        
        if isinstance(self.bebida,AguaMineral) and bebida.ID in [item.ID for item in self.estanteria_agua_mineral]:
            
            print(f"\nAGUA MINERAL:\nID: {self.bebida.ID}\nLitros: {self.bebida.litros}\nPrecio: {self.bebida.precio}\nMarca: {self.bebida.marca}\nOrigen: {self.bebida.origen}\n")
        
        
        elif isinstance(self.bebida,Refrescos)and bebida.ID in [item.ID for item in self.estanteria_refrescos]:
            
            print(f"\nREFRESO:\nID: {self.bebida.ID}\nLitros: {self.bebida.litros}\nPrecio: {self.bebida.precio}\nMarca: {self.bebida.marca}\nPorcentaje: {self.bebida.porcentaje}\nPromoción: {self.bebida.promocion}\n")
        
        else:
            print("Error: ID no encontrado")    
        
        
class Bebida:
    
    #Atributos: identificador, cantidad de litros, precio y marca.

    def __init__(self,ID,litros,precio,marca):
        
        self.ID=ID
        self.litros=litros
        self.precio=precio
        self.marca=marca

class AguaMineral(Bebida): # Si es agua mineral nos interesa saber también el origen (manantial tal sitio o donde sea).

    def __init__(self, ID, litros, precio, marca,origen="manantial"):
        super().__init__(ID, litros, precio, marca)
        self.origen=origen


class Refrescos(Bebida): #Si es una bebida azucarada queremos saber el porcentaje que tiene de azúcar y si tiene o no alguna promoción (si la tiene tendrá un descuento del 10% en el precio).
    
    def __init__(self, ID, litros, precio, marca,porcentaje,promocion=False):
        super().__init__(ID, litros, precio, marca)
        self.porcentaje=porcentaje
        self.promocion=promocion
        
        if self.promocion:
            self.precio=precio*0.9
        
##########################################################################################################
# Puedes usar un main para probar las funcionalidades (añade productos, calcula precios, muestra información, etc)

miAlmacen=Almacen()

AM1=AguaMineral("AM1",1,2,"lanjaron")
miAlmacen.Agregar_Productos(AM1)

AM2=AguaMineral("AM2",1,3.5,"bezoya")
miAlmacen.Agregar_Productos(AM2)

AM3=AguaMineral("AM3",1,4,"lanjaron")
miAlmacen.Agregar_Productos(AM3)

AM4=AguaMineral("AM4",1,3,"bezoya")
miAlmacen.Agregar_Productos(AM4)

RF1=Refrescos("RF1",1,1,"CocaCola",10)
miAlmacen.Agregar_Productos(RF1)

RF2=Refrescos("RF2",1,5,"CocaCola",10,True)
miAlmacen.Agregar_Productos(RF2)

RF3=Refrescos("RF3",1,1,"CocaCola",10)
miAlmacen.Agregar_Productos(RF3)

RF4=Refrescos("RF4",1,1,"CocaCola",10,True)
miAlmacen.Agregar_Productos(RF4)

miAlmacen.Mostrar_Informacion(AM3)
#miAlmacen.Eliminar_Producto("RF2")
#miAlmacen.Eliminar_Producto("AM2")
miAlmacen.Mostrar_Informacion(AM2)
miAlmacen.Cacular_Precio_Total_Almacen()
miAlmacen.Calcular_Precio_Total_Marca("lanjaron")
miAlmacen.Calcular_Precio_Total_Estanteria()






