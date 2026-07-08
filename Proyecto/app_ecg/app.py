"""
Página principal (home) de la aplicación de clasificación de señales ECG.

Punto de entrada. Se ejecuta con:
    streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Clasificador ECG",
    page_icon="🫀",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🫀 Clasificador de señales ECG")
st.subheader("Diferenciación entre pacientes sanos y patológicos")

st.markdown(
    """
    Esta herramienta analiza registros de electrocardiograma (ECG) usando las
    **derivaciones frontales I, II y III** y un modelo de *Machine Learning*
    para estimar si la señal corresponde a un paciente **Sano** o **Patológico**.
    """
)

st.divider()

st.markdown("### ¿Cómo usar la aplicación?")
st.markdown(
    """
    1. Ve a la sección **Clasificacion** en el menú de la izquierda.
    2. Sube tu registro de ECG (`.dat`/`.hea` de PhysioNet o `.txt` de BITalino).
    3. Obtén el resultado con su nivel de confianza.

    En **Informacion** encontrarás detalles sobre las señales y sus características,
    y en **Acerca del algoritmo** se explica el modelo y sus limitaciones.
    """
)

# Contenido extra en la barra lateral (se muestra en esta página home).
with st.sidebar:
    st.markdown("### Proyecto")
    st.caption("Clasificación de ECG basada en las derivaciones I, II y III.")

st.divider()
st.caption(
    "⚠️ Esta aplicación es una herramienta de apoyo y no reemplaza el "
    "diagnóstico de un profesional médico."
)