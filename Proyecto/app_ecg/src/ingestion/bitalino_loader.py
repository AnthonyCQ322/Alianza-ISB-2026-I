"""
Lectura de archivos .txt del hardware BITalino.

Cada archivo .txt contiene UNA sola derivación, en valores crudos del ADC
(bits, de 0 a 1023). Se necesita un archivo por derivación (I, II y III), y
hay que calibrar esos bits a milivoltios con la fórmula oficial de BITalino.
"""

import pandas as pd

from src.config import (
    DERIVACIONES,
    FRECUENCIA_MUESTREO,
    BITALINO_VCC,
    BITALINO_GANANCIA,
    BITALINO_RESOLUCION,
)


def _leer_bits_crudos(ruta_archivo):
    """
    Lee un .txt de BITalino y devuelve la columna de la señal en bits.

    El archivo puede traer líneas de comentario (que empiezan con '#') y
    varias columnas separadas por espacios o tabulaciones. La señal de ECG
    es la ÚLTIMA columna con datos.
    """
    # sep=r"\s+" reconoce uno o más espacios/tabulaciones como separador.
    # comment="#" ignora las líneas de encabezado que empiezan con '#'.
    df = pd.read_csv(ruta_archivo, sep=r"\s+", comment="#", header=None)

    # Elimina columnas "fantasma" que quedaron completamente vacías (NaN).
    df = df.dropna(axis=1, how="all")

    # La última columna es la señal; la forzamos a número y los huecos a 0.
    bits = pd.to_numeric(df.iloc[:, -1], errors="coerce").fillna(0).values
    return bits


def _calibrar_a_milivoltios(bits):
    """
    Convierte los bits crudos del ADC (0..1023) a milivoltios reales,
    usando la fórmula oficial de BITalino para el sensor de ECG.
    """
    voltios = ((bits / BITALINO_RESOLUCION) - 0.5) * BITALINO_VCC / BITALINO_GANANCIA
    return voltios * 1000.0  # de voltios a milivoltios


def cargar_registro_bitalino(rutas_por_derivacion):
    """
    Carga las tres derivaciones desde tres archivos .txt de BITalino.

    Parámetros
    ----------
    rutas_por_derivacion : dict
        {'I': ruta_I, 'II': ruta_II, 'III': ruta_III} con la ruta del
        archivo .txt de cada derivación.

    Retorna
    -------
    senales : dict
        {'I': array, 'II': array, 'III': array}, cada señal en milivoltios.
    fs : int
        Frecuencia de muestreo (la del proyecto, 1000 Hz).
    """
    senales = {}
    for derivacion in DERIVACIONES:
        ruta = rutas_por_derivacion[derivacion]
        bits = _leer_bits_crudos(ruta)
        senales[derivacion] = _calibrar_a_milivoltios(bits)

    return senales, FRECUENCIA_MUESTREO