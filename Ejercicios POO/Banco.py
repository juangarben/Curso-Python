

from Modulo_Menu import Menu
import random,os
#help(Menu)

class Usuario:
    
    def __init__(self,nombre,password,num_cuenta):
        self.nombre=nombre
        self.password=password
        self.num_cuenta=num_cuenta
        self.saldo=0
        self.logging=False
        self.descubierto=0
        
    def Inicia_sesion(self,nombre,password):
        
        if nombre==self.nombre and password==self.password:
            print(f"### Bienvenido {self.nombre} ###")
            self.logging=True
            return True
        else:
            self.logging=False
            return False
            
            
    def __str__(self):
        
        return f"\nNombre: {self.nombre}\tPassword: {self.password}\tCCC:{self.num_cuenta}\tSaldo:{self.saldo}\tServicio Descubierto:{self.descubierto}\n"
            

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
        
        nueva_cantidad=usuario.saldo-cantidad
        
        if nueva_cantidad>=0:
               usuario.saldo-=cantidad
               
        elif abs(nueva_cantidad)<=usuario.descubierto:
                usuario.saldo-=cantidad
        else:    
            print("Error: No hay saldo suficiente")
                                
    
    def Ingresar_efectivo(self,usuario,cantidad):
        usuario.saldo+=cantidad
        
    def Hacer_transferencia(self,usuario_origen,usuario_destino,cantidad):
        #La transferencia sólo se puede hacer si hay suficiente saldo en la cuenta de origen
        nueva_cantidad=usuario_origen.saldo-cantidad
        
        if nueva_cantidad>=0:
               usuario_origen.saldo-=cantidad
               usuario_destino.saldo+=cantidad
               return True
               
               
        elif abs(nueva_cantidad)<=usuario_origen.descubierto:
                usuario_origen.saldo-=cantidad
                usuario_destino.saldo+=cantidad
                return True
        else:    
            return False
    
        
    
class Ejecutable:
    
    def __init__(self):
        
        opciones_menu=["Hazte cliente","Iniciar Sesión","Retirar efectivo","Ingresar efectivo","Hacer transferencia","Contratar descubirto","Cerrar Sesión","Cancelar Cuenta","Acceso Administrador"]
        self.lista_usuarios=[]
        self.salir=False
        self.logging=False
    
        while not self.salir:
            os.system('cls')
            
            if self.logging:
                try:
                    print(miUsuario)
                except:
                    pass
            
            self.opcion_elegida=Menu("Cajero Automático",opciones_menu).crear_menu()
            
            
            if self.opcion_elegida==1: #Hazte cliente
                
                if not self.logging:
                    self.lista_usuarios.append(Cajero_automatico.Hazte_cliente(self))
                    print("### Usuario registrado correctamente ###")
                    print(self.lista_usuarios[-1])
                
                else:
                    print("Error: Ya hay una sesión iniciada. Debes cerrar sesión para registrar un nuevo cliente")
                
                input("Presiona Enter para continuar...")

            elif self.opcion_elegida==2: #Inicia sesión
                try:
                    if not self.logging:
                        nombre_usuario_answ=input("Introduce el nombre de usuario: ")
                        password_answ=input("Introduce la clave: ")
                        contador=0
                        
                    
                        for usuario in self.lista_usuarios:
                            if usuario.Inicia_sesion(nombre_usuario_answ,password_answ):
                                miUsuario=usuario
                                self.logging=True
                                break
                            else:
                                contador+=1
                                self.logging=False
                        
                        if contador==len(self.lista_usuarios):
                            print("Usuario o clave incorrectos")
                    else:
                        print("Error: Ya hay una sesión iniciada, debes cerrar sesión si quieres cambiar de usuario")        
                        
                    input("Presiona Enter para continuar...")
                    
                    
                except:
                    print("Error: No existe este usuario. Debes hacerte cliente primero")
                    input("Presiona Enter para continuar...")
                
            
            elif self.opcion_elegida==3: #Retirar efectivo
                
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
                
                            
                
            elif self.opcion_elegida==4: #Ingresar efectivo
                
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
            
            elif self.opcion_elegida==5: #Hacer transferencia
                try:
                    usuario_destino_ok=True
                    contador=0
                    
                    if self.logging:
                        usuario_destino=input("Indica el nombre del usuario destino: ")
                        cantidad_transferencia=float(input("Indica la cantidad que quieres transferir: "))
                        
                        
                        for usuario in self.lista_usuarios:
                            
                            if usuario.nombre==usuario_destino:
                            
                                miUsuario_destino=usuario
                                break
                            
                            else:
                                contador+=1
                        
                        if contador==len(self.lista_usuarios):
                            print("Error: El usuario de destino no existe")
                            input("Presiona Enter para continuar...")
                            usuario_destino_ok=False
                            
                        if usuario_destino_ok:
                            if(Cajero_automatico.Hacer_transferencia(self,miUsuario,miUsuario_destino,cantidad_transferencia)):
                                print("Transferencia realizada correctamente")
                                input("Presiona Enter para continuar...")
                            else:
                                print("Error: No hay saldo suficiente")
                                input("Presiona Enter para continuar...")
                            
                                    
                    else:
                        print("Error: Para hacer una transferencia debes loggearte primero")
                        input("Presiona Enter para continuar...")
            
                        
                
                except:
                    print("Error: Para hacer una transferencia debes loggearte primero")
                    input("Presiona Enter para continuar...")
            
                            
            elif self.opcion_elegida==6: #Contratar descubierto
                try:
                    if self.logging:
                        
                        cantidad_descubierto=float(input(f"Indica la cantidad máxima de descubierto que quieres contratar: "))
                        coste_descubierto=cantidad_descubierto*0.1
                        respuesta=input(f"El coste del servicio de descubierto es: {coste_descubierto}€. Quieres continuar?(S/N)")
                        if respuesta=="S" or respuesta=="s":
                            if miUsuario.saldo>=coste_descubierto:
                                miUsuario.descubierto=cantidad_descubierto
                                miUsuario.saldo-=coste_descubierto
                                print(f"Servicio de descubierto contratado, ahora tu cuenta se puede quedar en negativo hasta {cantidad_descubierto}€")
                                input("Presiona Enter para continuar...")
                            else:
                                print(f"Error: No tienes suficiente saldo para contratar el servicio de descubierto")
                                input("Presiona Enter para continuar...")
                                
                    else:
                        print("Error: Para contratar el servicio debes loggearte primero")
                        input("Presiona Enter para continuar...")
                except:
                    print("Error: Para ingresar efectivo debes loggearte primero")
                    input("Presiona Enter para continuar...")      
                    
            elif self.opcion_elegida==7: #Cerrar Sesión
                try:
                    if self.logging:
                        
                        self.logging=False
                        print(f"Hasta pronto {miUsuario.nombre}!!!!")
                        input("Presiona Enter para continuar...")
                        
                    else:
                        print("Error: No se ha iniciado sesión previamente")
                        input("Presiona Enter para continuar...")
                    
                except:
                        print("Error: No se ha iniciado sesión previamente")
                        input("Presiona Enter para continuar...")
                    
                
                
            elif self.opcion_elegida==8: #Cancelar cuenta
                try:
                    if self.logging:
                    
                        respuesta=input(f"¿Estás seguro que quieres borrar el usuario:{miUsuario.nombre} (S/N)?")
                        
                        if respuesta=="S" or respuesta=="s":
                            if miUsuario.saldo == 0:
                                
                                self.lista_usuarios.remove(miUsuario)
                                self.logging=False
                                print("El usuario ha sido eliminado")
                                input("Presiona Enter para continuar...")
                            else:
                                print("Error: No es posible eliminar la cuenta, la cuenta tiene saldo")
                                input("Presiona Enter para continuar...")
                    else:
                        print("Error: No se ha iniciado sesión previamente")
                        input("Presiona Enter para continuar...")
                except:
                    print("Error: No se ha iniciado sesión previamente")
                    input("Presiona Enter para continuar...")
                    
            elif self.opcion_elegida==9: #Acceso adimnistrador
                
                if self.logging:
                    
                    print("Error: Ya hay un usuario loggeado. Debes de cerrar sesión")
                    input("Presiona Enter para continuar...")
                
                else:
                    password=input("Introduce el password del administrador: ")
                    
                    if password=="admin":
                    
                        print(f"\n ______________________ Lista de usuarios registrados _______________________________\n")
                        for usuario in self.lista_usuarios:
                            print(usuario)
                        print(f"\n_______________________________________________________________________\n")
                        
                        input("Presiona Enter para continuar...")
                        
                        
                        
                    else:
                        
                        print("Error: password incorrecto")
                        input("Presiona Enter para continuar...")
                    
                    
            else:
                self.salir=True
        
######################################################################################################################

Ejecutable()

