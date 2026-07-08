"""
Página de Información.

Explica qué señales usa el sistema y qué características calcula.
Contenido estático (informativo).
"""

import streamlit as st

st.set_page_config(page_title="Información · ECG", page_icon="📖", layout="centered")

st.title("📖 Información")

st.markdown("### Derivaciones utilizadas")
st.markdown(
    """
    El sistema analiza únicamente las tres **derivaciones frontales** del
    triángulo de Einthoven:

    - **Derivación I:** entre brazo izquierdo y brazo derecho.
    - **Derivación II:** entre pierna izquierda y brazo derecho (la mejor para el ritmo).
    - **Derivación III:** entre pierna izquierda y brazo izquierdo.

    Se descartan las derivaciones precordiales (V1–V6) para mantener el modelo
    ligero y aplicable a dispositivos de bajo consumo.
    """
)

st.divider()

st.markdown("### Características que calcula el sistema")
st.markdown(
    """
    A partir de la señal se extraen 8 características numéricas:

    - **Frecuencia cardíaca:** latidos por minuto, a partir de los intervalos R-R.
    - **RMS (I, II, III):** energía eficaz de la señal en cada derivación.
    - **Varianza (I, II, III):** dispersión de las oscilaciones de voltaje.
    - **Ancho del QRS:** duración del complejo QRS en milisegundos.
    """
)

st.divider()

st.markdown("### Limitaciones")
st.markdown(
    """
    - Agrupa toda anomalía bajo el término general **Patológico**, sin
      especificar el tipo (infarto, arritmia, bloqueo, etc.).
    - Al excluir las derivaciones precordiales, pierde sensibilidad ante
      ciertas isquemias.
    - Requiere que la señal cruda tenga una calidad mínima.
    """
)

st.caption("⚠️ Herramienta de apoyo. No reemplaza el diagnóstico profesional.")