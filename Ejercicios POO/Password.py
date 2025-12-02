import math,os,random,string,re

os.system('cls')

class Password:
#Que tenga los atributos longitud y contraseña . Por defecto, la longitud sera de 8.

    def __init__(self,longitud=8):
        self.longitud=longitud
        self.password=self.generarPassword(self.longitud)#Generar contraseña aleatoria con esa longitud
        
    
    def generarPassword(self,longitud):
    # generarPassword():  genera la contraseña del objeto con la longitud que tenga.
        return (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters+string.digits, k=longitud)))

    def esFuerte(self):
    # esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener minimo de 2 mayúsculas, minimo de 1 minúscula y minimo de 1 números.
        
        mayusculas = len(re.findall(r'[A-Z]', self.password))
        minusculas = len(re.findall(r'[a-z]', self.password))
        numeros = len(re.findall(r'\d', self.password))
        print(f"Mayusculas: {mayusculas}\tMinúsculas: {minusculas}\t Números: {numeros}\n")
        
        if mayusculas>=2 and minusculas>=1 and numeros>=1:
            return True
        else:
            return False
    
   
    def getPassword(self):
        print(f"Password: {self.password}\tLongitud: {self.longitud} caracteres")
    
class Ejecutable:
    
# Crea un array de Passwords con el tamaño que tu le indiques por teclado.
    def __init__(self):
          
        self.lista_longitud=[]
        self.lista_password=[]
        self.lista_esFuerte=[]
        
        for i in range(5):
            self.lista_longitud.append(int(input(f"Introduce la longitud del password {i+1}: ")))# Indica también por teclado la longitud de los Passwords (antes de bucle).
        
        for longitud in self.lista_longitud: 
            self.lista_password.append(Password(longitud))  # Crea un bucle que cree un objeto para cada posición del array. 
            self.lista_esFuerte.append(Password(longitud).esFuerte()) # Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
        
        indice=0
        for pass_esFuerte in self.lista_esFuerte:
            print(f"Contraseña {indice+1} {self.lista_password[indice].password} es Fuerte: {pass_esFuerte}")
            indice+=1
# Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
# contraseña1 valor_booleano1
# contraseña2 valor_bololeano2
#######################################################################

Ejecutable()


