"""
Módulo de inferencia.

Carga el modelo Random Forest y el StandardScaler entrenados, ordena las 8
características, las escala y devuelve la predicción (Sano / Patológico) con su
nivel de confianza.

Está diseñado para funcionar aunque los artefactos aún no existan: expone
`modelo_disponible()` para que la interfaz muestre un mensaje amable en lugar
de romperse.
"""

from functools import lru_cache

import joblib
import pandas as pd

from src.config import (
    RUTA_MODELO,
    RUTA_SCALER,
    ORDEN_CARACTERISTICAS,
    ETIQUETAS,
)


def modelo_disponible():
    """Indica si los dos artefactos (modelo y scaler) existen en disco."""
    return RUTA_MODELO.exists() and RUTA_SCALER.exists()


@lru_cache(maxsize=1)
def cargar_artefactos():
    """
    Carga el modelo y el scaler desde disco (una sola vez por proceso).

    lru_cache guarda el resultado tras la primera carga exitosa, así no se
    releen los archivos en cada predicción. Si los archivos no existen, lanza
    un error claro (y al fallar NO se cachea, para poder reintentar cuando
    aparezcan).
    """
    if not modelo_disponible():
        raise FileNotFoundError(
            "No se encontraron 'model.joblib' y/o 'scaler.joblib' en la "
            "carpeta 'models/'. Colócalos ahí para habilitar la clasificación."
        )
    modelo = joblib.load(RUTA_MODELO)
    scaler = joblib.load(RUTA_SCALER)
    return modelo, scaler


def _ordenar_caracteristicas(caracteristicas):
    """
    Convierte el dict de características en un DataFrame de una fila, con las
    columnas en el ORDEN EXACTO que el scaler y el modelo esperan.

    Usar un DataFrame con nombres de columna (en vez de una lista suelta) evita
    advertencias de scikit-learn, porque el scaler fue ajustado con nombres.
    """
    fila = {nombre: caracteristicas[nombre] for nombre in ORDEN_CARACTERISTICAS}
    return pd.DataFrame([fila], columns=ORDEN_CARACTERISTICAS)


def clasificar(caracteristicas):
    """
    Clasifica un registro a partir de sus 8 características.

    Parámetros
    ----------
    caracteristicas : dict
        Las 8 características (salida de extraer_caracteristicas).

    Retorna
    -------
    dict
        {
            'clase': int,              # 0 = Sano, 1 = Patológico
            'etiqueta': str,           # 'Sano' o 'Patológico'
            'prob_sano': float,        # probabilidad de la clase 0 (0..1)
            'prob_patologico': float,  # probabilidad de la clase 1 (0..1)
            'confianza': float,        # probabilidad de la clase predicha
        }
    """
    modelo, scaler = cargar_artefactos()

    X = _ordenar_caracteristicas(caracteristicas)
    X_escalado = scaler.transform(X)

    clase = int(modelo.predict(X_escalado)[0])
    probabilidades = modelo.predict_proba(X_escalado)[0]

    return {
        "clase": clase,
        "etiqueta": ETIQUETAS[clase],
        "prob_sano": float(probabilidades[0]),
        "prob_patologico": float(probabilidades[1]),
        "confianza": float(probabilidades[clase]),
    }