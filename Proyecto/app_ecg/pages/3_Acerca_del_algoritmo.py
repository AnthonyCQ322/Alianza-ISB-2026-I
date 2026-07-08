"""
Página Acerca del algoritmo.

Explica el modelo de Machine Learning empleado y cómo fue entrenado.
Contenido estático (informativo).
"""

import streamlit as st

st.set_page_config(
    page_title="Acerca del algoritmo · ECG", page_icon="🧠", layout="centered"
)

st.title("🧠 Acerca del algoritmo")

st.markdown("### Modelo utilizado")
st.markdown(
    """
    El clasificador es un **Random Forest** (bosque aleatorio): combina muchos
    árboles de decisión y vota la clase más probable. Se eligió porque logró el
    mejor equilibrio para distinguir pacientes sanos de patológicos.
    """
)

st.divider()

st.markdown("### Datos de entrenamiento")
st.markdown(
    """
    Se entrenó con la **PTB Diagnostic ECG Database** de PhysioNet, usando solo
    las derivaciones I, II y III. Para corregir el desbalance entre clases se
    aplicó la técnica **SMOTE**, que genera ejemplos sintéticos de la clase
    minoritaria durante el entrenamiento.
    """
)

st.divider()

st.markdown("### Limitaciones del modelo")
st.markdown(
    """
    Ninguna herramienta automática es infalible. El resultado debe tomarse como
    una **orientación preliminar**, no como un diagnóstico definitivo.
    """
)

st.caption("⚠️ Herramienta de apoyo. No reemplaza el diagnóstico profesional.")