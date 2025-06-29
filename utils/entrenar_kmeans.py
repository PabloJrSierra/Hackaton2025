import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import joblib
from sqlalchemy import create_engine
import sys

# 1. Parámetros de conexión
DB_USER = "postgres"
DB_PASS = "OZPEuAAsQCQchPVODIEqqaFhOKllbpUJ"
DB_HOST = "nozomi.proxy.rlwy.net"
DB_PORT = "45303"
DB_NAME = "railway"

try:
    # 2. Crear conexión SQLAlchemy
    engine = create_engine(f'postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    # 3. Consulta SQL
    consulta = """
    SELECT frescos,
        rapida,
        saludable,
        vegano,
        dulce,
        promo,
        innovador,
        tradicional,
        precio,
        ambiental
    FROM usuarios_respuestas;
    """
    
    # 4. Cargar datos en DataFrame
    df = pd.read_sql_query(consulta, engine)

    if df.empty:
        print("❌ La base de datos no tiene registros.")
        sys.exit(1)

    # 5. Normalización a rango -1 a 1
    scaler = MinMaxScaler(feature_range=(-1, 1))
    datos_normalizados = scaler.fit_transform(df)

    # 6. Entrenamiento del modelo KMeans
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(datos_normalizados)

    # 7. Guardar el modelo y el scaler
    joblib.dump(kmeans, "modelo_kmeans.pkl")
    joblib.dump(scaler, "escalador.pkl")

    print("✅ Modelo entrenado y guardado correctamente.")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)