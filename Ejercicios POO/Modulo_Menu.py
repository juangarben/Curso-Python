
import os,random

os.system('cls')

class Menu:
    """Clase Menu: Crea un menú en la consola
    
    Argumentos: titulo y lista de strings con las distintas opciones del menú (el último índice de la lista es "salir" y se genera automáticamente)
    
    Methods:
    - refrescar()
        refresca la pantalla cada vez que hay un error al elegir una opcion
    

    Returns:
        - un int con la opcion del menu seleccionada, 0 si se selecciona salir
    """
    
    def __init__(self,titulo="",lista_menu=[]):
        self.titulo=titulo
        self.lista_menu=lista_menu
        self.salir=False
        self.opcion=0
        
    def refrescar(self):
        
        os.system('cls')
        self.crear_menu()
    
    def crear_menu(self):
        
        print(f"__________________________ MENU: {self.titulo}  ______________________________\n")
        
 # Crea un menú con opciones pasadas como argumento de la lista por consola para probar todas estas funcionalidades.
        
        for num_orden,opciones in enumerate(self.lista_menu,1):
            print(f"{num_orden}. {opciones}\n")
        
        print(f"{num_orden+1}. Salir")
        print("______________________________________________________________________\n")
        
        while not self.salir:
            
            try:
                
                self.opcion=int(input("Elige una opcion: "))
                
                if self.opcion>0 and self.opcion<=num_orden:
                    
                    self.salir=True
                    return self.opcion
                    
                    
                elif self.opcion==num_orden+1: 
                    input(f"Hasta pronto!!\nPresiona Enter para continuar...")
                    self.salir=True
                    return 0
                
                else:
                    input(f"Error opción no válida.\nPresiona Enter para continuar...")
                    self.refrescar()
                    return self.opcion
                    
            except:
                input(f"Error opción no válida.\nPresiona Enter para continuar...")
                self.refrescar()
                return self.opcion
                

            