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
        self.estado_pedido="en preparación"
        
        
    def agregar_item(self,item):
        
        #comprobar si el item está en la lista, si está sumamos uno a la cantadidad actual, sino lo añadimos
        
        if item in self.lista_items:
            item.cantidad+=1
            
        else:           
            self.lista_items.append(item)
        
        print("Item añadido correntamente")
    
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
        
        if self.estado_pedido!=nuevo_estado:
            
            self.estado_pedido=nuevo_estado
            
            return True
       
        return False
    
    def __str__(self):
        
        cadena="\n".join([str(vars(item)) for item in self.lista_items])
    
        return f"Lista de platos:\n\n{cadena}\n\nEstado del pedido: {self.estado_pedido}"
    

class Carta:
    
    def __init__(self):
        
        self.lista_items=[]
    
    def agregar_item(self,ID,nombre,descripcion,precio):
        
        #Si el plato no está en el menú lo añade
        
        item=next((i for i in self.lista_items if i.ID==ID),None)
        
        if item==None:
            self.lista_items.append(ItemMenu(ID,nombre,descripcion,precio,1))
            return True
        
        print("Error: Ya existe un plato igual en el menu")
        return False
      
            
    
    def remover_item(self,ID):
        
        for i,id in enumerate(self.lista_items):
            
            if id==ID:
            
                del self.lista_items[i]
                print(f"el item {id} se ha eliminado correctamente del menu")
                return True
        
        print("Error:El plato no se encuentra en el menu")
        return False
        
                
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
        
        self.pedido_actual.estado_pedido="servido"
    
    def solicitar_cuenta(self):
        return self.pedido_actual.calcular_total()
    
    def __str__(self):
        return f"Cliente Nombre:{self.nombre}\tMesa asignada:{self.mesa_asignada}\tPedido: {self.pedido_actual}"

 
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
            print(f"La mesa {numero} liberada correctamente")
            return True
        
        print("Error: No ha sido posible liberar la mesa")
        return False
    
    def mostrar_mesas_disponibles(self):
        
        for mesa in self.lista_mesas:
            print(mesa)

    def mostrar_clientes(self):
     
        for cliente in self.lista_clientes:
            print(cliente)
     
    
    def reservar_mesa(self,cliente,numero_mesa,capacidad):
        
        #comprobamos si la mesa cumple las condiciones para que se pueda reservar: 
        # 1. que el numero esté en la lista de mesas del restaurante
        # 2. que esté libre
        # 3. que tenga la capacidad correcta
        
        mesa=next((mesa for mesa in self.lista_mesas if mesa.numero==numero_mesa and mesa.estado=="libre" and mesa.capacidad<=capacidad),None)
        
        if mesa!=None:
            mesa.estado="ocupada"
            cliente.asignar_mesa(numero_mesa)
            self.lista_clientes.append(cliente)
            return True
        
        print(f"Error: La mesa {numero_mesa} no está disponible")
        return False
           
        
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
        
        print("Error: No ha sido posible mostrar la cuenta")
        return False
    

class Ejecutable:
    
    def __init__(self):
        
        miRestaurante=Restaurante("Pachuparselosdedos")
        
        lista_menu=["Mostrar mesas","Actualizar mesas",
                    "Mostrar carta","Actualizar la carta",
                    "Mostrar reservas","Actualizar reserva",
                    "Mostrar pedidos","Hacer pedido","Pagar"]
        
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
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 4: #Actualizar carta
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 5: #Mostrar reservas
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 6: #Actualizar reservas
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 7: #Mostrar pedidos
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 8: #Hacer pedido
                 input("Presiona Enter para continuar...")
                 
            elif opcion_elegida == 9: #Pagar
                 input("Presiona Enter para continuar...")
                 
            else:
                salir=True
                
        
"""

Opciones:

MESAS

1.Mostrar mesas disponibles
2.Añadir mesas
3.Eliminar mesas
4.Liberar mesa

MENU
1.Mostrar Carta
2.Añadir plato a la carta
3.Eliminar plato de la carta

RESERVAS

5.Mostrar reservas
6.Reservar mesa
7.Cancelar reserva 

PEDIDOS

8.Mostrar pedidos
9.Añadir item al pedido
10.Eliminar item pedido
11.Enviar pedido
12.Servir pedido
13.Mostrar cuenta


"""

    
################################

Ejecutable()

# p1=ItemMenu("01","pizza","Carbonara","12","1")
# p2=ItemMenu("02","pizza","Margarita","15","2")
# p3=ItemMenu("03","pizza","Boloñesa","10","3")
# p4=ItemMenu("04","pizza","Barbacoa","14","1")
# p5=ItemMenu("05","pizza","Peperoni","11","2")
# # miPedido=Pedido()
# # miPedido.agregar_item(p1)
# # miPedido.agregar_item(p2)
# # miPedido.agregar_item(p3)
# # miPedido.agregar_item(p4)
# # miPedido.agregar_item(p5)
# # print(miPedido)
# # print(miPedido.calcular_total())
# # miMenu=Menu()
# # miMenu.agregar_item("01","pizza","Carbonara","12")
# # miMenu.agregar_item("02","pizza","Margarita","15")
# # miMenu.agregar_item("03","pizza","Boloñesa","10")
# # miMenu.agregar_item("04","pizza","Barbacoa","14")
# # miMenu.agregar_item("05","pizza","Peperoni","11")
# # miMenu.mostrar()

# c1=Cliente("juan")
# c2=Cliente("maria")
# lista_platos=[p1,p2,p3]
# #c1.realizar_pedido(lista_platos)
# # print(miCliente.pedido_actual)
# # print(miCliente.solicitar_cuenta())

# miRestaurante=Restaurante()
# miRestaurante.añadir_mesas(1,4)
# miRestaurante.añadir_mesas(2,2)
# miRestaurante.añadir_mesas(3,6)
# miRestaurante.añadir_mesas(4,8)
# miRestaurante.mostrar_mesas_disponibles()
# print("_______________")


# miRestaurante.reservar_mesa(c1,4,6)
# miRestaurante.reservar_mesa(c2,3,5)
# miRestaurante.gestionar_pedido(c2,lista_platos)
# #miRestaurante.mostrar_clientes()
# miRestaurante.mostrar_mesas_disponibles()
# print("#################")
# print("Vamos a pedir la cuenta...")
# miRestaurante.mostrar_cuenta(c2)
# print("Nos vamos del restaurante...")
# miRestaurante.liberar_mesas(3)
# #miRestaurante.reservar_mesa(c2,3)
# #miRestaurante.mostrar_clientes()
# miRestaurante.mostrar_mesas_disponibles()



# # print(plato1)
# # mesa1=Mesa(1,4)
# # print(mesa1)
# # mesa1.reservar(1)
# # print(mesa1)
# # if mesa1.esta_libre():
# #     mesa1.reservar(1)
# # else:
# #     mesa1.liberar(1)
    
# # print(mesa1)