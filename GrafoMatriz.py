from Grafo import Grafo

class GrafoMatriz(Grafo):
    # Constructor de la clase GrafoMatriz que es especializacion de la Clase Grafo, esta se represetara a traves de matriz de adyacencia
    def __init__(self, maximo):
        super().__init__(maximo)
        self.matriz_adyacencia = [[0] * maximo for _ in range(maximo)]      #Matriz de Adyacencia

    #Metodo que crea un arco entre 2 vertices
    def crear_nuevo_arco(self, a, b):
        va = self.get_numero_del_vertice(a)      #Obtiene el numero del Vertice a
        vb = self.get_numero_del_vertice(b)      #Obtiene el numero del Vertice b
        #Si el número del vertice es menor a cero, quiere decir que no existe el vertice vi donde i -> parametro del metodo
        if not (va < 0 or vb < 0):
            # Cuando existen 2 vertices en el grafo, se indica su arco en la matriz de adyacencia con un 1
            self.matriz_adyacencia[va][vb] = 1

    #Metodo que muestra la representacion del grafo a atraves de la matriz de adyacencia
    def imprimir_grafo(self):
        grafoRepresentacion = ""                                # Variable para mejor impresion
        print("Representacion de la matriz de adyacendia")
        #For anidado que recorre toda la matriz guardanddo sus valores en la variable que se imprimira
        for i in range (0, self.numero_de_vertices):
            for j in range(0, self.numero_de_vertices):
                grafoRepresentacion += f"{self.matriz_adyacencia[i][j]} "
            grafoRepresentacion += "\n"
        print(grafoRepresentacion)