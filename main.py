from GrafoLista import GrafoLista
from GrafoMatriz import GrafoMatriz

if __name__ == '__main__':
    """
    grafoConMatriz = GrafoMatriz(7)
    grafoConMatriz.crear_nuevo_vertice("A")
    grafoConMatriz.crear_nuevo_vertice("B")
    grafoConMatriz.crear_nuevo_vertice("C")
    grafoConMatriz.crear_nuevo_vertice("D")
    grafoConMatriz.crear_nuevo_vertice("T")
    grafoConMatriz.crear_nuevo_vertice("H")
    grafoConMatriz.crear_nuevo_vertice("R")

    grafoConMatriz.crear_nuevo_arco("D", "B")
    grafoConMatriz.crear_nuevo_arco("D", "C")
    grafoConMatriz.crear_nuevo_arco("B", "H")
    grafoConMatriz.crear_nuevo_arco("R", "H")
    grafoConMatriz.crear_nuevo_arco("H", "D")
    grafoConMatriz.crear_nuevo_arco("H", "T")
    grafoConMatriz.crear_nuevo_arco("H", "A")
    grafoConMatriz.crear_nuevo_arco("C", "R")

    grafoConMatriz.imprimir_grafo()
    """
    grafoConListas = GrafoLista(7)
    grafoConListas.crear_nuevo_vertice("A")
    grafoConListas.crear_nuevo_vertice("B")
    grafoConListas.crear_nuevo_vertice("C")
    grafoConListas.crear_nuevo_vertice("D")
    grafoConListas.crear_nuevo_vertice("T")
    grafoConListas.crear_nuevo_vertice("H")
    grafoConListas.crear_nuevo_vertice("R")

    grafoConListas.crear_nuevo_arco("D", "B")
    grafoConListas.crear_nuevo_arco("D", "C")
    grafoConListas.crear_nuevo_arco("B", "H")
    grafoConListas.crear_nuevo_arco("R", "H")
    grafoConListas.crear_nuevo_arco("H", "D")
    grafoConListas.crear_nuevo_arco("H", "T")
    grafoConListas.crear_nuevo_arco("H", "A")
    grafoConListas.crear_nuevo_arco("C", "R")

    grafoConListas.imprimir_grafo()