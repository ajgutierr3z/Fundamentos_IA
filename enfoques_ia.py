import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import io

# 1. Cargar los datos (Simulando el archivo CSV)
csv_data = """nombre,tiene_pelo,pone_huevos,sangre_caliente,clase
Perro,1,0,1,Mamifero
Gato,1,0,1,Mamifero
Serpiente,0,1,0,Reptil
Lagarto,0,1,0,Reptil
Murcielago,1,0,1,Mamifero
Tortuga,0,1,0,Reptil
Ornitorrinco,1,1,1,Mamifero
Cocodrilo,0,1,0,Reptil"""

df = pd.read_csv(io.StringIO(csv_data))
print("Datos cargados:\n", df, "\n")

# ==========================================
# ENFOQUE 1: IA Simbólica (Basada en Reglas)
# ==========================================
print("--- Resultados Enfoque 1: Reglas Manuales ---")
def clasificar_por_reglas(tiene_pelo, pone_huevos, sangre_caliente):
    # El programador define la lógica explícitamente
    if tiene_pelo == 1 and sangre_caliente == 1:
        return "Mamifero"
    elif pone_huevos == 1 and sangre_caliente == 0:
        return "Reptil"
    else:
        return "Desconocido"

# Probando el modelo manual con un caso nuevo
nuevo_animal = {"nombre": "Leon", "tiene_pelo": 1, "pone_huevos": 0, "sangre_caliente": 1}
prediccion_reglas = clasificar_por_reglas(nuevo_animal["tiene_pelo"], nuevo_animal["pone_huevos"], nuevo_animal["sangre_caliente"])
print(f"El sistema basado en reglas clasificó al {nuevo_animal['nombre']} como: {prediccion_reglas}\n")

# ==========================================
# ENFOQUE 2: Machine Learning (Basado en Datos)
# ==========================================
print("--- Resultados Enfoque 2: Machine Learning ---")
# Separar características (X) y etiquetas (y)
X = df[['tiene_pelo', 'pone_huevos', 'sangre_caliente']]
y = df['clase']

# Entrenar un Árbol de Decisión (El algoritmo aprende las reglas solo)
modelo_ml = DecisionTreeClassifier()
modelo_ml.fit(X, y)

# Predecir el mismo caso nuevo
X_nuevo = pd.DataFrame([[1, 0, 1]], columns=['tiene_pelo', 'pone_huevos', 'sangre_caliente'])
prediccion_ml = modelo_ml.predict(X_nuevo)
print(f"El modelo de Machine Learning clasificó al {nuevo_animal['nombre']} como: {prediccion_ml[0]}")
