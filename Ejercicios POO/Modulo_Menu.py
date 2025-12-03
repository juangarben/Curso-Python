import os,random

os.system('cls')

class Menu:
    
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
        num_orden=1
        
        for opciones in self.lista_menu:
            print(f"{num_orden}. {opciones}\n")
            num_orden+=1
            
        
        print(f"{num_orden}. Salir")
        print("______________________________________________________________________\n")
        
        
        while not self.salir:
            
            try:
                
                self.opcion=int(input("Elige una opcion: "))
                
                if self.opcion>0 and self.opcion<num_orden:
                    
                    self.salir=True
                    return self.opcion
                    
                    
                elif self.opcion==num_orden: 
                    input(f"Hasta pronto!!\nPresiona Enter para continuar...")
                    self.salir=True
                    return 0
                
                else:
                    input(f"Error opción no válida.\nPresiona Enter para continuar...")
                    self.refrescar()
                    return self.opcion
                    
                # if opcion>0 and opcion<7:
                        
                #     if (opcion==1):#Listar contactos
                        
                #         self.Agenda.listarContactos()
                                                
                #         input("Presiona Enter para continuar...")
                #         self.refrescar()
            
                #     if (opcion==2): #Añadir contacto
                        
                #         nombre_contacto=input("Introduce el nombre: ")
                #         telefono_contacto=input("Introduce el teléfono: ")
                #         Contacto=contacto(nombre_contacto,telefono_contacto)
                #         self.Agenda.aniadirContacto(Contacto)
                        
                #         input("Presiona Enter para continuar...")
                #         self.refrescar()
                        
                #     if (opcion==3): #Eliminar contacto
                        
                #         nombre_eliminar=input("Introduce el nombra a eliminar: ")
                #         self.Agenda.eliminarContacto(nombre_eliminar)
                        
                #         input("Presiona Enter para continuar...")
                #         self.refrescar()
                    
                    
                #     if (opcion==4): #Buscar contacto
                        
                #         nombre_buscar=input("Introduce el nombre a buscar: ")
                #         self.Agenda.buscaContacto(nombre_buscar)
                        
                #         input("Presiona Enter para continuar...")
                #         self.refrescar()
                            
                #     if (opcion==5): #Consultar huecos agenda
                    
                #         self.Agenda.huecosLibres()
                    
                #         input("Presiona Enter para continuar...")
                #         self.refrescar()
                            
                #     if (opcion==6):
                    
                #         print("Hasta pronto!!!")
                #         input("Presiona Enter para continuar...")
                #         self.salir=True
                
                # # else:
                #     print("Error: Opción incorrecta.")
                    
                #     input("Presiona Enter para continuar...")
                #     self.refrescar()
            
            except:
                input(f"Error opción no válida.\nPresiona Enter para continuar...")
                self.refrescar()
                return self.opcion
                

# opciones_menu=["Crear usuario","Iniciar Sesion","Consultar Saldo","Retirar efectivo","Ingresar Efectivo","Hacer Transferencia"]
# miMenu=Menu("banco",opciones_menu)
# print(miMenu.crear_menu())
            