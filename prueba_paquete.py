from paquetes.mipaquete1.mi_modulo import SayHello
from paquetes.mipaquete1.mi_modulo2 import SayBye
import os

di_hola = SayHello()
di_hola.say_hello()

di_chao = SayBye()
di_chao.chao()


os.kill()