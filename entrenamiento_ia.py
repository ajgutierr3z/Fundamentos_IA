# Importar las librerías necesarias
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Cargar los datos (simulando que se subió el archivo CSV)
# Nota para el estudiante: En Google Colab, asegúrate de subir el archivo frutas_dataset.csv
try:
    datos = pd.pd.read_csv('frutas_dataset.csv')
    print("Datos cargados correctamente.\n", datos)
except:
    print("Error: No se encontró el archivo frutas_dataset.csv")

# 2. Separar características (X) y la etiqueta a predecir (y)
X = datos[['peso', 'textura']] # Features: características físicas
y = datos['etiqueta']          # Labels: lo que queremos predecir (0=Manzana, 1=Naranja)

# 3. Inicializar el modelo de Inteligencia Artificial (Árbol de Decisión)
modelo = DecisionTreeClassifier()

# 4. Entrenar el modelo (Fase de aprendizaje)
modelo.fit(X, y)
print("\n¡El modelo ha sido entrenado con éxito!")

# 5. Hacer una predicción con datos nuevos que la IA nunca ha visto
nuevo_dato = [[142, 1]] # Una fruta que pesa 142g y es lisa (1)
prediccion = modelo.predict(nuevo_dato)

resultado = "Manzana" if prediccion[0] == 0 else "Naranja"
print(f"\nPredicción de la IA para una fruta de 142g y textura lisa: Es una {resultado}.")
