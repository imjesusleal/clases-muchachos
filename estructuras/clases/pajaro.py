from interfaces.animal import IAnimal

class Pajaro(IAnimal):
    def hacer_sonido(self):
        return "Pipi"