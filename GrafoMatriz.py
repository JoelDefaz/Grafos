from Vertice import Vertice

class GrafoMatriz:
    #Constructor de la clase Grafo con sus atributos inicializados
    def __init__(self, maximo):
        self.maximo = maximo                                                #Maximo de vertices del grafo
        self.numero_de_vertices = 0
        self.vertices = [None] * maximo                                     #Arreglo de Vertices
        self.matriz_adyacencia = [[0] * maximo for _ in range(maximo)]      #Matriz de Adyacencia
        # For anidado que llena la matriz de adyacencia con 0
        for i in range(0,maximo):
            for j in range(0,maximo):
                self.matriz_adyacencia[i][j] = 0

    #Metodo que valida si ya existe un vertice
    def get_numero_de_vertice(self, nombre):
        vertice_auxiliar = Vertice(nombre)      #Se ocupa un vertice axiliar
        encontrado = False                      #Condicion de encontrado
        i = 0
        #Recorre todos los vertices para verifciar que aun no exista
        while i < self.numero_de_vertices and not encontrado:
            encontrado = self.vertices[i].es_igual(vertice_auxiliar)
            if not encontrado:
                i=i+1
        # Si encuenra un valor duplicado devolvera el numero de vertice y en caso de que no existe devolvera un -1
        return i if  i < self.numero_de_vertices else -1

    #Metodo que crea nuevos vertices
    def crear_nuevo_vertice(self, nombre):
        # Verifica que no exista el vertice con ese nombre
        existe = self.get_numero_de_vertice(nombre) >= 0
        if not existe:
            nuevo_vertice = Vertice(nombre)                                     #Crea el nuevo vertice
            nuevo_vertice.asignar_numero_de_vertice(self.numero_de_vertices)
            self.vertices[self.numero_de_vertices] = nuevo_vertice              #Agrega el nuevo vertice al arreglo de vertices
            self.numero_de_vertices += 1

    #Metodo que crea un arco entre 2 vertices
    def crear_nuevo_arco(self, a, b):
        va = self.get_numero_de_vertice(a)      #Obtiene el numero del Vertice a
        vb = self.get_numero_de_vertice(b)      #Obtiene el numero del Vertice b
        #Si el numero de vertice es menor a cero quiero decir que no existe el vertice vi donde i -> parametro del metodo
        if not (va < 0 or vb < 0):
            # Cuando si existen 2 vertices en el grafo, se indica su arco en la matriz de adyacencia con un 1
            self.matriz_adyacencia[va][vb] = 1

    #Metodpo que muestra la representacion del grafo a atraves de la matriz de adyacencia
    def imprimir_grafo(self):
        grafoRepresentacion = ""
        print("Representacion de la matriz de adyacendia")
        #For anidado que recorre toda la matriz guardanddo sus valores en la variable que se imprimira
        for i in range (0,self.maximo):
            for j in range(0,self.maximo):
                grafoRepresentacion += f"{self.matriz_adyacencia[i][j]} "
            grafoRepresentacion += "\n"
        print(grafoRepresentacion)