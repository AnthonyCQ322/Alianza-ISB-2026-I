"""
Extracción de las 8 características que alimentan al modelo.

Recibe las tres derivaciones ya filtradas (en milivoltios) y devuelve un
diccionario con las 8 variables numéricas, calculadas EXACTAMENTE como en el
notebook de entrenamiento (celdas 27 y 34), respetando el orden de config.py.

Características:
    - Frec_Cardiaca            (a partir de los intervalos R-R en la derivación II)
    - RMS_I, RMS_II, RMS_III   (energía eficaz por derivación)
    - Var_I, Var_II, Var_III   (varianza por derivación)
    - Ancho_QRS_ms             (duración media del complejo QRS)
"""

import numpy as np
import neurokit2 as nk

from src.config import (
    FRECUENCIA_MUESTREO,
    QRS_FALLBACK_MS,
    HR_FALLBACK_BPM,
)


def _calcular_rms(senal):
    """Valor cuadrático medio: raíz del promedio de los cuadrados."""
    return np.sqrt(np.mean(senal ** 2))


def _detectar_picos_r(senal_ii, fs):
    """
    Detecta las posiciones de los picos R usando la derivación II.

    Se usa la II porque es donde el pico R es más pronunciado y fácil de
    detectar (por eso el notebook la llama "la derivación metrónomo").
    neurokit2 aplica internamente una versión optimizada del algoritmo
    Pan-Tompkins.
    """
    _, info = nk.ecg_peaks(senal_ii, sampling_rate=int(fs))
    return info["ECG_R_Peaks"]


def _calcular_frecuencia_cardiaca(picos_r, fs):
    """
    Frecuencia cardíaca (latidos por minuto) a partir de los picos R.

    Se mide la distancia entre picos consecutivos (intervalos R-R), se pasa a
    segundos y se convierte a BPM con 60 / promedio(R-R). Si no hay suficientes
    picos, se devuelve un valor de seguridad.
    """
    if len(picos_r) < 2:
        return HR_FALLBACK_BPM

    rr_intervalos = np.diff(picos_r) / fs  # de muestras a segundos
    return 60.0 / np.mean(rr_intervalos)


def _calcular_ancho_qrs(senal_ii, picos_r, fs):
    """
    Ancho medio del complejo QRS en milisegundos.

    Delinea cada latido para encontrar el inicio (R_Onset) y el fin (R_Offset)
    del QRS, mide su duración y promedia. Si la señal es demasiado ruidosa y el
    delineado falla, se devuelve un valor de seguridad.
    """
    try:
        _, ondas = nk.ecg_delineate(
            senal_ii, picos_r, sampling_rate=int(fs), method="dwt"
        )
        inicios = ondas["ECG_R_Onsets"]
        finales = ondas["ECG_R_Offsets"]

        anchos = []
        for inicio, fin in zip(inicios, finales):
            # El delineado puede dejar huecos (NaN) en latidos mal definidos.
            if not np.isnan(inicio) and not np.isnan(fin):
                anchos.append(((fin - inicio) / fs) * 1000.0)  # a milisegundos

        return np.nanmean(anchos) if len(anchos) > 0 else QRS_FALLBACK_MS
    except Exception:
        # Ante cualquier fallo del delineado, no rompemos el pipeline.
        return QRS_FALLBACK_MS


def extraer_caracteristicas(senales, fs=FRECUENCIA_MUESTREO):
    """
    Calcula las 8 características a partir de las derivaciones filtradas.

    Parámetros
    ----------
    senales : dict
        {'I': array, 'II': array, 'III': array}, filtradas y en milivoltios.
    fs : int
        Frecuencia de muestreo en Hz.

    Retorna
    -------
    dict
        Las 8 características con sus nombres (los mismos de config.py).
    """
    senal_ii = senales["II"]

    # Características temporales (dependen de los latidos).
    picos_r = _detectar_picos_r(senal_ii, fs)
    frecuencia = _calcular_frecuencia_cardiaca(picos_r, fs)
    ancho_qrs = _calcular_ancho_qrs(senal_ii, picos_r, fs)

    # Diccionario de salida, con las 8 claves que espera el modelo.
    caracteristicas = {
        "Frec_Cardiaca": frecuencia,
        "RMS_I": _calcular_rms(senales["I"]),
        "RMS_II": _calcular_rms(senales["II"]),
        "RMS_III": _calcular_rms(senales["III"]),
        "Var_I": np.var(senales["I"]),
        "Var_II": np.var(senales["II"]),
        "Var_III": np.var(senales["III"]),
        "Ancho_QRS_ms": ancho_qrs,
    }
    return caracteristicas