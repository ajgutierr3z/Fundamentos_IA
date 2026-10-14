# ==========================================
# INSUMO DE PRÁCTICA: MAPA DE CIUDADES Y CÓDIGO BASE
# ==========================================

# Grafo que representa conexiones entre ciudades (mapa no dirigido)
mapa_ciudades = {
    'Aris': ['Bora', 'Cali'],
    'Bora': ['Aris', 'Dora', 'Elio'],
    'Cali': ['Aris', 'Faro'],
    'Dora': ['Bora'],
    'Elio': ['Bora', 'Galo'],
    'Faro': ['Cali', 'Galo'],
    'Galo': ['Elio', 'Faro']
}

def busqueda_a_lo_ancho(grafo, nodo_inicio, nodo_objetivo):
    """
    Implementación de BFS (Breadth-First Search).
    Explora nivel por nivel utilizando una estructura de COLA (Queue).
    """
    visitados = set()
    cola = [[nodo_inicio]]

    if nodo_inicio == nodo_objetivo:
        return "El inicio es el objetivo."

    while cola:
        # TODO: El estudiante debe extraer el primer camino de la cola,
        # obtener el último nodo de ese camino, verificar si es el objetivo,
        # y si no, iterar sobre sus vecinos para agregar nuevos caminos a la cola.
        pass # Reemplazar con la lógica

def busqueda_en_profundidad(grafo, nodo_inicio, nodo_objetivo):
    """
    Implementación de DFS (Depth-First Search).
    Explora a fondo cada rama utilizando una estructura de PILA (Stack).
    """
    visitados = set()
    pila = [[nodo_inicio]]

    if nodo_inicio == nodo_objetivo:
        return "El inicio es el objetivo."

    while pila:
        # TODO: El estudiante debe extraer el ÚLTIMO camino de la pila,
        # obtener el último nodo, verificar si es el objetivo,
        # y si no, iterar sobre sus vecinos para agregar nuevos caminos a la pila.
        pass # Reemplazar con la lógica

# Pruebas a ejecutar una vez completados los algoritmos
# print("Ruta BFS de Aris a Galo:", busqueda_a_lo_ancho(mapa_ciudades, 'Aris', 'Galo'))
# print("Ruta DFS de Aris a Galo:", busqueda_en_profundidad(mapa_ciudades, 'Aris', 'Galo'))
