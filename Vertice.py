class Vertice:
    # Constructor de la clase Vertice con sus atributos inicializados
    def __init__(self, nombre):
        self.nombre = nombre                #Nombre del Vertice
        self.numero_vertice = -1            #Numero del  vertice
        self.lista_de_adyacencia = list()   #Lista de adyacencia(si aplica)

    # Método que compara los nombres del vertice actual con el nombre del vertice de parametro
    def es_igual(self, vertice):
        return self.nombre == vertice.nombre

    # Asigna el numero de vertices que tendra este vertice
    def asignar_numero_de_vertice(self, n):
        self.numero_vertice = n

    # Método que agrega el vertice a la lista de adyacencia
    def agregar_a_la_lista_de_adyancencia(self, b):
        self.lista_de_adyacencia.append(b)

    # Método que retorna la composicion de la lista de adyacencia
    def get_lista_de_adyacencia(self):
        representacion_lista_adyacencia = ""            # Variable auxiliar
        for vert in self.lista_de_adyacencia:
            representacion_lista_adyacencia += str(vert.numero_vertice) + " -> "
        return representacion_lista_adyacencia

    # To string de la clase Vertice
    def __str__(self):
        #Descripcion de la clase Vertice con sus repsectivos atributos
        return f"Nombre: {self.nombre}\n" \
               f"Numero de Vertices: {self.numero_vertice}\n"