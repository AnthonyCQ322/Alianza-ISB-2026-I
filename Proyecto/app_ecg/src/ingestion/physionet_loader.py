"""
Lectura de registros de PhysioNet en formato .dat / .hea.

Un registro de PhysioNet son al menos DOS archivos con el mismo nombre base:
- un .hea (cabecera de texto con metadatos: canales, frecuencia, etc.)
- uno o más archivos de señal (.dat, y a veces .xyz para las derivaciones
  de Frank vx/vy/vz).

Como solo necesitamos I, II y III (que están en el .dat), leemos ÚNICAMENTE
esos canales. Así wfdb no intenta abrir el .xyz, que el usuario no sube.
"""

import wfdb

from src.config import DERIVACIONES


def cargar_registro_physionet(ruta_base):
    """
    Lee un registro PhysioNet y devuelve solo las derivaciones I, II y III.

    Parámetros
    ----------
    ruta_base : str o Path
        Ruta del registro SIN extensión. Si los archivos son 'paciente.hea'
        y 'paciente.dat', se pasa 'paciente' (sin extensión).

    Retorna
    -------
    senales : dict
        {'I': array, 'II': array, 'III': array}, cada señal en milivoltios.
    fs : int
        Frecuencia de muestreo del registro (Hz).
    """
    ruta_base = str(ruta_base)

    # 1. Leemos SOLO la cabecera para conocer los nombres reales de los canales.
    #    En la base PTB vienen en minúscula ('i', 'ii', 'iii'...).
    cabecera = wfdb.rdheader(ruta_base)
    mapa_nombres = {nombre.upper(): nombre for nombre in cabecera.sig_name}

    # 2. Emparejamos nuestras derivaciones (I, II, III) con el nombre real,
    #    sin importar mayúsculas/minúsculas.
    canales_a_leer = []
    for derivacion in DERIVACIONES:
        if derivacion.upper() not in mapa_nombres:
            raise ValueError(
                f"El registro no contiene la derivación '{derivacion}'. "
                f"Canales encontrados: {cabecera.sig_name}"
            )
        canales_a_leer.append(mapa_nombres[derivacion.upper()])

    # 3. Leemos SOLO esos tres canales. wfdb abrirá únicamente el archivo de
    #    señal que los contiene (el .dat), nunca el .xyz.
    registro = wfdb.rdrecord(ruta_base, channel_names=canales_a_leer)

    # 4. Armamos el diccionario en nuestro orden estándar I, II, III.
    nombres_leidos = [n.upper() for n in registro.sig_name]
    senales = {}
    for derivacion in DERIVACIONES:
        indice = nombres_leidos.index(derivacion.upper())
        senales[derivacion] = registro.p_signal[:, indice]

    return senales, registro.fs