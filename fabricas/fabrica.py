from abc import ABC, abstractmethod

class Trabajar:
    pass

class Estudiar:
    pass

class Descansar:
    pass

class FabricaClasica():

    @staticmethod
    def crear_objeto(param):
        TIPOS = ['Estudiar', 'Trabajar', 'Descansar']
        if not param in TIPOS:
            print("No existe el tipo a crear")
        match param.lower():
            case "estudiar":
                return Estudiar()
            case "trabajar":
                return Trabajar()
            case "descansar":
                return Descansar() 

def fabrica_clasica():
    trabajar = FabricaClasica.crear_objeto("Trabajar")
    estudiar = FabricaClasica.crear_objeto("Estudiar")
    descansar = FabricaClasica.crear_objeto("Descansar")

    print(type(trabajar))
    print(type(estudiar))
    print(type(descansar))


class IDeportes:

    @abstractmethod
    def entrenar(self):
        pass


class Futbol(IDeportes):
    def entrenar(self):
        print("Entrenando fulbito")


class Basket(IDeportes):
    def entrenar(self):
        print("Entrenando baskito")

class Tenis(IDeportes):
    def entrenar(self):
        print("Entrenando tenisito")

class FabricaAbstracta:

    @staticmethod
    def crear_objeto(param: str) -> IDeportes:
        match param.lower(): 
            case "futbol":
                return Futbol()
            case "basket":
                return Basket()
            case "tenis":
                return Tenis()

def fabrica_abstracta():
    fut = FabricaAbstracta.crear_objeto("futbol")
    bask = FabricaAbstracta.crear_objeto("basket")
    tenis = FabricaAbstracta.crear_objeto("tenis")
    otro = FabricaAbstracta.crear_objeto("otro")

    print(type(fut))
    print(type(bask))
    print(type(tenis))
    print(type(otro))

# fabrica_abstracta()

class IEntidad(ABC):
    @abstractmethod
    def get_id(self):
        pass

class Persona(IEntidad):

    def __init__(self, id):
        self.__id = id if isinstance(id, int) else None

    def get_id(self):
        return self.__id

class Animal(IEntidad):

    def __init__(self, id):
        self.__id = id if isinstance(id, int) else None

    def get_id(self):
        return self.__id
    
class Insecto(IEntidad):

    def __init__(self, id):
        self.__id = id if isinstance(id, int) else None

    def get_id(self):
        return self.__id
    
class XFabricaAbstracta:
    @staticmethod
    def crear_objeto(bandera: str, id: int) -> IEntidad:
        tipos = {
            "persona": Persona,
            "animal": Animal,
            "insecto": Insecto
        }

        if bandera.lower() in tipos:
            return tipos[bandera](id)
        else:
            None

def crear_x_objeto():
    opciones = ["persona", "animal", "insecto", "otro"]
    contador = 1
    lista: list[IEntidad] = [XFabricaAbstracta.crear_objeto(tipo,id) for id, tipo in enumerate(opciones, start=contador)]

    for i in lista: 
        print(i.get_id() if i != None else None)
    

crear_x_objeto()
