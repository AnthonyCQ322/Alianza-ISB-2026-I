<div align="center">
  <h1><b>LABORATORIO N°8: Aplicación de ICA en Señales EEG</b></h1>
  <p><b>Universidad Peruana Cayetano Heredia</b></p>
  <h1><b>Remoción de Artefactos mediante Análisis de Componentes Independientes</b></h1>
</div>

<div align="center">
  <h1><b>INTRODUCCIÓN A SEÑALES BIOMÉDICAS</b></h1>
</div>

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Marco Teórico](#2-marco-teórico)
   - 2.1 [Artefactos en la señal EEG](#21-artefactos-en-la-señal-eeg)
   - 2.2 [Análisis de Componentes Independientes (ICA)](#22-análisis-de-componentes-independientes-ica)
3. [Materiales y equipos](#3-materiales-y-equipos)
   - 3.1 [Hardware](#31-hardware)
   - 3.2 [Software](#32-software)
4. [Metodología](#4-metodología)
5. [Resultados](#5-resultados)
6. [Análisis de Resultados](#6-análisis-de-resultados)
7. [Discusión](#7-discusión)
8. [Conclusiones](#8-conclusiones)
9. [Bibliografía](#9-bibliografía)

## 1. Introducción
<div align="justify">

La señal de electroencefalografía (EEG) es de muy baja amplitud, lo que la hace especialmente vulnerable a la contaminación por artefactos de origen no cerebral, tales como el parpadeo ocular, la actividad muscular y la interferencia de la red eléctrica. Esta contaminación puede distorsionar significativamente la interpretación de la actividad cortical, particularmente en derivaciones frontopolares (Fp1, Fp2), donde la cercanía a los músculos faciales y oculares agrava el problema.

El Análisis de Componentes Independientes (ICA) es una técnica estadística ampliamente utilizada para separar una señal multivariada en componentes estadísticamente independientes entre sí, permitiendo aislar y remover aquellas componentes asociadas a fuentes no neuronales sin necesidad de descartar el registro completo [1]. En este laboratorio se aplica ICA sobre el registro EEG de dos canales (Fp1, Fp2) adquirido con el sistema BITalino, con el objetivo de identificar y remover artefactos de parpadeo y masticación.

</div>

## 2. Marco Teórico

### 2.1. Artefactos en la señal EEG
<div align="justify">

Los principales artefactos que afectan el registro EEG son de origen ocular (EOG), muscular (EMG) y eléctrico. Los artefactos oculares, generados por el parpadeo, producen un campo eléctrico de gran amplitud que se propaga principalmente hacia los electrodos frontales, afectando a ambos canales con la misma polaridad. Los artefactos musculares (EMG), como los generados por la masticación, se caracterizan por actividad de alta frecuencia e irregular, con picos frecuentes asociados a la activación de unidades motoras [2].

</div>

### 2.2. Análisis de Componentes Independientes (ICA)
<div align="justify">

ICA asume que la señal registrada en cada electrodo es una mezcla lineal de fuentes estadísticamente independientes (actividad cortical, artefactos oculares, artefactos musculares, etc.). El algoritmo estima una matriz de desmezcla que permite recuperar dichas fuentes por separado. Una vez identificadas las componentes asociadas a artefactos —mediante inspección de su topografía espacial y su curso temporal—, estas pueden excluirse y la señal puede reconstruirse proyectando de vuelta únicamente las componentes de interés [1].

Cabe señalar que el número máximo de componentes que ICA puede extraer está limitado por el número de canales disponibles. En un sistema de dos canales, como el empleado en este laboratorio, solo es posible separar un máximo de dos fuentes independientes.

</div>

## 3. Materiales y equipos

### 3.1 Hardware
<div align="justify">

- **Placa BITalino (r)evolution Board Kit BLE/BT:** sistema de adquisición de bioseñales.
- **Sensor de Electroencefalografía (EEG):** módulo analógico con ganancia de 40000 y rango de medición de ±40 µV, conectado a los canales analógicos A1 (Fp1) y A2 (Fp2).
- **Electrodos de superficie Ag/AgCl** y cable de referencia.

</div>

### 3.2 Software
<div align="justify">

- **Google Colab:** entorno de ejecución para el procesamiento de la señal.
- **MNE-Python:** librería especializada en el análisis de señales EEG/MEG, empleada para la construcción del objeto Raw, el filtrado y la implementación de ICA.
- **Picard:** algoritmo de optimización utilizado como método de estimación de ICA.

</div>

## 4. Metodología
<div align="justify">

**Adquisición y carga de datos:** se importó la lectura continua obtenida con el dispositivo BITalino desde los canales analógicos correspondientes a Fp1 y Fp2, con una frecuencia de muestreo de 1000 Hz. Los valores digitales del conversor analógico-digital (ADC) se transformaron a voltios empleando la ecuación de conversión del fabricante, y posteriormente se organizaron en un objeto `RawArray` mediante MNE-Python.

**Filtrado digital:** se aplicó un filtro Notch en 50 Hz y 60 Hz para eliminar la interferencia de la red eléctrica, seguido de un filtro pasa-banda de fase cero entre 0.5 Hz y 40 Hz para acotar la banda fisiológica de interés.

**Implementación de ICA:** dado que el registro cuenta con dos canales físicos, se configuró el algoritmo ICA para extraer exactamente dos componentes independientes, empleando el método de optimización Picard.

**Identificación de artefactos:** se inspeccionaron visualmente la topografía espacial (topomapas) y el curso temporal de cada componente, evaluando su consistencia con los patrones esperados de artefactos oculares o musculares.

**Reconstrucción:** la componente identificada como artefactual fue excluida (`ica.exclude`), reconstruyéndose la señal mediante `ica.apply()`.

**Comparación:** la señal filtrada (pre-ICA) y la señal reconstruida (post-ICA) se compararon en el dominio del tiempo, en el dominio de la frecuencia (densidad espectral de potencia mediante el método de Welch) y en términos de amplitud pico a pico por canal.

</div>

## 5. Resultados

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Im%C3%A1genes%20Laboratorio%20N%C2%B010/senal-cruda.png?raw=true" width="70%">
</p>
<p align="center">
Fig. 1. Señal EEG cruda – Parpadeo + Masticación (Fp1 y Fp2).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Im%C3%A1genes%20Laboratorio%20N%C2%B010/topomapas.png?raw=true" width="70%">
</p>
<p align="center">
Fig. 2. Topomapas de las componentes ICA000 e ICA001.
</p>

<p align="center">
  <img src="PEGA_AQUI_TU_LINK" width="70%">
</p>
<p align="center">
Fig. 3. Curso temporal de las fuentes independientes (ICA000, ICA001).
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Im%C3%A1genes%20Laboratorio%20N%C2%B010/fuentes-ica.png?raw=true" width="70%">
</p>
<p align="center">
Fig. 4. Comparación de la señal pre-ICA y post-ICA en el dominio del tiempo.
</p>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Im%C3%A1genes%20Laboratorio%20N%C2%B010/psd-welch.png?raw=true" width="70%">
</p>
<p align="center">
Fig. 5. Densidad espectral de potencia (Welch) pre-ICA y post-ICA.
</p>

<div align="justify">

Se evaluó el efecto de ICA sobre la grabación de parpadeo y masticación constante, comparando la señal filtrada (pre-ICA) con la señal reconstruida tras excluir la componente ICA000.

Los topomapas mostraron que ICA000 presenta la misma polaridad en ambos canales frontales, patrón típico de un artefacto ocular, dado que el parpadeo afecta a Fp1 y Fp2 de forma casi simultánea y en el mismo sentido. ICA001, en cambio, mostró polaridades opuestas entre canales, patrón más asociado a actividad neural, por lo que se conservó en la reconstrucción.

En cuanto a la amplitud pico a pico, se reportó por canal en lugar de una cifra combinada, ya que esta última queda dominada por el canal de mayor amplitud. El canal Fp1 disminuyó de 96.68 µV a 85.98 µV (reducción de 11.1%), mientras que Fp2 disminuyó de 87.64 µV a 80.67 µV (reducción de 7.9%).

El análisis espectral mediante el método de Welch mostró que la mayor parte de la potencia, tanto antes como después de ICA, se concentra por debajo de 2 Hz. En dicha banda, la reducción fue clara: de aproximadamente 200 a 75 µV²/Hz en Fp1, y de 180 a 70 µV²/Hz en Fp2 (~60% de reducción), consistente con la remoción del componente lento asociado al parpadeo.

</div>

## 6. Análisis de Resultados
<div align="justify">

La diferencia en el porcentaje de reducción entre canales (11.1% en Fp1 frente a 7.9% en Fp2) resulta consistente con lo observado en la señal cruda, donde Fp1 presentó un mayor porcentaje de muestras saturadas en el conversor analógico-digital que Fp2, dado que el rango de medición del sensor EEG (±40 µV) fue superado en ciertos tramos por la magnitud del artefacto. Esto sugiere que el artefacto de parpadeo/masticación tuvo una expresión de mayor magnitud en el electrodo Fp1.

Asimismo, dado que la escala de los gráficos de PSD está dominada por el pico de baja frecuencia asociado al parpadeo, no fue posible evaluar con la misma claridad visual la reducción de potencia en frecuencias superiores a 15 Hz, rango en el que suele manifestarse la contaminación por actividad muscular de la masticación.

</div>

## 7. Discusión
<div align="justify">

El pipeline implementado logró identificar y remover una componente (ICA000) con características consistentes con un artefacto ocular, tanto por su patrón espacial de polaridad uniforme entre canales como por su contribución dominante a la potencia espectral de baja frecuencia.

No obstante, la magnitud de esta reducción debe interpretarse considerando una limitación estructural del diseño experimental. Con solo dos canales EEG, ICA solo puede separar un máximo de dos componentes, mientras que en el registro coexisten al menos tres fuentes fisiológicas distintas: actividad cortical genuina, artefacto ocular y artefacto muscular por masticación. Al existir más fuentes que canales, el sistema se encuentra subdeterminado: ICA logra aislar razonablemente bien una fuente (el parpadeo), pero la segunda componente retenida queda como una mezcla residual entre actividad neural genuina y contaminación muscular no separada. Esto explica por qué no se observó una reducción clara de potencia en las bandas de frecuencia más altas, típicamente asociadas a la actividad electromiográfica.

Adicionalmente, la presencia de saturación del ADC en la señal cruda constituye una consideración relevante, ya que ICA asume un modelo de mezcla lineal entre fuentes, supuesto que puede verse comprometido ante la presencia de no linealidades como el recorte (clipping) de la señal.

</div>

## 8. Conclusiones
<div align="justify">

ICA constituye una herramienta útil incluso en configuraciones mínimas de dos canales para atenuar artefactos oculares dominantes, logrando en este laboratorio una reducción de la amplitud pico a pico de 11.1% en Fp1 y 7.9% en Fp2 tras la exclusión de la componente asociada al parpadeo.

Sin embargo, su capacidad para separar múltiples fuentes de contaminación simultáneas —como ocurre en condiciones de parpadeo y masticación concurrentes— se encuentra intrínsecamente limitada por el número de electrodos disponibles, dado que el número de componentes que ICA puede extraer nunca puede superar el número de canales de registro. Una extensión natural de este trabajo consistiría en replicar el análisis con un sistema de adquisición de mayor número de canales, lo que incrementaría los grados de libertad espaciales disponibles para el algoritmo y permitiría una separación más fina entre actividad neural y las distintas fuentes de artefacto.

</div>

## 9. Bibliografía
<div align="justify">

[1] Dharmaprani D, Nguyen HK, Lewis TW, DeLosAngeles D, Willoughby JO, Pope KJ. A Comparison of Independent Component Analysis Algorithms and Measures to Discriminate between EEG and Artifact Components. In: 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). Orlando, FL, USA: IEEE; 2016. p. 825–828. doi:10.1109/EMBC.2016.7590828.

[2] BITalino (r)evolution Lab Guide [Internet]. Available from: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[3] MNE-Python Documentation [Internet]. Available from: https://mne.tools/stable/index.html

</div>
