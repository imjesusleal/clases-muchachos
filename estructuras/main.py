from clases.gato import Gato
from clases.perro import Perro
from clases.pajaro import Pajaro
from interfaces.animal import IAnimal

def main():
    perro = Perro()
    gato = Gato()
    pajaro = Pajaro()

    animales_haciendo_sonido(perro)
    animales_haciendo_sonido(gato)
    animales_haciendo_sonido(pajaro)


def animales_haciendo_sonido(animal: IAnimal):
    print(animal.hacer_sonido())

if __name__ == '__main__':
    main()