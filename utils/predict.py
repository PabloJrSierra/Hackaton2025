import os
import joblib
import numpy as np
import pandas as pd
import sys

# Ruta al directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar modelo y scaler
modelo = joblib.load(os.path.join(current_dir, "modelo_kmeans.pkl"))
scaler = joblib.load(os.path.join(current_dir, "escalador.pkl"))  # asegúrate de tenerlo guardado igual

# Nombres de columnas usados al entrenar
columnas = [
    "frescos", "rapida", "saludable", "vegano", "dulce",
    "promo", "innovador", "tradicional", "precio", "ambiental"
]

# Recibir datos desde Node o terminal
input_data = list(map(float, sys.argv[1:]))

# Crear DataFrame con nombres correctos
entrada_df = pd.DataFrame([input_data], columns=columnas)

# Escalar datos
entrada_escalada = scaler.transform(entrada_df)

# Predecir
pred = modelo.predict(entrada_escalada)

# Mostrar resultado
print(pred[0])
