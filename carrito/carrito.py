# Crear una sistema de un carrito, que te permita agregar elementos al carrito y eliminarlos. 
# Cuando el usuario decida finalizar con la compra, imprimir por pantalla la cantidad de elementos del carrito, el valor de cada elemento y 
# el monto total a pagar por el usuario

class FabricaElemento:
    @staticmethod
    def crear_elemento(producto, valor):
        PRODUCTOS_POSIBLES = ['Compu', 'Radio', 'Tele', 'Telefono']
        if not producto in PRODUCTOS_POSIBLES:
            raise TypeError("Me mandaste cualquier cosa")
        return Elemento(producto, valor)


class Elemento():
    def __init__(self, nombre: str, valor: int):
        self.nombre = nombre 
        self.__valor = valor if self.__validate_valor(valor) else None

    @property
    def valor(self):
        return self.__valor

    def __validate_valor(self, valor) -> bool:
        if not isinstance(valor, int):
            raise TypeError("Me enviaste un tipo incorrecto boludo")
        if valor <= 0:
            raise ValueError("No loco, no regalo nada")
        return True
    

class Carrito():
    def __init__(self):
        self.carrito: list[Elemento] = []

    def agregar(self, elemento: Elemento):
        self.__validar_elemento(elemento)
        self.carrito.append(elemento)

    def sacar(self, elemento: Elemento):
        if len(self.carrito) <= 0:
            raise Exception("Che no tengo nada loco")
        self.carrito.remove(elemento)

    def finalizar(self):
        monto_total = 0
        for i in self.carrito:
            print(f'Elemento: {i.nombre}, Monto: {i.valor}')
            monto_total += i.valor
        print(monto_total)

    def __validar_elemento(self, elemento: Elemento) -> bool:
        if not isinstance(elemento, Elemento):
            raise TypeError("Me enviaste un tipo incorrecto boludo")
        return True


el1 = FabricaElemento.crear_elemento("Compu", 900000)
el2 = FabricaElemento.crear_elemento("Radio", 150000)
el3 = FabricaElemento.crear_elemento("Tele", 4000000)
el4 = FabricaElemento.crear_elemento("Telefono", 1200000)

lista_elementos = [el1, el2, el3, el4]

carrito = Carrito()

for elemento in lista_elementos:
    carrito.agregar(elemento)

carrito.finalizar()
