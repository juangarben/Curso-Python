# En este programa simularemos  una sala de cine que tiene un conjunto de asientos (8 filas por 8 columnas= 64). OK

# Del cine nos interesa conocer la película que se está reproduciendo y el precio de la entrada en el cine. OK

# De las películas nos interesa saber el título, duración, edad mínima y director. OK

# Del espectador, nos interesa saber su nombre, edad y el dinero que tiene. OK

# Los asientos son etiquetados por una letra (columna) y un número (fila), la fila 1 empieza al final de la matriz como se muestra en la tabla. También deberemos saber si está ocupado o no el asiento.

# 1 A B C D E F G H 
# 2 A B C D E F G H 
# 3 A B C D E F G H 
# 4 A B C D E F G H 
# 5 A B C D E F G H 
# 6 A B C D E F G H 
# 7 A B C D E F G H 
# 8 A B C D E F G H 

# Al llamar a la clase cine generaremos muchos espectadores y los sentaremos aleatoriamente (no podemos donde ya este ocupado). OK
# En esta versión sentaremos a los espectadores de uno en uno.

# Solo se podrá sentar si:
#     - Tienen el suficiente dinero
#     - Hay espacio libre
#     - Tiene edad para ver la película
    
# En caso de que el asiento este ocupado le buscamos uno libre. OK

# Los datos del espectador y la película pueden ser totalmente aleatorios.

################################################################################

import os,random

os.system('cls')

class cine:
    
    def __init__(self,pelicula,precio):   #Lo primero que haremos será generar los asientos vacios de la sala
    
        self.pelicula=pelicula.titulo
        self.precio=precio
       
            
        self.asientos=[
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
                    ["A","B","C","D","E","F","G","H"],
        ]
        
        print(f"Hoy proyectamos la película: ### {self.pelicula} ####\n\nPrecio: {self.precio} €\nDuracion: {pelicula.duracion}\nEdad: {pelicula.edad}\nDirector: {pelicula.director}\n")
        
        
    def generar_asientos(self): #A continuación generamos los asientos aleatorios y marcamos con una X los que están ocupados
                                    
        for i in range(random.randint(1,64)):
            self.asientos[random.randint(0,7)][random.randint(0,7)]="X" 
        
        
    
    def imprimir_asientos(self):
            
        fila=1
        for i in self.asientos:
            print(fila,i)
            fila+=1
            
        print(f"Quedan {numero_asientos_libres()} asientos libres")
    
    def asignar_asiento(self,numero_entradas): #Este método asigna los asientos libres de forma automática y consecutiva
        
        num_fila=0
        num_columna=0
        self.num_entradas=numero_entradas
        asiento_asignado=False
        
        #Comprobamos si los asientos están ocupados y nos paramos en el primero que esté libre
        for i in range(self.num_entradas):
            
            while self.asientos[num_fila][num_columna]=="X" and contar_lista_2D(miSala.asientos,"X")<64:
                num_columna+=1
                if(num_columna==8):
                    num_columna=0
                    num_fila+=1
            
            if (contar_lista_2D(miSala.asientos,"X")<64):
                
                self.asientos[num_fila][num_columna]="X"
                print(f"Te hemos asignado el asiento {num_fila+1}{convertir_nombre_columna(num_columna)}\n")
                print("------------------------------------------------")
                self.imprimir_asientos() 
                asiento_asignado=True
            else:
                print("No quedan asientos libres")
                return False
        
        return asiento_asignado
    
    def elegir_asiento(self):
        
        #Devolvemos una lista con los asientos libres
        
        lista_asientos=[]
        
        for i in range(8):
            for j in range(8):
                lista_asientos.append(str(i+1)+self.asientos[i][j])
                    
        lista_asientos_libres = [item for item in lista_asientos if "X" not in item]
        
        #Comprobamos si el asiento elegido está disponible (libre) y en caso afirmativo lo asignamos
        
        while True:
        
            numero_asiento=input("Indica el número de asiento que quieres reservar: ")
        
            if numero_asiento in lista_asientos_libres:
                self.asignar_asiento_2(numero_asiento)
                print(f"Perfecto asiento {numero_asiento} reservado")
                self.imprimir_asientos()
                break
            else:
                print(f"Lo siento el asiento {numero_asiento} no está disponible. Inténtalo de nuevo")
                
    def asignar_asiento_2(self,numero_asiento): #Este método asigna el asiento elegido
        num_fila=int(numero_asiento[0])-1
        num_columna=int(convertir_numero_columna(numero_asiento[1]))
        self.asientos[num_fila][num_columna]="X"

class pelicula:
    
    def __init__(self,titulo,duracion,edad,director):
        
        self.titulo=titulo
        self.duracion=duracion
        self.edad=edad
        self.director=director
    

class espectador():
    
    def __init__(self,nombre,edad,dinero):
        self.nombre=nombre
        self.edad=edad
        self.dinero=dinero
        print(f"\nHola soy: {self.nombre}, tengo {self.edad} años, llevo {self.dinero} € para ir hoy al cine")
        
    def comprar_entrada(self,cine,pelicula):
        
        # Solo se podrá sentar si:
#     - Tienen el suficiente dinero
#     - Hay espacio libre
#     - Tiene edad para ver la película

        self.numero_entradas=0    
        self.numero_asientos_libres=numero_asientos_libres()
        self.respuesta="S"
        
        while True:
            if (self.numero_asientos_libres>0):
                try:
                    self.numero_entradas=int(input(f"Cuantas entradas quieres comprar {self.nombre}?: "))
                    if(self.numero_entradas==0):
                        print ("Debe seleccionar un número de entradas mayor que 0")
                    else:
                        break
                except:
                    print("Valor de entrada incorrecto, debes introducir un valor numérico entero")
            else:
                break  
           
        
        while (self.numero_entradas>self.numero_asientos_libres):
            
            if(self.numero_entradas==0):
                break
                
            self.respuesta=input(f"Lo siento, quedan {self.numero_asientos_libres} asientos libres.\n¿Quieres seguir con el proceso de compra (S/N) ? ")
                
            if (self.respuesta=="S"):
                    
                try:
            
                    self.numero_entradas=int(input("Cuantas entradas quieres comprar?: "))
        
                except:
                    print("Lo siento el número de entradas debe ser un valor numérico, prueba otra vez.")
                
            else:
                break    
                
        if(self.numero_asientos_libres<64 and self.respuesta=="S" and self.numero_entradas>0):
            
            if(self.edad>=pelicula.edad):
                
                if(self.dinero>=self.numero_entradas*cine.precio):
                    
                    for i in range(self.numero_entradas):
                        cine.elegir_asiento()
                        
                    return True
                
                else:
                    print(f"Lo siente no tienes suficiente dinero para comprar {self.numero_entradas} entrada/s")
                    return False
            else:
                print("Lo siento no tienes la edad mínima para ver esta película")
                return False
        elif(self.respuesta!="S"):
            print("Proceso de compra abortado. Que tengas un buen día, hasta pronto!")
            return False
        else:
            print("Lo siento no quedan butacas libres")
            return False
    
###################################################################################        

def contar_lista_2D(lista,valor_a_buscar):

    contador = 0

    for fila in lista:
        for elemento in fila:
            if elemento == valor_a_buscar:
               contador += 1
    
    return contador    
######################################################################################          

def numero_asientos_libres():
    
    numero_asientos_libres=64-contar_lista_2D(miSala.asientos,"X")    
    return numero_asientos_libres

#######################################################################################

def convertir_nombre_columna(num_columna):
    dic_asientos={"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H"}
    return dic_asientos[str(num_columna)]

#######################################################################################

def convertir_numero_columna(nombre_columna):
    dic_asientos={"A":"0","B":"1","C":"2","D":"3","E":"4","F":"5","G":"6","H":"7"}
    return dic_asientos[str(nombre_columna)]
########################################################################################

mipelicula=pelicula("Regreso al futuro",120,12,"Robert Zemeckis")
miSala=cine(mipelicula,5)
#miSala.imprimir_asientos()

print("\nGenerando asientos ocupados....\n")
miSala.generar_asientos()
miSala.imprimir_asientos()

espectador1=espectador("Juan",12,10000)
espectador1.comprar_entrada(miSala,mipelicula)
     
espectador2=espectador("Estefanía",12,1000)
espectador2.comprar_entrada(miSala,mipelicula)
  

