from tkinter import *

################ Creamos la raiz (ventana) #####################################

raiz=Tk()
raiz.title("Ventana de pruebas")
#raiz.resizable(0,0) #Width,Heigh 0,0 significa que no deja cambiar el tamaño de la ventana
raiz.iconbitmap("icono_Juan.ico") 
raiz.geometry("850x450")
#raiz.config(bg="green") #color de fondo de la ventana

##################################################################################

############## Creamos el frame (lienzo para introducir los widgets) #############

miFrame=Frame(raiz,width="650",height="350")
miFrame.pack(fill="both",expand="True") #El frame se expande con el tamaño de la ventana
#miFrame.pack()
miFrame.config(bg="red")
miFrame.config(bd=35) #grosor del borde
miFrame.config(relief="ridge")
miFrame.config(cursor="hand2")
###################################################################################

############ WIDGET Label #########################################################
# Permite introducir texto estático
miImagen=PhotoImage(file="foto_Juan.gif") 
Label(miFrame,text="Hola como estás?",fg="red",font=("Comic Sans MS",18)).place(x=100,y=200)
Label(miFrame,image=miImagen).place(x=400,y=50)


###################################################################################


raiz.mainloop() #siempre tiene que estar al fina y es como un bucle infinito que está ejecutando constamente la ventana para que esté a la escucha de eventos

#### NOTA: Me he quedado en el video 44 del curso de pildorasinformaticas###



