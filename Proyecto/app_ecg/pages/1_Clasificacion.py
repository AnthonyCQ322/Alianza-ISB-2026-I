"""
Página de Clasificación.

Une todo el pipeline: el usuario sube su registro (PhysioNet o BITalino),
y la app lee, filtra, extrae las 8 características y clasifica la señal.
"""

import os
import tempfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from src.config import DERIVACIONES
from src.ingestion.physionet_loader import cargar_registro_physionet
from src.ingestion.bitalino_loader import cargar_registro_bitalino
from src.processing.filters import filtrar_registro
from src.processing.feature_extraction import extraer_caracteristicas
from src.inference.classifier import clasificar, modelo_disponible

st.set_page_config(page_title="Clasificación · ECG", page_icon="🩺", layout="wide")


# ---------------------------------------------------------------------------
# Funciones auxiliares (privadas de esta página)
# ---------------------------------------------------------------------------
def _preparar_physionet(archivos_subidos):
    """
    Guarda los archivos subidos en una carpeta temporal y devuelve la ruta
    base (sin extensión) que wfdb necesita. Exige al menos el .hea.
    """
    nombres = [a.name for a in archivos_subidos]
    archivo_hea = next((a for a in archivos_subidos if a.name.lower().endswith(".hea")), None)

    if archivo_hea is None:
        return None

    carpeta_temporal = tempfile.mkdtemp()
    for archivo in archivos_subidos:
        ruta = os.path.join(carpeta_temporal, archivo.name)
        with open(ruta, "wb") as destino:
            destino.write(archivo.getbuffer())

    nombre_base = os.path.splitext(archivo_hea.name)[0]
    return os.path.join(carpeta_temporal, nombre_base)

def _graficar_senales(senales, fs, segundos=5):
    """Dibuja los primeros `segundos` de las tres derivaciones."""
    n = int(segundos * fs)
    fig, ejes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)

    for eje, derivacion in zip(ejes, DERIVACIONES):
        senal = senales[derivacion][:n]
        tiempo = np.arange(len(senal)) / fs
        eje.plot(tiempo, senal, color="#1D3557", linewidth=0.8)
        eje.set_ylabel(f"Deriv. {derivacion}\n(mV)")
        eje.grid(True, alpha=0.3)

    ejes[-1].set_xlabel("Tiempo (s)")
    fig.tight_layout()
    return fig


def _mostrar_resultado(resultado):
    """Muestra el veredicto con código de color y las probabilidades."""
    if resultado["clase"] == 0:
        st.success(f"### 🟢 Resultado: {resultado['etiqueta']}")
    else:
        st.error(f"### 🔴 Resultado: {resultado['etiqueta']}")

    columna_izq, columna_der = st.columns(2)
    columna_izq.metric("Probabilidad Sano", f"{resultado['prob_sano'] * 100:.1f}%")
    columna_der.metric(
        "Probabilidad Patológico", f"{resultado['prob_patologico'] * 100:.1f}%"
    )


# ---------------------------------------------------------------------------
# Interfaz
# ---------------------------------------------------------------------------
st.title("🩺 Clasificación")
st.markdown(
    "Sube un registro de ECG para obtener una clasificación **Sano / Patológico**."
)
st.divider()

# --- Sección 1: Carga del registro ---
st.markdown("### 1. Carga del registro")

formato = st.radio(
    "Elige el formato de tu registro:",
    options=["PhysioNet (.dat / .hea)", "BITalino (.txt)"],
    horizontal=True,
)

senales_crudas = None  # se llenará según el formato elegido
fs = None

if formato == "PhysioNet (.dat / .hea)":
    st.caption("Sube **ambos** archivos: el .hea y el .dat (mismo nombre base).")
    archivos = st.file_uploader(
        "Archivos PhysioNet (sube el .hea y su archivo de señal)",
        accept_multiple_files=True,
    )
    if archivos:
        ruta_base = _preparar_physionet(archivos)
        if ruta_base is None:
            st.warning("Faltan archivos: necesito un .hea y un .dat juntos.")
        else:
            senales_crudas, fs = cargar_registro_physionet(ruta_base)

else:  # BITalino
    st.caption("Sube un archivo .txt por cada derivación.")
    col_i, col_ii, col_iii = st.columns(3)
    archivo_i = col_i.file_uploader("Derivación I", type=["txt"], key="der_i")
    archivo_ii = col_ii.file_uploader("Derivación II", type=["txt"], key="der_ii")
    archivo_iii = col_iii.file_uploader("Derivación III", type=["txt"], key="der_iii")

    if archivo_i and archivo_ii and archivo_iii:
        rutas = {"I": archivo_i, "II": archivo_ii, "III": archivo_iii}
        senales_crudas, fs = cargar_registro_bitalino(rutas)


# --- Botón de análisis ---
st.divider()
analizar = st.button(
    "🔬 Analizar señal", type="primary", disabled=senales_crudas is None
)

if senales_crudas is None:
    st.info("Sube tu registro para habilitar el análisis.")

# Al presionar el botón ejecutamos el pipeline UNA vez y guardamos el
# resultado en session_state, la "memoria" que sobrevive a los re-runs.
if analizar and senales_crudas is not None:
    try:
        with st.spinner("Filtrando la señal y extrayendo características..."):
            senales_limpias = filtrar_registro(senales_crudas, fs)
            caracteristicas = extraer_caracteristicas(senales_limpias, fs)

        st.session_state["resultado_analisis"] = {
            "senales_limpias": senales_limpias,
            "caracteristicas": caracteristicas,
            "fs": fs,
        }
    except Exception as error:
        # Si algo falla, borramos cualquier resultado viejo y avisamos.
        st.session_state.pop("resultado_analisis", None)
        st.error(f"Ocurrió un problema al procesar la señal: {error}")

# Dibujamos el resultado GUARDADO (si existe), fuera del if del botón.
# Así permanece visible aunque la página se vuelva a ejecutar.
if "resultado_analisis" in st.session_state:
    datos = st.session_state["resultado_analisis"]

    # --- Sección 2: Vista previa ---
    st.markdown("### 2. Vista previa de la señal (filtrada)")
    st.pyplot(_graficar_senales(datos["senales_limpias"], datos["fs"]))

    with st.expander("Ver las 8 características extraídas"):
        tabla = pd.DataFrame(
            datos["caracteristicas"].items(), columns=["Característica", "Valor"]
        )
        st.dataframe(tabla, hide_index=True, use_container_width=True)

    # --- Sección 3: Resultado ---
    st.markdown("### 3. Resultado del análisis")
    if modelo_disponible():
        resultado = clasificar(datos["caracteristicas"])
        _mostrar_resultado(resultado)
    else:
        st.warning(
            "🔧 El modelo aún no está cargado. Coloca `model.joblib` y "
            "`scaler.joblib` en la carpeta `models/` para habilitar el "
            "veredicto. Mientras tanto, arriba puedes ver la señal filtrada "
            "y las características ya calculadas."
        )

        
st.divider()
st.caption(
    "⚠️ Herramienta de apoyo. No reemplaza el diagnóstico de un profesional médico."
)