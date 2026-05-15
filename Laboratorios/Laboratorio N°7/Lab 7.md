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
3. [Materiales y equipos](#3-materiales-y-equipos)
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
