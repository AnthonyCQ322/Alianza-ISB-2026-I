"""
Filtrado de la señal ECG.

Replica EXACTAMENTE el acondicionamiento usado durante el entrenamiento
(notebook, celda 8): un filtro Notch a 50 Hz seguido de un Butterworth
pasa-banda (0.5–40 Hz), aplicados con filtrado de fase cero (filtfilt).

Que la limpieza aquí sea idéntica a la del entrenamiento es lo que garantiza
que el modelo reciba datos "con la misma forma" que aprendió.
"""

from scipy.signal import butter, iirnotch, filtfilt

from src.config import (
    DERIVACIONES,
    FRECUENCIA_MUESTREO,
    NOTCH_FREQ,
    NOTCH_Q,
    BANDPASS_LOW,
    BANDPASS_HIGH,
    BANDPASS_ORDEN,
)


def _disenar_filtros(fs):
    """
    Calcula los coeficientes de ambos filtros una sola vez.

    Retorna dos pares de coeficientes (b, a): uno para el Notch y otro para
    el pasa-banda. Separar el "diseño" del "uso" evita recalcularlos por cada
    derivación.
    """
    filtro_notch = iirnotch(NOTCH_FREQ, NOTCH_Q, fs)
    filtro_banda = butter(
        BANDPASS_ORDEN, [BANDPASS_LOW, BANDPASS_HIGH], btype="bandpass", fs=fs
    )
    return filtro_notch, filtro_banda


def _filtrar_canal(canal, filtro_notch, filtro_banda):
    """
    Aplica los dos filtros en cadena a una sola derivación.

    Se usa filtfilt (filtrado hacia adelante y hacia atrás) para no introducir
    desfases: así los picos R quedan en su posición temporal original, algo
    crítico para calcular después la frecuencia cardíaca y el ancho QRS.
    """
    b_notch, a_notch = filtro_notch
    b_banda, a_banda = filtro_banda

    senal_sin_red = filtfilt(b_notch, a_notch, canal)      # quita los 50 Hz
    senal_limpia = filtfilt(b_banda, a_banda, senal_sin_red)  # deja 0.5–40 Hz
    return senal_limpia


def filtrar_registro(senales, fs=FRECUENCIA_MUESTREO):
    """
    Filtra las tres derivaciones de un registro.

    Parámetros
    ----------
    senales : dict
        {'I': array, 'II': array, 'III': array} en milivoltios (crudos).
    fs : int
        Frecuencia de muestreo en Hz.

    Retorna
    -------
    dict
        {'I': array, 'II': array, 'III': array} ya filtrados, misma estructura.
    """
    filtro_notch, filtro_banda = _disenar_filtros(fs)

    senales_limpias = {}
    for derivacion in DERIVACIONES:
        senales_limpias[derivacion] = _filtrar_canal(
            senales[derivacion], filtro_notch, filtro_banda
        )
    return senales_limpias