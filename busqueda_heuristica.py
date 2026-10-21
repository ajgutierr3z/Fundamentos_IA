import heapq

class Nodo:
    def __init__(self, posicion, padre=None):
        self.posicion = posicion
        self.padre = padre
        self.g = 0 # Costo desde el inicio
        self.h = 0 # Heurística (costo estimado hasta la meta)
        self.f = 0 # Costo total (g + h)

    def __lt__(self, otro):
        return self.f < otro.f

# Entorno: 0 = Camino libre, 1 = Pared/Obstáculo
laberinto = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (9, 9)

# TODO: Función heurística a completar por el estudiante
def calcular_heuristica(posicion_actual, posicion_meta):
    # Implementar Distancia Manhattan
    pass

# TODO: Algoritmo A* a completar por el estudiante
def busqueda_a_estrella(matriz, start, end):
    # Inicializar lista abierta y cerrada
    # Implementar ciclo principal de búsqueda
    pass

# Ejecución esperada (comentada hasta que el código esté completo):
# camino = busqueda_a_estrella(laberinto, inicio, meta)
# print("Camino encontrado:", camino)
