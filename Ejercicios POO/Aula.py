# Queremos representar con programación orientada a objetos, un aula con estudiantes y un profesor.

# Tanto de los estudiantes como de los profesores necesitamos saber su nombre, edad y sexo. --> OK

# De los estudiantes, queremos saber también su calificación actual (entre 0 y 10) y del profesor que materia da. --> OK

# Las materias disponibles son matemáticas, filosofía y física. 

# Los estudiantes tendrán un 50% de hacer novillos, por lo que si hacen novillos no van a clase pero aunque no vayan quedara registrado en el aula (como que cada uno tiene su sitio). --> OK

# El profesor tiene un 20% de no encontrarse disponible (reuniones, baja, etc.) --> OK

# Las dos operaciones anteriores deben llamarse igual en Estudiante y Profesor (polimorfismo). --> OK

# El aula debe tener un identificador numérico, el número máximo de estudiantes y para que esta destinada (matemáticas, filosofía o física). Piensa que más atributos necesita. -->OK


# NOTA: Los datos pueden ser aleatorios (nombres, edad, calificaciones, etc.) siempre y cuando tengan sentido (edad no puede ser 80 en un estudiante o calificación ser 12).

import os,random

os.system('cls')

class Persona:
    #Atributos: nombre,edad, sexo
    def __init__(self, nombre,edad,sexo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    
class Profesor(Persona):
    #Atributos: materia (matemáticas, filosofía, física), Absentismo (20%)
    def __init__(self,nombre,edad,sexo,materia):
        super().__init__(nombre,edad,sexo)
        self.materia=materia
        self.ausencia=0
        self.disponibilidad=True
    
    def Absentismo(self,ausencia):
        
        self.ausencia+=ausencia
        if (self.ausencia<=20):
            self.disponibilidad=True
        else:
            self.disponibilidad=False
        
    
class Estudiante(Persona):
    #Atributos: calificación (entre 0 y 10), Absentismo (50%)
    
    def __init__(self,nombre,edad,sexo,calificacion,aula):
        super().__init__(nombre,edad,sexo)
        self.calificacion=calificacion
        self.ausencia=0
        self.disponibilidad=True
        self.aula=aula
        self.aula.lista_alumnos.append(self) #Añade los estudiantes a la lista del aula cuando se crea el objeto
        
            
    def Absentismo(self,ausencia):
        
        self.ausencia+=ausencia
        if (self.ausencia<=50):
            self.disponibilidad=True
        else:
            self.disponibilidad=False
            self.aula.lista_alumnos.remove(self) #Elimina un estudiante de la lista del aula cuando la estudiante.disponibilidad==False
    

class Aula:
    #Atributos: ID, num_max_estudiantes,materia
    def __init__(self,ID,num_max_estudiantes,materia,profesor,lista_alumnos):
        self.ID=ID
        self.num_max_estudiantes=num_max_estudiantes
        self.materia=materia
        self.lista_alumnos=lista_alumnos
        self.profesor=profesor
        self.lista_materias_disponibles=["matemáticas","física","filosofía"]
        self.lista_alumnos_masculina=[]
        self.lista_alumnos_femenina=[]
    
    def DarClase(self):
        # Un aula para que se pueda dar clase necesita que el profesor esté disponible, 
        # que el profesor de la materia correspondiente en el aula correspondiente (un profesor de filosofía no puede dar en un aula de matemáticas)
        # y que haya más del 50% de alumnos.
       
        if (self.materia in self.lista_materias_disponibles and self.profesor.disponibilidad and self.profesor.materia==self.materia and len(self.lista_alumnos)>=0.5*self.num_max_estudiantes and len(self.lista_alumnos)<=self.num_max_estudiantes):
            print("Sí es posible dar clase. Los siguientes alumnos están aprobados:")
            self.Notas()
            return True
        else:
            print("No es posible dar clase")
            return False
    
    def Notas(self):
        # Si se puede dar clase mostrar cuantos alumnos y alumnas (por separado) están aprobados de momento (imaginad que les están entregando las notas).
        #Recorrer la lista de alumnos y separar por sexos > 5 APROBADOS
        #Nombre Alumnos aprobados y nota
        #Nombre Alumnas aprobadas y nota:
        
        for i in self.lista_alumnos:
            if(getattr(i,"sexo")=="M"):
                self.lista_alumnos_femenina.append(i)
            else:
                self.lista_alumnos_masculina.append(i)
        
        print("___________________\nSEXO FEMENINO:\n____________________")
        for i in self.lista_alumnos_femenina:
            if (getattr(i,"calificacion")>=5):
                nombre=getattr(i,"nombre")
                nota=getattr(i,"calificacion")
                print(f"{nombre} Nota:{nota}")
        
        print("\n__________________\nSEXO MASCULINO:\n___________________")
        for i in self.lista_alumnos_masculina:
            if (getattr(i,"calificacion")>=5):
                nombre=getattr(i,"nombre")
                nota=getattr(i,"calificacion")
                print(f"{nombre} Nota:{nota}")
        print("\n____________________________________________\n")

############### POLIMORFISMO ###################

def Absentismo(persona,ausencia):
    #devuelve True si el profesor está disponible y False si no lo está 
    
    return persona.Absentismo(ausencia)

##################################################


################################################
# El objetivo es crear un aula de alumnos y un profesor y determinar si puede darse clase, teniendo en cuenta las condiciones antes dichas.
####################################################

lista_alumnos=[]

Profesor1=Profesor("Juan",50,"H","matemáticas")


Aula1=Aula("A01",11,"matemáticas",Profesor1,lista_alumnos)

ALU_1=Estudiante("Pepito",12,"H",4,Aula1)
ALU_2=Estudiante("Jaimito",12,"H",3,Aula1)
ALU_3=Estudiante("Eva",12,"M",7,Aula1)
ALU_4=Estudiante("Maria",12,"M",3,Aula1)
ALU_5=Estudiante("Ester",12,"M",9,Aula1)
ALU_6=Estudiante("Manolito",12,"H",7,Aula1)
ALU_7=Estudiante("Joselito",12,"H",2,Aula1)
ALU_8=Estudiante("Anita",12,"M",8,Aula1)
ALU_9=Estudiante("Paloma",12,"M",8,Aula1)
ALU_10=Estudiante("Carlitos",12,"H",10,Aula1)
ALU_11=Estudiante("Javier",12,"H",10,Aula1)


Absentismo(Profesor1,20)
Absentismo(ALU_3,51)

Aula1.DarClase()
    
    











