# ==========================================
# INSUMO PRÁCTICO: RAMAS DE LA IA
# Entorno recomendado: Google Colab
# ==========================================

# Instalación de librerías necesarias (Ejecutar en una celda de Colab)
# !pip install textblob scikit-learn scikit-image matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- INICIANDO LABORATORIO DE IA ---")

# 1. APRENDIZAJE AUTOMÁTICO (Machine Learning - Árboles de Decisión)
print("\n[1] Rama: Aprendizaje Automático (Clasificación)")
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Cargar dataset de flores Iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Entrenar modelo
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
precision = clf.score(X_test, y_test)
print(f"Modelo entrenado con una precisión de: {precision * 100:.2f}%")
print(f"Predicción para una nueva flor con medidas [5.1, 3.5, 1.4, 0.2]: Clase {clf.predict([[5.1, 3.5, 1.4, 0.2]])[0]}")


# 2. PROCESAMIENTO DE LENGUAJE NATURAL (NLP)
print("\n[2] Rama: Procesamiento de Lenguaje Natural (Análisis de Sentimiento)")
from textblob import TextBlob

textos = [
    "I absolutely love this new Artificial Intelligence tool, it is amazing!",
    "The system crashed and caused a lot of terrible errors.",
    "The program ran as expected without any changes."
]

for texto in textos:
    analisis = TextBlob(texto)
    # Polaridad: -1.0 (Negativo) a 1.0 (Positivo)
    print(f"Texto: '{texto}' | Polaridad: {analisis.sentiment.polarity:.2f}")


# 3. VISIÓN POR COMPUTADORA (Computer Vision)
print("\n[3] Rama: Visión por Computadora (Detección de Bordes)")
from skimage import data, filters
from skimage.color import rgb2gray

# Cargar imagen de prueba y convertir a escala de grises
image = data.astronaut()
image_gray = rgb2gray(image)

# Aplicar filtro Sobel para detectar bordes
edges = filters.sobel(image_gray)

# Mostrar resultados
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(image)
axes[0].set_title('Imagen Original')
axes[0].axis('off')

axes[1].imshow(edges, cmap='gray')
axes[1].set_title('Detección de Bordes (IA visual)')
axes[1].axis('off')

plt.show()
print("Gráfico de visión por computadora generado con éxito.")
