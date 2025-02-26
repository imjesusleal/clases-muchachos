from abc import abstractmethod, ABC

def IHola(ABC):

    @abstractmethod
    def decir_hola():
        pass

class Hola(IHola):
    def decir_hola():
        print("hola")

class HolaDeNuevo(IHola):
    def decir_hola():
        print("hola de nuevo")

class FabricaHola():

    @staticmethod
    def create_hola(clase: str):
        if clase == 'Hola':
            return Hola()
        if clase == 'HolaDeNuevo':
            return HolaDeNuevo()

hola0 = FabricaHola.create_hola("hola")
print(hola0.decir_hola())

# def decir_hola(clase: IHola):
#     clase.Hola()

# hola1 = Hola()
# decir_hola(hola1)

# holaAgain = HolaDeNuevo()
# decir_hola(holaAgain)

# class ParamsDio:
#     def __init__(self, parm1, parm2, parm3, parm4, parm5, parm6):
#         self.parm1 = parm1
#         self.parm2 = parm2
#         self.parm3 = parm3
#         self.parm4 = parm4
#         self.parm5 = parm5
#         self.parm6 = parm6

# class FabricaDiO:
#     def create_object(params: ParamsDio):
#         return DiO(params.parm1, params.parm2, params.parm3, params.parm4, params.parm5, params.parm6)

# class DiO:
#     def __init__(self, parm1, parm2, parm3, parm4, parm5, parm6):
#         self.parm1 = parm1
#         self.parm2 = parm2
#         self.parm3 = parm3
#         self.parm4 = parm4
#         self.parm5 = parm5
#         self.parm6 = parm6
        

# def create_object(parm1, parm2, parm3, parm4, parm5, parm6):
#     return DiO(parm1, parm2, parm3, parm4, parm5, parm6)

# instancia = create_object(1,2,3,4,5,6)
# instancia2 = FabricaDiO.create_object(6,5,4,3,2,1)

# print(instancia.parm1)
# print(instancia2.parm1)