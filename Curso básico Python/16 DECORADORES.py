################################## DECORADORES ###############################
#
# Funciones que añaden funciones "decoran " a otras funciones ya existentes
# Se trata de 3 funciones A,B,C donde A recibe a B como parámetro y devuelve C
#
##############################################################################

############ La estructura de un decorador es la siguiente: ##################

def funcion_decorador(funcion):
    def funcion_interna():
     #codigo de la funcion interna
     return funcion_interna

##############################################################################

def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():
        
        #Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")
        
        funcion_parametro()
        
        #Acciones adicionales que decoran
        print("Hemos terminado el calculo")
        
    return funcion_interior
        

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora    
def resta():
    print(30-10)
    
suma()
resta()

#NOTA: Me he quedado en el vídeo 73


