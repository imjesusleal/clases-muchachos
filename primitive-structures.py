# sumar = 1 + 2 
# print(dir(int))

# restar = 1 - 2
# print(dir(restar))

# print(dir(float))

# print(dir(str))
# cadena1 = "hola"
# cadena = " mundo"
# print(cadena1 + cadena) 

# var = float(input("Escribe un flotante: "))
# print(type(var))

# milista = [5,3,7,8,11]
# print(milista[2])

# midiccionaro = {"clav1": 5, "clav2": 10}
# print(midiccionaro["clav1"])

# def restar(a,b):
#     return a - b

# midicc = {"clav1": restar(5,10)}
# print(midicc["clav1"])

# print(dir(dict))

# print(midict)
# midict.clear()
# print(midict)

# print("clave3" in midict)
# print(midict.keys())
# print(midict.values())
# print(midict.items())

# var_midict = list(midict.items())
# print(var_midict)
# print(f'tamaño del var_midict: {len(var_midict)}')
# print(var_midict[1][1])

# print(dir(dict))

# midict.pop("clave1")
# print(midict)

# midict = {"clave1": 5, "clav2": 10}
# midict["clave3"] = "Algo muy importante"
# # print(midict)

# # midict.setdefault("clave4", "Esto es algo muy importante pero nuevo")
# midict["clave4"] = "Un valor para no entrar en el if"

# if "clave4" not in midict:
#     midict["clave4"] = "Esto es lo mismo pero con un if"
#     print("Entre por aqui")


# print(midict)

# inputValue = input("Escribe un numero:\n")
# if isinstance(inputValue,str):
#     exit(-1)



# inputValue = int(inputValue)
# print(type(inputValue))
# print(inputValue)


# estudiantes = ["Jesus", "Mary"]
# tupla = (1,2)
# for i in estudiantes:
#     print(i)


# i = 0
# while(i < 5):
#     print("Aqui entre por i es menor que 5")
#     i = i + 1  

# productos = ["Higiene", "Tecnologia", "Deporte", "Hogar"]
# print(len(productos))

# for mivar in range(len(productos)-1, -1, -1):
#     print(productos[mivar])

# i = len(productos) -1
# x = 0
# while(i >= x):
#     print(productos[i])
#     i = i - 1

# Realizar un programa de un carrito. El programa debe consistir en: solicitarle al usuario que usuario que ingrese 
# productos de categorias especificas (las categorias las pueden definir ustedes). 
# El programa debe darle la oportunidad al usuario de seguir agregando productos 
# hasta que el no desee agregar ninguno otro. Cuando el usuario no desee ingresar mas productos, 
# debes devolverle la cantidad de productos que se lleva por cafa categoria y el total de productos que se lleva.


# valor = input("Escribe la vocal A:\n")
# print(valor == "A")

# def sumar(x):
#     if not isinstance(numero_a_sumar, (int,float)):
#         raise TypeError("Chao pescao")
#     return x + 1

# def sumarSinReturn(x):
#     if not isinstance(numero_a_sumar, (int,float)):
#         raise TypeError("Chao pescao")
#     print(x + 1)

# def restar(a,b):
#     return a - b

# numero_a_sumar = 5
# resultado = sumar(numero_a_sumar)
# resultado2 = sumarSinReturn(numero_a_sumar)
# print(resultado)
# print(resultado2)

# resultado3 = restar(5,3)
# print(f'resultado3: {resultado3}')

# un_dict = {"clave1": "hola", "clave2": "chao"}


def agregarClave(diccionario):
    print(diccionario)

def agregarClaveDeNuevo(pepe):
    agregarClave(pepe)

def contabilizar():
    pass

pepe = "hgola"

def main():
    # un_dict = {"clave1": "hola", "clave2": "chao"}
    # agregarClaveDeNuevo(un_dict)
    main()
    
if __name__ == '__main__':
    main()