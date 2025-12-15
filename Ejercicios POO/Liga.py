"""POO que simula una liga de equipos
"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os

class Equipo:
    
    def __init__(self,nombre):
        self.nombre=nombre
        self.puntos=0
        self.GF=0
        self.GC=0
        self.resultado=0
        
    def __str__(self):
        return f"{self.nombre:<10}{self.puntos} puntos\tGF:{self.GF}\tGC:{self.GC}\n"
        
        
class Partido:
    def __init__(self,equipo_local,equipo_visitante,jornada):
        self.equipo_local=equipo_local
        self.equipo_visitante=equipo_visitante
        self.jornada=jornada
        self.resultado={}
        
    def Jugar(self):
        self.equipo_local.resultado=random.randint(0,7)
        self.equipo_visitante.resultado=random.randint(0,7)
        self.equipo_local.GF+=self.equipo_local.resultado
        self.equipo_local.GC+=self.equipo_visitante.resultado
        self.equipo_visitante.GF+=self.equipo_visitante.resultado
        self.equipo_visitante.GC+=self.equipo_local.resultado
        
        if self.equipo_local.resultado>self.equipo_visitante.resultado:
            self.equipo_local.puntos+=3
            
        elif self.equipo_local.resultado<self.equipo_visitante.resultado:
            self.equipo_visitante.puntos+=3         
        else:
            self.equipo_local.puntos+=1
            self.equipo_visitante.puntos+=1
            
        self.resultado={self.equipo_local.nombre:self.equipo_local.resultado,self.equipo_visitante.nombre:self.equipo_visitante.resultado}
        
    def __str__(self):
        
        cadena=str(self.resultado)
        return f"Resultado Jornada: {self.jornada}\n{cadena}"
    

class Liga:
    
    def __init__(self,lista_equipos):
        self.lista_equipos=lista_equipos
   
        
    def tabla_equipos(self):
        
        #Generamos la combinación de partidos:
        
        jornada=1
        
        for i in range(len(self.lista_equipos)-1):
            for j in range(i+1,len(self.lista_equipos)):
                if i!=j:
                    miPartido=Partido(self.lista_equipos[i],self.lista_equipos[j],jornada)
                    miPartido.Jugar()
                    print(miPartido)
                    print(f"_______________________________________________________\n")
                    jornada+=1
      
    
    def imprimir_clasificacion(self):
        
        #ordenamos la lista por puntos de forma descendente (de mayor a menor):
        # 1 puntos
        # 2 duferencia de goles
        # 3 goles a favor
        
        lista_equipos_ordenada=sorted(self.lista_equipos,key=lambda equipo:(equipo.puntos,equipo.GF-equipo.GC,equipo.GF),reverse=True) 
                    
        for posicion,equipo in enumerate(lista_equipos_ordenada,1):
            print(posicion,equipo)
       

class Ejecutar:
    
    def __init__(self):
        
        miLiga=Liga([])
        lista_equipos=[]
    
        lista_menu=["Añadir equipos",
                    "Eliminar equipos",
                    "Jugar liga",
                    "Buscar equipo",
                    "Clasificación"]
        
        salir=False
        
        while not salir:
            
            os.system('cls')
            opcion_elegida=Menu(f"LIGA",lista_menu).crear_menu()
            
        
            if opcion_elegida == 1: #Añadir equipos
                
                while True:
                    
                    nombre=input("Introduce el nombre del equipo: ")
                    
                    if next((e for e in lista_equipos if e.nombre==nombre),None)==None:
                        lista_equipos.append(Equipo(nombre))
                    else:
                        print("Error: El equipo ya existe, prueba con otro nombre")
                                                                
                    while True:
                        respuesta=input("Continuar (C) o Salir (S): ").lower()
                        if respuesta!="s" and respuesta!="c":
                            print("Opción incorrecta")
                        else:
                            break
                
                    if respuesta=="s": 
                        
                        print(f"\n###############################################\n")
                        miLiga=Liga(lista_equipos)
                        miLiga.imprimir_clasificacion()
                        break
                
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida == 2: #Eliminar equipos
                    
                nombre=input("Introduce el nombre del equipo: ")
                
                equipo=next((e for e in lista_equipos if e.nombre==nombre),None)
                if equipo!=None:
                    lista_equipos.remove(equipo)
                else:
                    print("Error: Equipo no encontrado")
                                    
                print(f"\n###############################################\n")
                miLiga=Liga(lista_equipos)
                miLiga.imprimir_clasificacion()
                    
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 3: #Jugar Liga
                
                miLiga.tabla_equipos()
                
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 4: #Buscar equipo
                nombre=input("Introduce el nombre del equipo: ")
                    
                equipo=next((e for e in lista_equipos if e.nombre==nombre),None)
                if equipo!=None:
                    print(equipo)
                else:
                    print("Error: El equipo no existe")
            
                input("Presiona Enter para continuar...")
                                  
            elif opcion_elegida == 5: #Clasificacion
                
                print(f"\n############## CLASIFICACIÓN ##############################\n")
                miLiga.imprimir_clasificacion()
                print(f"\n###########################################################\n")
                                        
                input("Presiona Enter para continuar...")
                      
            else:
                salir=True

##################################################################################################

Ejecutar()


