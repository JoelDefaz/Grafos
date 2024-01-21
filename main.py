from RecorrerGrafo import RecorrerGrafo
from GrafoLista import GrafoLista
from GrafoMatriz import GrafoMatriz

if __name__ == '__main__':
    grafo = GrafoMatriz(7)

    grafo.crear_nuevo_vertice("A")
    grafo.crear_nuevo_vertice("B")
    grafo.crear_nuevo_vertice("C")
    grafo.crear_nuevo_vertice("D")
    grafo.crear_nuevo_vertice("T")
    grafo.crear_nuevo_vertice("H")
    grafo.crear_nuevo_vertice("R")

    grafo.crear_nuevo_arco("D", "B")
    grafo.crear_nuevo_arco("D", "C")
    grafo.crear_nuevo_arco("B", "H")
    grafo.crear_nuevo_arco("R", "H")
    grafo.crear_nuevo_arco("H", "D")
    grafo.crear_nuevo_arco("H", "T")
    grafo.crear_nuevo_arco("H", "A")
    grafo.crear_nuevo_arco("C", "R")

    grafo.imprimir_grafo()

    print("Recorrido en Profundidad")
    RecorrerGrafo().recorrer_profundidad(grafo,"D")