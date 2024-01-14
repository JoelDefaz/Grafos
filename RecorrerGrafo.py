from queue import Queue

class RecorrerGrafo:
    CLAVE = 90              # Atributo que representa si un vertice ya fue visitado/revisado

    # Metodo para recorrer el grafo en anchura, empezando desde el vertice que se indica en el parametro
    def recorrer_anchura(self, grafo, nombre_vertice):
        m = [90] * grafo.numero_de_vertices                                     # Arreglo para indicar que ya se visito el vertice
        vertice_inicial = grafo.get_numero_del_vertice(nombre_vertice)          # Vertice donde inicia el recorrido
        if vertice_inicial > 0:
            cola = Queue()                  # Se crea una EDA tipo Cola para el recorrido
            m[vertice_inicial] = 0          # Se indica en la posicon del vertice el valor de 0 (0 -> Visitado/revisado)
            cola.put(vertice_inicial)       # Se ingresa en la cola el vertice inicial
            while not (cola.empty()):       # Mientras la cola no este vacia
                pass
                w = cola.get()                                                      # Obtiene el 1er dato de la cola
                print(f"Vértice {grafo.vertices[w].nombre} => visitado")            # Indica que se a visitado el vertice
                for u in range(0, grafo.numero_de_vertices):
                    #Si el vertice atual tiene un vertice adyacente y no a sido visitado entonces:
                    if grafo.matriz_adyacencia[w][u] == 1 and m[u] == self.CLAVE:
                        m[u] = m[w] + 1                                             # Cambia el estado del vertice a visitado
                        cola.put(u)                                                 # Ingresa el numero del vertice siguiente en la cola
        return m
    