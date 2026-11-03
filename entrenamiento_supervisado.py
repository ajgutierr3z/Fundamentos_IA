# Importación de bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. Carga de los datos
# Se asume que el archivo CSV está en el mismo directorio
df = pd.read_csv('datos_estudiantes.csv')
print("Primeros registros del dataset:")
print(df.head())

# 2. Separación de características (X) y etiqueta (y)
X = df[['horas_estudio', 'horas_practica']]
y = df['aprobado']

# 3. División del conjunto de datos (Entrenamiento y Prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"\nTamaño del conjunto de entrenamiento: {len(X_train)}")
print(f"Tamaño del conjunto de prueba: {len(X_test)}")

# 4. Inicialización del modelo de aprendizaje supervisado
modelo = LogisticRegression()

# 5. Entrenamiento del modelo
# TODO: El estudiante debe escribir el código para entrenar el modelo usando los datos de entrenamiento
# modelo.fit(..., ...)

# 6. Predicción
# TODO: El estudiante debe escribir el código para predecir las etiquetas del conjunto de prueba
# predicciones = modelo.predict(...)

# 7. Evaluación
# TODO: El estudiante debe calcular la exactitud (accuracy) del modelo
# exactitud = accuracy_score(..., ...)
# print(f"Exactitud del modelo: {exactitud}")
