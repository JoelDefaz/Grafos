class Vertice:
    #Constructor de la clase Vertice con sus atributos inicializados
    def __init__(self, nombre):
        self.nombre = nombre            #Nombre del Vertice
        self.numero_vertice = -1

    def get_nombre_vertice(self):
        #Metodo que retorna el nombre del vertice
        return self.nombre

    def es_igual(self, vertice):
        # Método que compara los nombres del vertice actual con el nombre del vertice de parametro
        return self.nombre == vertice.nombre

    def asignar_numero_de_vertice(self, n):
        #Asigna el numero de vertices que tendra este vertice
        self.numero_vertice = n

    def __str__(self):
        #Descripcion de la clase Vertice con sus repsectivos atributos
        return f"Nombre: {self.nombre}\n" \
               f"Numero de Vertices: {self.numero_vertice}\n"