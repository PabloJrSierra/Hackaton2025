# utils/predict.py
import sys
import joblib
import numpy as np

modelo = joblib.load("modelo_kmeans.pkl")
# Recibir datos desde Node
input_data = list(map(float, sys.argv[1:]))
input_array = np.array(input_data).reshape(1, -1)

pred = modelo.predict(input_array)
print(pred[0])