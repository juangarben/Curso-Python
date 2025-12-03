from Modulo_Menu import Menu
import random

class Usuario:
    
    def __init__(self,nombre,password,num_cuenta):
        self.__nombre=nombre
        self.__password=password
        self.__num_cuenta=num_cuenta
        self.saldo=0
        self.logging=False
        
    def Inicia_sesion(self,nombre,password):
        
        if nombre==self.__nombre and password==self.__password:
            print("### Logging correcto!! ###")
            self.logging=True
            return True
        else:
            self.logging=False
            return False
            
            
    def __str__(self):
        
        return f"\nNombre: {self.__nombre}\tPassword: {self.__password}\tCCC:{self.__num_cuenta}\tSaldo:{self.saldo}\n"
            

class Cajero_automatico:
    def __init__(self):
        pass
        
    
    def Hazte_cliente(self):
        nombre=input("Introduce un nombre usuario: ")
        password=input("Introduce un password: ")
        ccc= random.randint(10000000, 99999999)
        return Usuario(nombre,password,ccc)
        
    
    def Consulta_saldo(self,usuario):
    
        print(usuario)
            
    
    def Retirar_efectivo(self,usuario,cantidad):
        if usuario.saldo>=cantidad:
           usuario.saldo-=cantidad
        else:
            print("Error: No hay saldo suficiente")
        
    
    def Ingresar_efectivo(self,usuario,cantidad):
        usuario.saldo+=cantidad
    
    

class Ejecutable:
    
    def __init__(self):
        
        opciones_menu=["Hazte cliente","Inicio Sesión","Consulta Saldo","Retirada efectivo","Ingreso efectivo"]
        lista_usuarios=[]
        self.salir=False
        self.logging=False
    
        while not self.salir:
            self.opcion_elegida=Menu("Cajero Automático",opciones_menu).crear_menu()
            
            if self.opcion_elegida==1: #Hazte cliente
                
                lista_usuarios.append(Cajero_automatico.Hazte_cliente(self))
                print("### Usuario registrado correctamente ###")
                print(lista_usuarios[-1])
                input("Presiona Enter para continuar...")

            elif self.opcion_elegida==2: #Inicia sesión
                try:
                    nombre_usuario_answ=input("Introduce el nombre de usuario: ")
                    password_answ=input("Introduce la clave: ")
                    contador=0
                    
                    for usuario in lista_usuarios:
                        if usuario.Inicia_sesion(nombre_usuario_answ,password_answ):
                            miUsuario=usuario
                            self.logging=True
                            break
                        else:
                            contador+=1
                            self.logging=False
                    
                    if contador==len(lista_usuarios):
                        print("Usuario o clave incorrectos")
                        
                    input("Presiona Enter para continuar...")
                    
                    
                except:
                    print("Error: No existe este usuario. Debes hacerte cliente primero")
                    input("Presiona Enter para continuar...")
                
                
            elif self.opcion_elegida==3:
             
                try:
                    if self.logging:
                        Cajero_automatico.Consulta_saldo(self,miUsuario)
                        input("Presiona Enter para continuar...")
                    else:
                        print("Error: Para consultar el saldo debes loggearte primero")
                        input("Presiona Enter para continuar...")
                except:
                    print("Error: Para consultar el saldo debes loggearte primero")
                    input("Presiona Enter para continuar...")
        
            
            elif self.opcion_elegida==4:
                
                try:
                    if self.logging:
                        cantidad=int(input("Indica la cantidad de dinero que quieres retirar: "))
                        Cajero_automatico.Retirar_efectivo(self,miUsuario,cantidad)
                        print("### Retirada de efectivo realizada correctamente ###")
                        input("Presiona Enter para continuar...")
                    else:
                        print("Error: Para retirar efectivo debes loggearte primero")
                        input("Presiona Enter para continuar...")
                except:
                    print("Error: Para retirar efectivo debes loggearte primero")
                    input("Presiona Enter para continuar...")
                
                            
                
            elif self.opcion_elegida==5:
                
                try:
                    if self.logging:
                        cantidad=int(input("Indica la cantidad de dinero que quieres ingresar: "))
                        Cajero_automatico.Ingresar_efectivo(self,miUsuario,cantidad)
                        print("### Ingreso realizado correctamente!!! ###")
                        input("Presiona Enter para continuar...")
                    else:
                        print("Error: Para ingresar efectivo debes loggearte primero")
                        input("Presiona Enter para continuar...")
                except:
                    print("Error: Para ingresar efectivo debes loggearte primero")
                    input("Presiona Enter para continuar...")
                
                
            else:
                self.salir=True
        

######################################################################################################################

Ejecutable()

""" Mejoras a implementar:
    
    1.- que ponga el nombre de usuario en el menu
    2.- que se puedan hacer transferencias entre usuarios
    3.- que te tengas que desloggear para volver a iniciar sesión
    
"""
