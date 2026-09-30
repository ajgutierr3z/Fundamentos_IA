# =====================================================================
# INSUMO PRÁCTICO: Modelado del Espacio de Búsqueda
# Materia: Fundamentos de Inteligencia Artificial
# =====================================================================

# 1. Definición del Espacio de Búsqueda (Matriz 2D)
# 0 = Camino libre (Transición válida)
# 1 = Obstáculo (Transición inválida)
espacio_laberinto = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

estado_inicial = (0, 0) # Coordenada (Fila, Columna)
estado_meta = (4, 5)    # Objetivo a alcanzar

# 2. Estructura del Nodo para el Árbol de Búsqueda
class NodoBusqueda:
    def __init__(self, estado, padre=None, accion=None, costo_camino=0):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.costo_camino = costo_camino

    def obtener_sucesores(self, laberinto):
        """Genera los nodos hijos a partir del estado actual."""
        sucesores = []
        x, y = self.estado
        
        # Acciones posibles y sus deltas: (Nombre, dx, dy)
        movimientos = [
            ("ARRIBA", -1, 0), 
            ("ABAJO", 1, 0), 
            ("IZQUIERDA", 0, -1), 
            ("DERECHA", 0, 1)
        ]
        
        for accion, dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            # Validar que la nueva posición esté dentro de los límites y no sea obstáculo
            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]):
                if laberinto[nx][ny] == 0:
                    nuevo_estado = (nx, ny)
                    nuevo_nodo = NodoBusqueda(
                        estado=nuevo_estado, 
                        padre=self, 
                        accion=accion, 
                        costo_camino=self.costo_camino + 1
                    )
                    sucesores.append(nuevo_nodo)
        return sucesores

print(f"Inicio configurado en: {estado_inicial}")
print(f"Meta configurada en: {estado_meta}")
print("El entorno está listo para aplicar los algoritmos de búsqueda.")
