from interfaces.animal import IAnimal

class Gato(IAnimal):
    def hacer_sonido(self):
        return "Miau"