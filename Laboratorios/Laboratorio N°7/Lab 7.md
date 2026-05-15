<div align="center">
  <h1><b>LABORATORIO N°7: Adquisición de señales EEG</b></h1>
  <p><b>Universidad Peruana Cayetano Heredia</b></p>
  <h1><b>BITAlino para EEG</b></h1>
</div>

<div  align="center">
  <h1><b>INTRODUCCIÓN A SEÑALES BIOMÉDICAS</b></h1>
</div>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/bitalino.png" width="70%">
</p>

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Marco Teórico](#2-marco-teórico)
   - 2.1 [Fisiología de la señal EEG](#21-fisiología-de-la-senal-EEG)
   - 2.2 [Frecuencias Cerebrales y Bandas de Frecuencia](#22-frecuencias-cerebrales-y-bandas-de-frecuencia)
   - 2.3 [Fisiología de la señal EEG](#23-fisiología-de-la-señal-EEG)
3. [Materiales y equipos](#3-materiales-y-equipos)
   - 3.1 [Hardware](#31-hardware)
   - 3.2 [Software](#32-software)
4. [Procedimiento](#4-procedimiento)
5. [Resultados](#5-resultados)
6. [Discusión](#6-discusión)
   - 6.1 [Análisis de Resultados](#61-análisis-de-resultados)
   - 6.2 [Limitaciones](#62-limitaciones)
7. [Bibliografía](#8-bibliografía)

## 1. Introducción
<div align="justify">
La electroencefalografía (EEG) es una técnica neurofisiológica no invasiva para registrar la actividad eléctrica del cerebro con electrodos colocados sobre el cuero cabelludo, dando como resultado una representación gráfica del voltaje cerebral en función del tiempo. Esta actividad es la expresión de cambios en el potencial eléctrico, producidos principalmente por la suma de potenciales postsinápticos en las neuronas corticales [1].  

Este estudio de las ondas cerebrales permite a los científicos y profesionales de la salud adentrarse en los misterios de la cognición, las emociones y otros estados mentales, lo que no sólo amplía el conocimiento en neurociencia y psicología, sino que impulsa el desarrollo de métodos de diagnóstico y terapia para trastornos neurológicos y el progreso de las interfaces cerebro-máquina (BCI), contribuyendo así de manera significativa al bienestar humano [2]. 

En esta práctica se emplea el sistema de adquisición BITalino (r)evolution y el software Open Signals para la captura de bioseñales en tiempo real. Se pretende reconocer los ritmos cerebrales principales y entender cómo los factores externos (estímulos visuales) e internos (tareas cognitivas) modulan la señal, de acuerdo con los estándares del Sistema Internacional 10-20.

</div>

## 2. Marco Teórico
### 2.1. Fisiología de la señal EEG
<div align="justify">
El origen fisiológico es debido a la suma espacial y temporal de los potenciales postsinápticos excitatorios (EPSP) e inhibitorios (IPSP), y no a los potenciales de acción, ya que estos son demasiado breves para ser integrados. Se producen sobre todo en las dendritas de las células piramidales de la corteza cerebral, cuya disposición perpendicular y organizada permite que funcionen como dipolos microscópicos; la superposición de estos campos eléctricos produce potenciales que pueden ser detectados sobre el cuero cabelludo y para que esta actividad pueda ser registrada es necesario que se sincronicen grandes grupos neuronales, lo cual depende en gran medida de las conexiones talamocorticales y de las células marca-paso responsables de los ritmos cerebrales [3].
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-1.png" width="70%">
</p>
<p align="center">
Figura 1. Modelo de dipolo de corriente en una célula piramidal de la corteza cerebral [3]
</p>
</div>

### 2.2. Frecuencias Cerebrales y Bandas de Frecuencia
<div align="justify">
El EEG nos permite estudiar la corteza cerebral, que es donde se procesan las funciones superiores del ser humano como el pensamiento y la percepción. Las señales se agrupan en bandas de frecuencia asociadas a estados fisiológicos específicos [1,4]:
</div>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-2.png" width="70%">
</p>
<p align="center">
Figura 2. Bandas de frecuencia [4]
</p>

<div align="justify">
  
- **Gamma (> 25 Hz):** Resolución de problemas y procesamiento cognitivo complejo.
- **Beta (12 –  25 Hz):** Alerta, atención, pensamiento activo.
- **Alpha (8-12 Hz):** Estado de descanso, reflexión y relajación con los ojos cerrados.
- **Theta (4-8 Hz):** Somnolencia, meditación profunda o sueño ligero y ligero.
- **Delta (0 – 4 Hz):** Sueño reparador y físico. 

</div>

### 2.3. Fisiología de la señal EEG
<div align="justify">
La señal EEG es de muy baja amplitud, por lo que es vulnerable a la presencia de artefactos que pueden distorsionar su interpretación [1,2]:
  
- **Actividad Muscular:** Los movimientos de la cara, la masticación o la tensión del cuello producen señales que contaminan el registro.

- **Oculares (EOG):** Los parpadeos y los movimientos de los ojos generan campos eléctricos que son detectados mayormente por los electrodos frontales (Fp1/Fp2).

- **Interferencia eléctrica:** Ruido eléctrico de red (50/60 Hz) que puede ocultar la actividad cerebral si el entorno no está aislado adecuadamente.

- **Fuerzas Mecánicas:** Los electrodos mal adheridos o una preparación deficiente de la piel generan variaciones de impedancia y pérdida de calidad de la señal 

</div>

## 3. Materiales y equipos
### 3.1 Hardware

<div align="justify">
  
- **Placa BITalino (r)evolution Board Kit BLE/BT:** Sistema principal de adquisición de datos fisiológico.
- **Sensor de Electroencefalografía (EEG):** Módulo analógico preensamblado, diseñado específicamente para captar microvoltios de actividad cerebral.
- **Cable de electrodos de 3 vías:** Cable con conectores tipo snap para la medición diferencial (IN+ e IN-) y la referencia (REF).
- **Electrodos de superficie:** 3 Electrodos desechables pre gelificados de Ag/AgCl.
- **Batería Li-Po (3.7V):** Fuente de alimentación aislada de la red eléctrica para garantizar la seguridad del usuario.

</div>

### 3.2 Software

<div align="justify">
  
- **OpenSignals (r)evolution:** Software para la captura, visualización y almacenamiento de la señal EEG en tiempo real.
- **Google Colab:** Software de programación para el procesamiento digital de señales, haciendo uso de librerías como scipy.signal.

</div>

## 4. Procedimiento
<div align="justify">

- **Limpieza y Preparación:** Se procedió a limpiar minuciosamente con alcohol las zonas específicas de la cabeza del sujeto de prueba para eliminar la grasa capilar y células muertas, garantizando una baja impedancia acústica y eléctrica.
- **Colocación de electrodos:** Se ubican los electrodos positivos y negativos en la región frontal (Fp1, Fp2) para evaluar la atención y artefactos oculares. El electrodo de referencia se colocó en una zona ósea neutra (como la apófisis mastoides detrás de la oreja o el lóbulo de la oreja).
<p align="center">
[Figura 1: Colocación de los electrodos en la frente del sujeto (Fp1/Fp) y la referencia]
</p>

- **Conexión y Configuración:** Se encendió el BITalino y se emparejó por Bluetooth a la computadora. En OpenSignals se habilitó el canal EEG y se configuró una frecuencia de muestreo adecuada.
- **Medición de Línea base:** El sujeto cerró los ojos y se relajó en silencio sin moverse por un minuto.
<p align="center">
[Figura 2: Sujeto relajado con los ojos cerrados y con auriculares]
</p>

- **Medición de Ojos abiertos:** El sujeto se mantuvo relajado y en silencio, fijando la mirada en un punto estático durante un tiempo determinado.
<p align="center">
[Figura 3: Sujeto relajado con los ojos cerrados y con auriculares]
</p>

- **Medición de Línea base:** El sujeto cerró los ojos y se relajó en silencio sin moverse por un minuto por segunda vez.
<p align="center">
[Figura 4: Sujeto relajado con los ojos cerrados y con auriculares]
</p>

- **Medición de movimientos faciales:** Se le pidió al sujeto realizar movimientos faciales voluntarios que contaminan intencionalmente la señal como pestañear y simular la acción de masticar.
<p align="center">
[Figura 5: Sujeto con la acción de pestañear y mover la mandíbula]
</p>

- **Medición de Línea base:** El sujeto cerró los ojos y se relajó en silencio sin moverse por un minuto por tercera vez.
<p align="center">
[Figura 6: Sujeto relajado con los ojos cerrados y con auriculares]
</p>

- **Medición de Tarea Cognitiva:** El sujeto con los ojos abiertos escuchó dos tipos de sonidos, uno relajante y uno estresante.
<p align="center">
[Figura 7: Grabación del usuario escuchando sonidos relajantes y estresantes]
</p>

- **Filtrado y Procesamiento:** Se exportan los datos en formato .txt, se importaron a Google Colab usando Python y se aplicó un filtro pasa-banda de 0.8 Hz a 48 Hz para aislar los ritmos cerebrales útiles.

</div>

# 5. Resultados

- **Señal cruda y filtrada:**
  
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-3.png" width="70%">
</p>
<p align="center">
Fig. 1. Señales EEG - Basal 1 de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch)
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 2. Señales EEG - Mirada Fija de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 3. Señales EEG - Basal 2 de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 4. Señales EEG - Parpadeo + Masc. de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 5. Señales EEG - Basal 3 de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 6. Señales EEG - Música Relajante de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 7. Señales EEG - Música Estresante de Fp1 y Fp2 antes y después del filtrado (0.8 - 48 Hz + notch)
</p>

- **PSD Welch**

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 8. Densidad espectral de potencia de las señales EEG - Basal 1 en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 9. Densidad espectral de potencia de las señales EEG - Mirada Fija en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 10. Densidad espectral de potencia de las señales EEG - Basal 2 en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 11. Densidad espectral de potencia de las señales EEG - Parpadeo + Masc. en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 12. Densidad espectral de potencia de las señales EEG - Basal 3 en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 13. Densidad espectral de potencia de las señales EEG - Música Relajante en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 14. Densidad espectral de potencia de las señales EEG - Música Estresante en los canales Fp1 y Fp2 mediante método Welch.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Tabla 1. Potencia relativa por banda (%) - Fp1.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Tabla 2. Potencia relativa por banda (%) - Fp1.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 15. Comparación de potencia alpha entre condiciones a ojos cerrados y ojos abiertos en los canales Fp1 y Fp2.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Tabla 3. Resultados del análisis de potencia alpha.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 16. Comparación de potencia alpha entre condiciones a ojos cerrados y ojos abiertos en los canales Fp1 y Fp2.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Tabla 4. Resultados del análisis de potencia beta.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 17. Comparación de potencia beta entre condiciones Basal y Mirada Fija en los canales Fp1 y Fp2.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Tabla 5. Resultados de detección de parpadeos.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°7/lab7-4.png" width="70%">
</p>
<p align="center">
Fig. 18. Detección de parpadeos en las señales EEG - Parpadeo + Masticando.
</p>

# 6. Discusión
