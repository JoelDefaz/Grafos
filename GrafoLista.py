from Grafo import Grafo

class GrafoLista(Grafo):
    def __init__(self, maximo):
        super().__init__(maximo)

    #Metodo que crea un arco entre 2 vertices
    def crear_nuevo_arco(self, a, b):
        va = self.get_numero_del_vertice(a)         # Obtiene el numero del Vertice a
        vb = self.get_numero_del_vertice(b)         # Obtiene el numero del Vertice b
        # Si el numero de vertice agregar_a_la_lista_de_adyancenciaes menor a cero quiero decir que no
        # existe el vertice vi donde i -> parametro del metodo
        if not (va < 0 or vb < 0):
            # Cuando existen 2 vertices en el grafo, se agrega al vertice a la adyancencia con el vertice b
            self.vertices[va].agregar_a_la_lista_de_adyancencia(self.vertices[vb])

    #Metodo que muestra la representacion del grafo a atraves de la matriz de adyacencia
    def imprimir_grafo(self):
        for vertice in self.vertices:               # Recorre todos los vertices, y en cada uno se obtiene la lista de adyacencia
            print(f"{vertice.numero_vertice} -> {vertice.get_lista_de_adyacencia()}null")