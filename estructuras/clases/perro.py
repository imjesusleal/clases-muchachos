from interfaces.animal import IAnimal

class Perro(IAnimal):
    def hacer_sonido(self):
        return "Guau"