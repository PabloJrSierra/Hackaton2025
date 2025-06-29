import pandas as pd
from sklearn.cluster import KMeans
import joblib
from sqlalchemy import create_engine

# 1. Parámetros de conexión a la base de datos
DB_USER = "usuario"
DB_PASS = "contraseña"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nombre_basedatos"

# 2. Crear engine SQLAlchemy
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# 3. Consulta SQL para extraer 10 datos (ajusta el SELECT a tus columnas numéricas)
consulta = """
SELECT edad, ingreso, gasto, puntaje_crediticio, visitas,
       compras, uso_app, devoluciones, recomendaciones, fidelidad
FROM usuarios
LIMIT 10;
"""

# 4. Cargar datos en DataFrame
df = pd.read_sql_query(consulta, engine)

# 5. Entrenamiento del modelo KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(df)

# 6. Guardar modelo entrenado
joblib.dump(kmeans, "modelo_kmeans.pkl")

print("✅ Modelo entrenado con datos de SQL y guardado correctamente.")
