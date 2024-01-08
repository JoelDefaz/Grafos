from Vertice import Vertice

class GrafoLista:
    def __init__(self, maximo):
        self.maximo = maximo                                                #Maximo de vertices del grafo
        self.numero_de_vertice = 0
        self.vertices = [None] * maximo                                     #Arreglo de Vertices
        self.lista_adyacencia = [None] * maximo                            #Listas de Adyacencia

    def get_numero_de_vertice(self, nombre):
        vertice_auxiliar = Vertice(nombre)      #Se ocupa un vertice axiliar
        encontrado = False                      #Condicion de encontrado
        i = 0
        #Recorre todos los vertices para verifciar que aun no exista
        while i < self.numero_de_vertice and not encontrado:
            encontrado = self.vertices[i].es_igual(vertice_auxiliar)
            if not encontrado:
                i=i+1
        # Si encuenra un valor duplicado devolvera el numero de vertice y en caso de que no existe devolvera un -1
        return i if  i < self.numero_de_vertice else -1

    def crear_nuevo_vertice(self, nombre):
        # Verifica que no exista el vertice con ese nombre
        existe = self.get_numero_de_vertice(nombre) >= 0
        if not existe:
            nuevo_vertice = Vertice(nombre)                                     #Crea el nuevo vertice
            nuevo_vertice.asignar_numero_de_vertice(self.numero_de_vertice)
            self.vertices[self.numero_de_vertice] = nuevo_vertice              #Agrega el nuevo vertice al arreglo de vertices
            self.numero_de_vertice += 1

    #Metodo que crea un arco entre 2 vertices
    def crear_nuevo_arco(self, a, b):
        va = self.get_numero_de_vertice(a)      #Obtiene el numero del Vertice a
        vb = self.get_numero_de_vertice(b)      #Obtiene el numero del Vertice b
        #Si el numero de vertice es menor a cero quiero decir que no existe el vertice vi donde i -> parametro del metodo
        if not (va < 0 or vb < 0):
            # Cuando si existen 2 vertices en el grafo, se indica su arco en la matriz de adyacencia con un 1
            if self.lista_adyacencia[va] == None:
                self.lista_adyacencia[va] = [vb]
            else:
                self.lista_adyacencia[va].append(vb)

    #Metodo que muestra la representacion del grafo a atraves de la matriz de adyacencia
    def imprimir_grafo(self):
        for i in range (0,self.maximo):
            if self.lista_adyacencia[i] == None:
                print(f"{i} -> null ")
            else:
                print(f"{i} -> {self.get_sublista(i)}null")

    def get_sublista(self,i):
        sublista = ""
        for elemento in self.lista_adyacencia[i]:
            sublista += str(elemento) + " -> "
        return sublista