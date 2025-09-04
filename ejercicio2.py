# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

class Computadora:
    lista_Computadoras =[]
    id_registradas=[]
    def __init__(self, id:str, modelo:str, marca:str, actualizacion: str, anio:int, storage:int, ram:int):
        if id in Computadora.id_registradas:
            raise ValueError (f'el id {id} ya esta registrado, no se puede duplicar')
        self.id = self.validar_cadena(id)
        self.modelo = self.validar_cadena(modelo)
        self.marca = self.validar_cadena(marca)
        self.actualizacion = self.validar_cadena(actualizacion)
        self.anio = self.validar_int(anio)
        self.storage= self.validar_int(storage)
        self.ram = self.validar_int(ram)
        Computadora.lista_Computadoras.append(self)
    def _str_(self):
        return (f'La computadora con el id {self.id},  marca {self.marca} con la actualizacion {self.actualizacion} es del anio {self.anio}, tiene un storage de {self.storage} GB y un ram de {self.ram}')
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
    def cantidad_compus():
        for i in Computadora.lista_Computadoras:
            cantidad= Computadora.lista_Computadoras.count(i)
        return (f'El numero de computadoras registradas es de {cantidad} ')
    def getter_actualizacion(self):
        return self.actualizacion
    def setter_actaualizacion(self,b): #b seria el parametro que se le pasa
        self.actualizacion= b
        print(f'la computadora {self.id} ha sido actualizada')
    def getter_storage(self):
        return self.storage 
    def setter_storage(self,parametro):
        self.storage= parametro
        print('el storage se ha cambiado')  
    
class RAM():
    def _init_(self, capacidad:int, velocidad:int):
        self.capacidad= self.validar_int(capacidad)
        self.velocidad = self.validar_int(velocidad)
    def validar_int(self, numero:int):
        if not isinstance(numero,int):
            raise TypeError ('La carga y/o el anio deben ser numeros')
        if numero<0:
            raise ValueError('el valor debe ser positivo')
        return numero       
    def _str_(self):
        return(f'el ram de capacidad {self.capacidad} tiene una velocidad de {self.velocidad}')  
    def getter_velocidad(self):
        return self.velocidad
    def setter_velocidad(self,nueva_velocidad):
        self.velocidad= nueva_velocidad
        print(f'se ha modificado la velocidad del {self.capacidad}')
    
    
    
compu1=Computadora('abd','modelo1','apple','ios18',2024, 100, 8)
compu2=Computadora('jkf','modelo2','apple','ios16', 2020, 80, 6)
compu1=Computadora('mno','modelo3','apple','ios16', 2023, 120, 10)



    
