# Importación de librerías necesarias
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. GENERACIÓN DEL DATASET (Insumo para el estudiante)
# Se crea un dataset binario sintético de 1000 muestras
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# División en datos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Datos generados y divididos con éxito.")
print(f"Tamaño de entrenamiento: {X_train.shape}")
print(f"Tamaño de prueba: {X_test.shape}\n")

# 2. MODELO DE MACHINE LEARNING (Regresión Logística)
print("--- Entrenando Modelo de Machine Learning ---")
ml_model = LogisticRegression()
ml_model.fit(X_train, y_train)

# Predicción y Evaluación
ml_predictions = ml_model.predict(X_test)
ml_accuracy = accuracy_score(y_test, ml_predictions)
print(f"Precisión del modelo de ML: {ml_accuracy * 100:.2f}%\n")

# 3. MODELO DE DEEP LEARNING (Red Neuronal Simple)
print("--- Entrenando Modelo de Deep Learning ---")
# Arquitectura básica: 1 capa oculta con 8 neuronas y 1 capa de salida
dl_model = Sequential([
    Dense(8, activation='relu', input_shape=(10,)),
    Dense(1, activation='sigmoid')
])

# Compilación del modelo
dl_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento (15 épocas, mostrando progreso)
history = dl_model.fit(X_train, y_train, epochs=15, batch_size=32, validation_split=0.1, verbose=1)

# Evaluación
dl_loss, dl_accuracy = dl_model.evaluate(X_test, y_test, verbose=0)
print(f"\nPrecisión del modelo de DL: {dl_accuracy * 100:.2f}%")
