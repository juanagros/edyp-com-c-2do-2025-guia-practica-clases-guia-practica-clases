# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

#a. Indicá qué devuelven las siguientes expresiones. Analizalo con tus compañeros y luego ejecutá las instrucciones en la máquina para comprobar tu respuesta.
'''
class Camion:
    def __init__(self, patente, marca ,carga,anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2) #true
print(furgon1 is furgon2) #true
print(furgon3 == furgon4) #False
print(furgon3 is furgon4) #False
print(furgon1 == furgon4) #False
'''

#b. Modificá el código dado para que la comparación de dos objetos de la clase Camion devuelva True cuando todos sus atributos sean iguales.
'''
class Camion:
    def __init__(self, patente, marca ,carga,anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self, other):
        if isinstance (other, Camion): #funcion que compara dos objetos
            return (self.patente == other.patente and self.marca == other.marca and self.carga == other.carga and self.anio == other.anio)
    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2) 
print(furgon1 is furgon2)
print(furgon3 == furgon4) 
print(furgon3 is furgon4) 
print(furgon1 == furgon4) 
'''

#c. ¿Qué atributo hace único a nuestros objetos? Identificá el atributo que hace único al objeto Camion y modificá el código para que la comparación de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.

'''
class Camion:
    def __init__(self, patente, marca ,carga,anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self, other):
        if isinstance (other, Camion): #funcion que compara dos objetos
            return (self.patente == other.patente)
    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("ABC123", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2) 
print(furgon1 is furgon2)
print(furgon3 == furgon4) 
print(furgon3 is furgon4) 
print(furgon1 == furgon4) '''

#d. Si dos personas tienen el mismo DNI, entonces... ¡Son la misma persona! ¿Cómo evitarías asignar el mismo DNI a dos personas distintas? Siguiendo esta analogía, adaptá el código anterior para el caso de los camiones.

'''
class Camion:
    patentes_registradas=[]
    def __init__(self, patente, marca ,carga,anio):
        if patente in Camion.patentes_registradas:
            raise ValueError (f'la patente {patente} ya esta registrada, no se puede duplicar')
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio
        Camion.patentes_registradas.append(patente)
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self, other):
        if isinstance (other, Camion): #funcion que compara dos objetos
            return (self.patente == other.patente)
    


furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2) 
print(furgon1 is furgon2)
print(furgon3 == furgon4) 
print(furgon3 is furgon4) 
print(furgon1 == furgon4)
'''
#f. Creá un pequeño menú que te permita:

#1. Registrar un nuevo camión.
#1. Modificar la carga de un camión.
#1. Mostrar por terminal la lista de camiones registrados, del más antiguo al más moderno.
#1. Mostrar por terminal la marca que más veces fue registrada.
    

class Camion:
    patentes_registradas=[]
    camion_lista=[]
    def __init__(self, patente:str, marca:str ,carga:int ,anio:int ):
        if patente in Camion.patentes_registradas:
            raise ValueError (f'la patente {patente} ya esta registrada, no se puede duplicar')
        self.patente = self.validar_cadena(patente)
        self.marca = self.validar_cadena(marca)
        self.carga = self.validar_int(carga)
        self.anio = self.validar_int(anio)
        Camion.patentes_registradas.append(patente)
        Camion.camion_lista.append(self)
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self, other):
        if isinstance (other, Camion): #funcion que compara dos objetos
            return (self.patente == other.patente)      
    def getter_carga(self):
        return self.carga
    def modificar_carga(self,parametro):
        self.carga= parametro
    def validar_cadena(self,cadena:str):
        if not isinstance(cadena,str):
            raise TypeError('El titulo debe ser una cadena de texto')
        if len(cadena)==0:
            raise ValueError('El titulo no puede estar vacio')
        return cadena
    def validar_int(self, numero:int):
        if not isinstance(numero,int):
            raise TypeError ('La carga y/o el anio deben ser numeros')
        if numero<0:
            raise ValueError('el valor debe ser positivo')
        return numero

def agregar_camion():
    try:
        a=input('ingrese la patente: ')
        b=input('ingrese la marca: ')
        c= int(input('ingrese carga: '))
        d=int(input('ingrese el anio: '))
        nuevo =Camion(a,b,c,d)
        print(nuevo)
    except ValueError as e:
        print(f'ocurrio el siguiente error: {e}')
     
def modificar():
    a = input("Ingrese la patente del camión a modificar: ")
    encontrado = False
    for camion in Camion.camion_lista:
        if camion.patente == a:
            nueva_carga = input("Ingrese la nueva carga: ")
            camion.modificar_carga(nueva_carga)
            print(f"La carga del camion con patente {a} ha sido modificada correctamente.")
            encontrado = True
            break
        if not encontrado:
            print(f"No se encontró ningún camión con esa patente.")
   
      
def listado_ordenado():
    for camion in sorted (Camion.camion_lista, key= lambda c: c.anio):
        print(camion)


def marca_mas_registrada():
    marcas=[]
    contador=0 
    marca_mas_repetida=''
    for camion in Camion.camion_lista:
        marcas.append(camion.marca)
    for i in marcas:
        cantidad=marcas.count(i)
        if cantidad>contador:
            marca_mas_repetida=i
    print(f'la marca mas repetida es {marca_mas_repetida}')
                
                            
def menu():
    try:
        opcion= int(input('Que desea hacer?\n1.Registrar un nuevo camion \n2. Modificar la carga de un camion \n3.Ver historial de camiones registrados \n4.Ver marca mas registrada\n5.Salir del menu\n'))    
        if opcion==1:
            agregar_camion()    
            opcion= int(input('Que desea hacer?\n1.Registrar un nuevo camion \n2. Modificar la carga de un camion \n3.Ver historial de camiones registrados \n4.Ver marca mas registrada5.Salir del menu\n'))    
        if opcion==2:
            modificar()
            opcion= int(input('Que desea hacer?\n1.Registrar un nuevo camion \n2. Modificar la carga de un camion \n3.Ver historial de camiones registrados \n4.Ver marca mas registrada5.Salir del menu\n'))    
        if opcion == 3:
            listado_ordenado()
            opcion= int(input('Que desea hacer?\n1.Registrar un nuevo camion \n2. Modificar la carga de un camion \n3.Ver historial de camiones registrados \n4.Ver marca mas registrada5.Salir del menu\n'))    

        if opcion== 4:
            marca_mas_registrada()
            opcion= int(input('Que desea hacer?\n1.Registrar un nuevo camion \n2. Modificar la carga de un camion \n3.Ver historial de camiones registrados \n4.Ver marca mas registrada5.Salir del menu\n'))    
        if opcion == 5:
            return
    except ValueError:
        print('se desea una respuesta numerica')

menu()
#hacer otra clase que sea "manager de camiones" que devuelva la funcion menu y almacene a todos los camciones

furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC124", "Mercedes", 1000, 2020)

