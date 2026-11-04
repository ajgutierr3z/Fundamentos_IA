import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Carga del conjunto de datos
# Asegúrate de haber guardado los datos provistos en un archivo llamado 'clientes_mall.csv'
df = pd.read_csv('clientes_mall.csv')

# 2. Selección de características
# Extraemos solo las columnas numéricas de interés (Ingreso Anual y Puntuación de Gasto)
X = df[['Annual_Income_k', 'Spending_Score']].values

# 3. Cálculo del "Método del Codo" (Elbow Method)
inercia = []
rango_clusters = range(1, 11)

for i in rango_clusters:
    # n_init=10 suprime las advertencias de versiones recientes de scikit-learn
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X)
    inercia.append(kmeans.inertia_)

# Gráfica del Método del Codo
plt.figure(figsize=(10, 5))
plt.plot(rango_clusters, inercia, marker='o', linestyle='--', color='b')
plt.title('Método del Codo para determinar K óptimo')
plt.xlabel('Número de Clústeres (K)')
plt.ylabel('Inercia (Suma de Errores Cuadráticos)')
plt.grid(True)
plt.show()

# 4. Entrenamiento del modelo final
# Al observar la gráfica anterior, supongamos que el "codo" se forma en K=4 
kmeans_final = KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10)
y_kmeans = kmeans_final.fit_predict(X)

# 5. Visualización de resultados
plt.figure(figsize=(10, 6))

# Trazar cada clúster identificado
colores = ['red', 'blue', 'green', 'purple']
for i in range(4):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], 
                s=100, c=colores[i], label=f'Clúster {i+1}')

# Trazar los centroides calculados por el algoritmo
plt.scatter(kmeans_final.cluster_centers_[:, 0], kmeans_final.cluster_centers_[:, 1], 
            s=300, c='yellow', marker='*', edgecolor='black', label='Centroides')

plt.title('Segmentación de Clientes según Ingreso y Gasto')
plt.xlabel('Ingreso Anual (k$)')
plt.ylabel('Puntuación de Gasto (1-100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
