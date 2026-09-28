# Archivo: entorno_busqueda.py
# Descripción: Plantilla para la formalización de un problema de búsqueda espacial.

class ProblemaBusquedaLaberinto:
    def __init__(self):
        # 1. ESTADO INICIAL: (fila, columna)
        self.estado_inicial = (0, 0)
        
        # 2. META: (fila, columna)
        self.meta = (4, 4)
        
        # EL ENTORNO (Espacio de estados): 0 = casilla libre, 1 = obstáculo
        self.mapa = [
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.filas_max = len(self.mapa)
        self.cols_max = len(self.mapa[0])

    def acciones(self, estado):
        """
        Componente 3: ACCIONES LEGALES
        Dado un estado actual (f, c), retorna una lista de acciones posibles 
        (ej. ['ARRIBA', 'ABAJO', 'IZQUIERDA', 'DERECHA']) que no se salgan 
        del mapa ni choquen contra un muro (1).
        """
        acciones_validas = []
        f, c = estado
        
        # TODO: El estudiante debe implementar la lógica de validación de límites y muros aquí
        
        return acciones_validas

    def modelo_transicion(self, estado, accion):
        """
        Componente 4: MODELO DE TRANSICIÓN
        Dado un estado y una acción legal, retorna el nuevo estado resultante (f_nueva, c_nueva).
        """
        f, c = estado
        
        # TODO: El estudiante debe implementar la suma/resta de coordenadas según la acción
        
        return (f, c) # Reemplazar con el estado real

    def prueba_meta(self, estado):
        """
        Componente 5: PRUEBA DE META
        Retorna True si el estado evaluado es igual a la meta, False en caso contrario.
        """
        # TODO: El estudiante debe implementar la condición lógica
        pass

    def costo_ruta(self, estado_actual, accion, estado_siguiente):
        """
        Componente 6 (Opcional pero recomendado): COSTO DE RUTA
        Retorna el costo numérico de ejecutar la acción. 
        En esta cuadrícula, cada movimiento cuesta 1.
        """
        return 1

# --- ZONA DE PRUEBAS ---
# El estudiante debe descomentar estas líneas para verificar su modelo
# entorno = ProblemaBusquedaLaberinto()
# estado_prueba = (0,0)
# print("Estado inicial:", estado_prueba)
# posibles_acciones = entorno.acciones(estado_prueba)
# print("Acciones legales desde el inicio:", posibles_acciones)
