from abc import ABC, abstractmethod


#1.- Crear una clase abstracta y generar, al menos tres clases, que implementen la clase abstracta (que hereden de ella). 
# Guardar las instancias de las clases en una lista, iterar sobre la lista e imprimir el resultado de los metodos comunes.

def ejercicio1():

    # from abc import ABC, abstractmethod --Esto podes importarlo en la cabecera del archivo y te evitas recuperarlo por cada f(x)

    class MetodoEstudio(ABC):
        @abstractmethod
        def aprendiendo(self):
            pass  


    class Lectura(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con lectura de libros"

    class Practica(MetodoEstudio):
     def aprendiendo(self):
        return "Aprendiendo con practicas de laboratorio"

    class Videos(MetodoEstudio):
        def aprendiendo(self):
         return "Aprendiendo con videos de youtube"

    metodos = [
        Lectura(),
        Practica(),
        Videos()
    ]

    for metodo in metodos:
     print(metodo.aprendiendo())

## Muy bien, esta era la idea. Otra forma de hacerlo seria de esta manera:
# lectura = Lectura()
# practica = Practica()
# videos = Videos()
#
# metodos = [lectura, practica, videos]
#
#  for metodo in metodos:
#   print(metodo.aprendiendo())
# 
# La diferencia es que aqui no creas una instancia diferente cada vez que llamas al indice de la lista, sino que agregas a la lista una instancia ya creada.     

# ejercicio1()

# 2.- Crear una clase abstracta y generar, al menos tres clases, que implementen a la clase abstracta. Generar una funcion que, 
# a partir de un parámetro, construya las instancias de las clases, dependiendo del valor del parámetro recibido. 

def ejercicio2():
   
    # from abc import ABC, abstractmethod --Esto podes importarlo en la cabecera del archivo y te evitas recuperarlo por cada f(x)

    class MetodoEstudio(ABC):
        @abstractmethod
        def aprendiendo(self):
            pass  

    class Lectura(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con lectura de libros"

    class Practica(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con prácticas de laboratorio"

    class Videos(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con videos"

   
    def crear_metodo_estudio(tipo):
        clases = {
            "lectura": Lectura,
            "practica": Practica,
            "videos": Videos
        }
        
        if tipo in clases:
            return clases[tipo]()  
        else:
            raise ValueError("Tipo de estudio no válido") ## Buen throw de excepcion para cortar el programa si tipo no esta en el dict.

    metodo1 = crear_metodo_estudio("lectura")
    metodo2 = crear_metodo_estudio("practica")
    metodo3 = crear_metodo_estudio("videos")


    print(metodo1.aprendiendo())  
    print(metodo2.aprendiendo())  
    print(metodo3.aprendiendo())  

# ejercicio2()
## Excelente, nada que decir. Muy buen uso del diccionario y del hecho de que clases[tipo] te devuelve el namespace de una clave para instanciarla, seguido con
## los parentesis para hacer el llamado a la clase. 
    
#3.- Crear una clase abstracta y generar, al menos tres clases, que implementen a la clase abstracta. 
# Guardar las clases en un diccionario, con una clave representativa. 
# Generar una f(x) que reciba una clave y que con ella, busque en el diccionario a la clase asociada a clave y utilice sus metodos.

def ejercicio3():

    # from abc import ABC, abstractmethod --Esto podes importarlo en la cabecera del archivo y te evitas recuperarlo por cada f(x)

    class MetodoEstudio(ABC):
        @abstractmethod
        def aprendiendo(self):
            pass  


    class Lectura(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con lectura de libros"

    class Practica(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con ejercicios prácticos"

    class Videos(MetodoEstudio):
        def aprendiendo(self):
            return "Aprendiendo con videos"

 
    metodos_estudio = {
        "lectura": Lectura,
        "practica": Practica,
        "videos": Videos
    }

  
    def aprender_con_metodo(tipo):
        if tipo in metodos_estudio:
            instancia = metodos_estudio[tipo]()  
            print(instancia.aprendiendo())  
        else:
            print("Método de estudio no válido")


    aprender_con_metodo("lectura")   
    aprender_con_metodo("practica") 
    aprender_con_metodo("videos")   
    aprender_con_metodo("audio")    

ejercicio3()

## Como el anterior, nada que decir. Completado el ejercicio aplicando todos los conocimientos aprendidos.
## Buen detalle al final mostrando que controlas la situacion en la que no tengas una clave en el dict.

10 / 10 