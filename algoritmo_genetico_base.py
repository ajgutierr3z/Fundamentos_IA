# =================================================================
# INSUMO PARA EL ESTUDIANTE: CÓDIGO BASE - ALGORITMO GENÉTICO
#
# =================================================================
import random
import string

# Parámetros del Algoritmo Genético (El estudiante deberá modificarlos)
OBJETIVO = "INTELIGENCIA"
TAMANO_POBLACION = 100
TASA_MUTACION = 0.01
GENERACIONES_MAXIMAS = 1000

def generar_gen_aleatorio():
    """Genera un carácter aleatorio (letras mayúsculas y espacios)."""
    caracteres = string.ascii_uppercase + " "
    return random.choice(caracteres)

def crear_individuo():
    """Crea un individuo (cadena de caracteres) aleatorio."""
    return [generar_gen_aleatorio() for _ in range(len(OBJETIVO))]

def calcular_aptitud(individuo):
    """Calcula cuántos caracteres coinciden exactamente con el objetivo."""
    aptitud = 0
    for i in range(len(OBJETIVO)):
        if individuo[i] == OBJETIVO[i]:
            aptitud += 1
    return aptitud

def seleccion(poblacion):
    """Selecciona un individuo basado en el método de torneo."""
    torneo = random.sample(poblacion, 3)
    torneo.sort(key=calcular_aptitud, reverse=True)
    return torneo[0]

def cruce(padre1, padre2):
    """Realiza el cruce de un punto entre dos padres."""
    punto_cruce = random.randint(1, len(OBJETIVO) - 1)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

def mutacion(individuo):
    """Aplica mutación aleatoria a los genes del individuo."""
    for i in range(len(individuo)):
        if random.random() < TASA_MUTACION:
            individuo[i] = generar_gen_aleatorio()
    return individuo

def ejecutar_algoritmo():
    # Inicialización de la población
    poblacion = [crear_individuo() for _ in range(TAMANO_POBLACION)]
    
    for generacion in range(GENERACIONES_MAXIMAS):
        poblacion.sort(key=calcular_aptitud, reverse=True)
        mejor_individuo = poblacion[0]
        mejor_cadena = "".join(mejor_individuo)
        mejor_aptitud = calcular_aptitud(mejor_individuo)
        
        print(f"Generación {generacion}: {mejor_cadena} (Aptitud: {mejor_aptitud})")
        
        # Condición de éxito
        if mejor_cadena == OBJETIVO:
            print(f"¡Objetivo alcanzado en la generación {generacion}!")
            break
            
        # Crear nueva generación
        nueva_poblacion = [mejor_individuo] # Elitismo
        while len(nueva_poblacion) < TAMANO_POBLACION:
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            hijo = cruce(padre1, padre2)
            hijo_mutado = mutacion(hijo)
            nueva_poblacion.append(hijo_mutado)
            
        poblacion = nueva_poblacion

if __name__ == "__main__":
    ejecutar_algoritmo()
