import random
import math

# 1. Definir la función a optimizar (Nuestra "montaña")
def funcion_objetivo(x):
    # Función a maximizar: f(x) = x * sin(x)
    return x * math.sin(x)

# 2. Algoritmo de Búsqueda Local (Ascensión de Colinas)
def hill_climbing(limite_inf, limite_sup, paso, iteraciones):
    # El agente inicia en un punto aleatorio dentro del dominio
    nodo_actual = random.uniform(limite_inf, limite_sup)
    
    print(f"Punto de inicio: x = {nodo_actual:.4f}, f(x) = {funcion_objetivo(nodo_actual):.4f}")
    
    for i in range(iteraciones):
        # Generar "vecinos" (dar un paso a la izquierda y otro a la derecha)
        vecino_izq = nodo_actual - paso
        vecino_der = nodo_actual + paso
        
        # Evaluar la altura de la función en la posición actual y en los vecinos
        eval_actual = funcion_objetivo(nodo_actual)
        eval_izq = funcion_objetivo(vecino_izq)
        eval_der = funcion_objetivo(vecino_der)
        
        # Seleccionar el mejor movimiento (el que suba más)
        if eval_der > eval_actual and eval_der >= eval_izq and vecino_der <= limite_sup:
            nodo_actual = vecino_der
        elif eval_izq > eval_actual and eval_izq > eval_der and vecino_izq >= limite_inf:
            nodo_actual = vecino_izq
        else:
            # Si ningún vecino es mejor, se asume que se llegó a la cima (óptimo local o global)
            print(f"Cima alcanzada en la iteración {i}.")
            break
            
    return nodo_actual, funcion_objetivo(nodo_actual)

# 3. Ejecución de la práctica
dominio_busqueda = (0, 10)
tamano_paso = 0.1
max_iteraciones = 100

mejor_x, mejor_y = hill_climbing(dominio_busqueda[0], dominio_busqueda[1], tamano_paso, max_iteraciones)
print(f"\nMejor solución encontrada: x = {mejor_x:.4f}, f(x) = {mejor_y:.4f}")
