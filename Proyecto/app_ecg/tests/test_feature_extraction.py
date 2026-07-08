"""
Pruebas unitarias del módulo de extracción de características.

Verifican dos cosas:
1. Que el cálculo del RMS coincide con un valor calculado a mano.
2. Que `extraer_caracteristicas` devuelve las 8 características esperadas y
   una frecuencia cardíaca coherente, usando un ECG sintético de neurokit2.

Para ejecutarlas, desde la raíz del proyecto:
    pytest
"""

import numpy as np
import neurokit2 as nk

from src.config import ORDEN_CARACTERISTICAS
from src.processing.feature_extraction import (
    _calcular_rms,
    extraer_caracteristicas,
)


def test_rms_valor_conocido():
    """El RMS de [3, 4] debe ser sqrt((9+16)/2) = sqrt(12.5) ≈ 3.5355."""
    senal = np.array([3.0, 4.0])
    resultado = _calcular_rms(senal)
    assert abs(resultado - 3.535533) < 1e-4


def test_extraer_caracteristicas_devuelve_las_8_claves():
    """La salida debe tener exactamente las 8 características de config.py."""
    ecg = nk.ecg_simulate(duration=10, sampling_rate=1000, heart_rate=70)
    senales = {"I": ecg, "II": ecg, "III": ecg}

    caracteristicas = extraer_caracteristicas(senales, fs=1000)

    # Mismas claves, ni más ni menos, que el orden esperado por el modelo.
    assert set(caracteristicas.keys()) == set(ORDEN_CARACTERISTICAS)


def test_frecuencia_cardiaca_coherente():
    """Con un ECG simulado a 70 bpm, la FC detectada debe rondar ese valor."""
    ecg = nk.ecg_simulate(duration=10, sampling_rate=1000, heart_rate=70)
    senales = {"I": ecg, "II": ecg, "III": ecg}

    caracteristicas = extraer_caracteristicas(senales, fs=1000)

    assert 55 < caracteristicas["Frec_Cardiaca"] < 85