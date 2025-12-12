"""
POO que simula la gestión de un Restaurante

"""
from Modulo_Menu import Menu
from datetime import datetime,date
import random,os

class Mesa:
    
    def __init__(self,numero,capacidad):
        
        self.numero=numero
        self.capacidad=capacidad
        self.estado="libre"
  
    def reservar(self,numero):
        
        if self.numero==numero and self.estado=="libre":
        
            self.estado="ocupada"
            return True
        
        return False
    
    def liberar(self,numero):
        
        if self.numero==numero and self.estado=="ocupada":
        
            self.estado="libre"
            return True
    
        return False
    
    def esta_libre(self):
        #Devuelve True si está libre y False si está ocupada
        if self.estado=="libre":
            return True
        return False
    
    def __str__(self):
        return f"Mesa nº{self.numero} de {self.capacidad} comensales, está {self.estado}"

class Pedido:
    
    def __init__(self):
        
        self.lista_items=[]
        self.estado="en preparacion" #los estados pueden ser "en preparacion","servido"
        
        
    def agregar_item(self,item):
        
        self.lista_items.append(item)
    
    def remover_item(self,item):
        
        #comprobar si el item está en la lista, si está comprobamos si la cantidad es 1, en ese caso lo eliminamos
        #En caso contrario, le restamos uno a la cantidad y lo mantenemos en la lista de items
        
        if item in self.lista_items:
            
            if item.cantidad==1:
                self.lista_items.remove(item)
            else:
                item.cantidad-=1
            print("item eliminado correctamente")
            return True
        
        print("Error: No se ha podido eliminar el item")
        return False
    
    def calcular_total(self):
            
        total=0
        
        for i in self.lista_items:
        
            total+=int(i.precio)*int(i.cantidad)
        
        return f"El precio total del pedido es {total}€"
            
    def actualizar_estado(self,nuevo_estado):
        
        if self.estado!=nuevo_estado:
            
            self.estado=nuevo_estado
            
            return True
       
        return False
    
    def __str__(self):
        
        cadena="\n".join([str(vars(item)) for item in self.lista_items])
    
        return f"Lista de platos:\n\n{cadena}\n\nEstado del pedido: {self.estado}\n___________________________________________________________________\n"
    

class Carta:
    
    def __init__(self):
        
        self.lista_items=[]
    
    def agregar_item(self,ID,nombre,descripcion,precio):
        
        #Si el plato no está en el menú lo añade
        
        item=next((i for i in self.lista_items if i.ID==ID),None)
        
        if item==None:
            self.lista_items.append(ItemMenu(ID,nombre,descripcion,precio,0))
            print(f"El plato con ID:{ID} {nombre} {descripcion} precio: {precio}€ se ha añadido correctamente a la carta")
            return True
        
        print("Error: Ya existe un plato igual en el menu")
        return False
      
    
    def remover_item(self,ID):
        
        for i,item in enumerate(self.lista_items):
            
            if item.ID==ID:
            
                del self.lista_items[i]
                print(f"el item {ID} se ha eliminado correctamente del menu")
                return True
        
        print("Error:El plato no se encuentra en el menu")
        return False
    
    def buscar_item(self,ID):
        
        return next((i for i in self.lista_items if i.ID==ID),None)
        
                
    def mostrar(self):
        
        print(f"\n_________________ ###### CARTA ###### _________________\n")
        
        for i,item in enumerate(self.lista_items):
            print(f"{item}")
        
        print(f"\n_______________________________________________________\n")
        
        
class ItemMenu:

    def __init__(self,ID,nombre,descripcion,precio,cantidad):
        
        self.ID=ID
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.cantidad=cantidad
        
    def __str__(self):
        return f"ID:{self.ID}\t{self.nombre}\t{self.descripcion}\tPrecio:{self.precio}€"
        
class Cliente: 
    
    def __init__(self,nombre):
        
        self.nombre=nombre
        self.mesa_asignada=0
        self.pedido_actual=Pedido()
       
    def asignar_mesa(self,numero):
       self.mesa_asignada=numero
        
    def realizar_pedido(self,list_of_items):
        
        for item in list_of_items:
            self.pedido_actual.agregar_item(item)
        
        self.pedido_actual.estado="servido"
    
    def solicitar_cuenta(self):
        return self.pedido_actual.calcular_total()
    
    def __str__(self):
        return f"Cliente:{self.nombre}\tMesa:{self.mesa_asignada}\t{self.pedido_actual}"

 
class Restaurante:
    
    def __init__(self,nombre):
        
        self.nombre=nombre
        self.lista_mesas=[]
        self.lista_clientes=[]
        self.carta=Carta()
    
    def añadir_mesas(self,numero,capacidad):
        
        #comprobar si el número de mesa está repatido
        if next((mesa for mesa in self.lista_mesas if mesa.numero==numero),None)==None:
        
            self.lista_mesas.append(Mesa(numero,capacidad))
            print(f"Mesa {numero} con capacidad para {capacidad} personas se ha añadido")
            return True
        
        print(f"Error: Ya existe una mesa con el número {numero}")
        return False
    
    
    def eliminar_mesas(self,numero):
        
        #comprobar si el número de mesa está en la lista de mesas
        mesa=next((mesa for mesa in self.lista_mesas if mesa.numero==numero),None)
        
        if mesa!=None:
        
            self.lista_mesas.remove(mesa)
            print(f"Mesa {numero} se ha eliminado")
            return True
        
        print(f"Error: No existe una mesa con el número {numero}")
        return False
    
    
    def liberar_mesas(self,numero):
        
        mesa=next((m for m in self.lista_mesas if m.numero==numero),None)
        
        if mesa!=None:
        
            mesa.liberar(numero)
        
            return True
        
        return False
    
    def asignar_mesa(self,numero):
        
        mesa=next((m for m in self.lista_mesas if m.numero==numero),None)
        
        if mesa!=None:
        
            mesa.reservar(numero)
            
            return True
        
        return False
        
    
    def reservar_mesa(self,cliente,capacidad):
        
        #comprobamos si el cliente no está en la lista de clientes, en ese caso
        #buscamos la mesa en la lista de mesas del restaurante la que esté libre
        #y tenga la capacidad adecuada (mayor o igual a la pasada como parámetro)
        
        if next((c for c in self.lista_clientes if c.nombre==cliente.nombre),None)==None:
        
            for mesa in self.lista_mesas:
                
                if mesa.capacidad==capacidad and mesa.estado=="libre":
                    
                    cliente.asignar_mesa(mesa.numero)
                    self.asignar_mesa(mesa.numero)
                    self.lista_clientes.append(cliente)
                    print(f"Reservada realizada correctamente.\nSe ha asignado a {cliente.nombre} la mesa {mesa.numero} que disfrutes de la comida")
                    return True
            
            print("Error: No hay mesas disponibles")
            return False
        
        else:
            print(f"Error: el cliente ya tiene una mesa reservada en este restaurante")
            return False
    
    def cancelar_reserva(self,cliente):
        
        #Cancelar reserva (sólo se podrá cancelar si no se ha hecho un pedido)
        #buscamos al cliente, su mesa asignada y comprobamos el estado del pedido_actual
        #eliminamos al cliente de la lista y liberamos la mesa
        
        miCliente=next((c for c in self.lista_clientes if c.nombre==cliente.nombre),None)
        
        if miCliente!=None and miCliente.pedido_actual.estado!="servido":
            
            mesa=next((m for m in self.lista_mesas if m.numero==miCliente.mesa_asignada),None)
            self.liberar_mesas(mesa.numero)
            self.lista_clientes.remove(miCliente)
            print(f"Se ha cancelado correctamente la reserva de {miCliente.nombre} y se ha liberado la mesa {mesa.numero}")
            return True
        
        print("Error: No ha sido posible cancelar la reserva. No existe este cliente")
        return False
    
    def pagar(self,cliente):
        
        # Acciones que realiza este método:
        # Mostrar la cuenta
        # Liberar la mesa
        # eliminar al cliente de la lista de clientes del restaurante
        
        miCliente=next((c for c in self.lista_clientes if c.nombre==cliente.nombre),None)
        mesa=next((m for m in self.lista_mesas if m.numero==miCliente.mesa_asignada),None)
        
        self.mostrar_cuenta(miCliente)
        self.liberar_mesas(mesa.numero)
        self.lista_clientes.remove(miCliente)
        
        
    def buscar_cliente(self,nombre):
        
        return next((c for c in self.lista_clientes if c.nombre==nombre),None)
            
                    
    def gestionar_pedido(self,cliente,items):
        
        if cliente in self.lista_clientes:
        
            cliente.realizar_pedido(items)
            print("Pedido realizado correctamente")
            return True
        
        print("Error: No ha sido posible realizar el pedido")
        return False
            
    
    def mostrar_cuenta(self,cliente):
        
        if cliente in self.lista_clientes:
        
            print(cliente.solicitar_cuenta())
            return True
        
        return False
    
    def mostrar_mesas_disponibles(self):
        
        for mesa in self.lista_mesas:
            print(mesa)

    def mostrar_clientes(self):
     
        for cliente in self.lista_clientes:
            print(cliente)

class Ejecutable:
    
    def __init__(self):
        
        miRestaurante=Restaurante("Pachuparselosdedos")
        miCarta=Carta()
        
        lista_menu=["Mostrar mesas","Actualizar mesas",
                    "Mostrar carta","Actualizar la carta",
                    "Mostrar reservas","Actualizar reserva",
                    "Hacer pedido","Pagar"]
        
        salir=False
    
        while not salir:
            os.system('cls')
            opcion_elegida=Menu(f"RESTAURANTE {miRestaurante.nombre}",lista_menu).crear_menu()
        
            if opcion_elegida == 1: #Mostrar mesas
                
                if not miRestaurante.lista_mesas:
                    print("El restaurante no tiene mesas asignadas todavía")
                
                else:
                    miRestaurante.mostrar_mesas_disponibles()
                
                input("Presiona Enter para continuar...")
            
            elif opcion_elegida == 2: #Actualizar mesas
                while True:
                    try:
                        opcion=int(input(f"1. Añadir mesa\n2. Eliminar mesa\n3. Salir\n"))
                        if opcion>=1 and opcion<=3:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1:
                    while True:
                        try:
                            numero=int(input(f"Introduce el número de mesa: "))
                            capacidad=int(input(f"Introduce la capacidad de la mesa: "))
                            miRestaurante.añadir_mesas(numero,capacidad)
                            break
                        except:
                            print("Opción incorrecta")
        
            
                elif opcion==2:
                    while True:
                        try:
                            numero=int(input(f"Introduce el número de mesa: "))
                            miRestaurante.eliminar_mesas(numero)
                            break
                        except:
                            print("Opción incorrecta")
                    
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 3: #Mostrar carta
                
                miCarta.mostrar()                
                
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 4: #Actualizar carta
                
                while True:
                    try:
                        opcion=int(input(f"1. Añadir plato\n2. Eliminar plato\n3. Salir\n"))
                        if opcion>=1 and opcion<=3:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1:
                    while True:
                        try:
                            ID=int(input(f"Introduce el ID del plato: "))
                            nombre=input(f"Introduce el nombre del plato: ")
                            descripcion=input(f"Introduce la descripción del plato: ")
                            precio=int(input("Introduce el precio del plato: "))
                            miCarta.agregar_item(ID,nombre,descripcion,precio)
                            break
                        except:
                            print("Opción incorrecta")
        
            
                elif opcion==2:
                    while True:
                        try:
                            ID=int(input(f"Introduce el ID del plato: "))
                            miCarta.remover_item(ID)
                            break
                        except:
                            print("Opción incorrecta")
                    
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 5: #Mostrar reservas
                
                miRestaurante.mostrar_clientes()
                
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 6: #Actualizar reservas
                
                while True:
                    try:
                        opcion=int(input(f"1. Añadir reserva\n2. Cancelar reserva\n3. Salir\n"))
                        if opcion>=1 and opcion<=3:
                            break
                        input("Opción incorrecta")
                    except:
                        print("Opción incorrecta")
                        
                if opcion==1: #Añadir reserva
                    while True:
                        try:
                            nombre=input(f"Introduce nombre del cliente: ")
                            capacidad=int(input(f"Introduce el número de comensales: "))
                            miRestaurante.reservar_mesa(Cliente(nombre),capacidad)            
                            break
                        except:
                            print("Opción incorrecta")
                    
                elif opcion==2: #Cancelar reserva
                    while True:
                        try:
                            nombre=input(f"Introduce nombre del cliente: ")
                            miRestaurante.cancelar_reserva(Cliente(nombre))
                            break
                        except:
                            print("Opción incorrecta")
                
                input("Presiona Enter para continuar...")
                 
                 
            elif opcion_elegida == 7: #Hacer pedido
                
                lista_items=[]
                nombre=input("Introduce el nombre del cliente: ")
                miCliente=miRestaurante.buscar_cliente(nombre)
                
                while True:
                    
                    ID=int(input("Introduce el ID del plato: "))
                    cantidad=int(input("Introduce la cantidad: "))
                    
                    while True:
                        respuesta=input("Pulsa C para Continuar con el pedido o S para Salir y enviar el pedido: ").lower()
                        if respuesta!="s" and respuesta!="c":
                            print("Opción incorrecta")
                        else:
                            break
                    

                    Item=miCarta.buscar_item(ID)   
                        
                    item=next((item for item in lista_items if item.ID==ID),None)
                    
                    if item==None:
                        miItem=ItemMenu(Item.ID,Item.nombre,Item.descripcion,Item.precio,Item.cantidad)
                        miItem.cantidad=cantidad
                        lista_items.append(miItem)     
                    else:
                        
                        lista_items.remove(item)
                        item.cantidad+=cantidad
                        lista_items.append(item)
                            
                    if respuesta=="s": 
                        miRestaurante.gestionar_pedido(miCliente,lista_items)
                        print("__________________________________________________")
                        break
                                        
                input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 8: #Pagar
                
                try:
                    miRestaurante.pagar(miCliente)
                    
                except:
                    print("Error: No ha sido posible mostrar la cuenta")
                    
                print("__________________________________________________")
                input("Presiona Enter para continuar...")
                 
            else:
                salir=True
                

"""
    BUGS:
    
    - Control de excepciones, especialmente en la entrada de datos tipo int

    NUEVA IMPLEMENTACION:
  

"""
    
################################

Ejecutable()

