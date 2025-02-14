from abc import ABC, abstractmethod

class Animal:
    def hacer_sonido(self):
        print("Hago un sonido standard")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")


animal = Animal()
animal.hacer_sonido()

perro = Perro()
perro.hacer_sonido()

gato = Gato()
gato.hacer_sonido()

class Persona:
    nombre: str = ""
    edad = -1
    __salario = 1000000

    @property
    def salario(self):
        return self.__salario

    def decir_hola(self):
        print(f"Hola mi nombre es {self.nombre}")

class Mujer:
    def soy_mujer():
        pass

class Niña(Mujer):
    pass

class Mary(Persona, Niña):
    __salario = 500000000

    @property
    def salario(self):
        return self.__salario
    
    def decir_hola(self):
        print(f"Hola mi nombre es {self.nombre} y yo gano {self.__salario}")

class Sonido(ABC):
    decibeles: int = -1

    @abstractmethod
    def sonido_alto(self):
        pass

    @abstractmethod
    def sonido_bajo(self):
        pass

class SonidoBajo(Sonido):
    decibeles = -100

    def sonido_alto(self):
        print("")

    def sonido_bajo(self):
        print("Suena muy bajo")


sonido1 = SonidoBajo()
print(sonido1.sonido_bajo())
print(sonido1.sonido_alto())

jesus = Persona()
alberto = Persona()

jesus.nombre = "Jesus"
jesus.decir_hola()

alberto.nombre = "Alberto"
alberto.decir_hola()

jesus = Persona()
jesus.decir_hola()
print(jesus.salario)

#Herencia, Encapsulamiento, Abstraccion, Polimorfismo

mary1 = Mary()
mary1.nombre = "Mary"
mary1.decir_hola()
print(mary1.salario)

#MRO
# method resolution order --- 2 nivel
# 1 nivel de herencia

# public
# private
# protected

