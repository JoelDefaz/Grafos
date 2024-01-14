from abc import ABC, abstractmethod
from Vertice import Vertice


class Grafo(ABC):
    # Constructor de la clase abstracta Grafo con sus atributos inicializados
    def __init__(self, maximo):
        self.numero_de_vertices = 0             # Número de vertices del grafo
        self.vertices = [None] * maximo         # Arreglo de Vertices

    #Método que valida si ya existe un vertice
    def get_numero_del_vertice(self, nombre):
        vertice_auxiliar = Vertice(nombre)      #Se ocupa un vertice axiliar
        encontrado = False                      #Condicion de encontrado
        i = 0
        #Recorre todos los vertices para verifciar que aun no exista
        while i < self.numero_de_vertices and not encontrado:
            encontrado = self.vertices[i].es_igual(vertice_auxiliar)
            if not encontrado:
                i=i+1
        # Si encuenra un valor duplicado devolvera el numero del vertice y en caso de que no existe devolvera un -1
        return i if  i < self.numero_de_vertices else -1

    #Metodo que crea nuevos vertices
    def crear_nuevo_vertice(self, nombre):
        # Verifica que no exista el vertice con ese nombre
        existe = self.get_numero_del_vertice(nombre) >= 0
        if not existe:
            nuevo_vertice = Vertice(nombre)                                     #Crea el nuevo vertice
            nuevo_vertice.asignar_numero_de_vertice(self.numero_de_vertices)
            self.vertices[self.numero_de_vertices] = nuevo_vertice              #Agrega el nuevo vertice al arreglo de vertices
            self.numero_de_vertices += 1

    @abstractmethod
    def crear_nuevo_arco(self,a,b):
        pass

    @abstractmethod
    def imprimir_grafo(self):
        pass