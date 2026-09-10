
import itertools

def imprimir_tabla_verdad(funcion_logica, nombre_operacion):
    """
    Evalúa e imprime la tabla de verdad para una función lógica de dos variables (p, q).
    """
    # Valores posibles para p y q (Verdadero y Falso)
    valores = [True, False]
    
    print(f"--- Tabla de Verdad: {nombre_operacion} ---")
    print(f"{'p':<7} | {'q':<7} | {'Resultado':<10}")
    print("-" * 30)
    
    # Genera todas las combinaciones posibles (V-V, V-F, F-V, F-F)
    for p, q in itertools.product(valores, repeat=2):
        # Evalúa la función lógica proporcionada
        resultado = funcion_logica(p, q)
        print(f"{str(p):<7} | {str(q):<7} | {str(resultado):<10}")
    print("\n")

# 1. Definición de Operaciones Lógicas Básicas
def conjuncion(p, q):
    return p and q

def disyuncion(p, q):
    return p or q

def negacion_p(p, q):
    return not p

# Ejecución de prueba
if __name__ == "__main__":
    imprimir_tabla_verdad(conjuncion, "Conjunción (p AND q)")
    imprimir_tabla_verdad(disyuncion, "Disyunción (p OR q)")
    
    # === RETO PARA EL ESTUDIANTE ===
    # El estudiante deberá crear las funciones para:
    # 1. Disyunción Exclusiva (XOR)
    # 2. Implicación Lógica (p -> q)
    # 3. Comprobación de la Primera Ley de De Morgan: not (p and q) == (not p) or (not q)
