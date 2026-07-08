"""
Configuración central del proyecto.

Un único lugar para todas las constantes, rutas y parámetros. Si algún día
cambia la frecuencia de muestreo, la ruta del modelo o el orden de las
características, se edita AQUÍ y en ningún otro sitio.
"""

from pathlib import Path

# --- Rutas del proyecto ---
# Path(__file__) es la ubicación de ESTE archivo (src/config.py).
# .parent.parent sube dos niveles hasta la raíz del proyecto (ecg-classifier/).
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
DIR_MODELOS = RAIZ_PROYECTO / "models"
DIR_MUESTRAS = RAIZ_PROYECTO / "data" / "samples"

RUTA_MODELO = DIR_MODELOS / "model.joblib"
RUTA_SCALER = DIR_MODELOS / "scaler.joblib"

# --- Parámetros de la señal ---
FRECUENCIA_MUESTREO = 1000  # Hz (base PTB y adquisición BITalino)
DERIVACIONES = ["I", "II", "III"]  # derivaciones frontales que usamos

# --- Calibración del hardware BITalino (bits crudos -> milivoltios) ---
BITALINO_VCC = 3.3            # voltaje de alimentación
BITALINO_GANANCIA = 1100.0    # ganancia del sensor de ECG
BITALINO_RESOLUCION = 1023.0  # resolución del ADC (10 bits -> 0..1023)

# --- Parámetros de los filtros (deben coincidir con el entrenamiento) ---
NOTCH_FREQ = 50.0     # Hz, interferencia de red eléctrica (Europa)
NOTCH_Q = 30.0        # factor de calidad del filtro notch
BANDPASS_LOW = 0.5    # Hz, corte inferior (elimina deriva de línea base)
BANDPASS_HIGH = 40.0  # Hz, corte superior (elimina ruido de alta frecuencia)
BANDPASS_ORDEN = 4    # orden del filtro Butterworth

# --- Orden EXACTO de las características que espera el modelo ---
# ¡Este orden NO se puede cambiar! El StandardScaler y el Random Forest
# fueron entrenados con las columnas en esta secuencia exacta.
ORDEN_CARACTERISTICAS = [
    "Frec_Cardiaca",
    "RMS_I", "RMS_II", "RMS_III",
    "Var_I", "Var_II", "Var_III",
    "Ancho_QRS_ms",
]

# --- Valores de seguridad si la extracción falla ---
QRS_FALLBACK_MS = 95.0   # ancho QRS típico si no se puede delinear
HR_FALLBACK_BPM = 75.0   # frecuencia cardíaca típica si no hay picos

# --- Etiquetas de las clases ---
ETIQUETAS = {0: "Sano", 1: "Patológico"}