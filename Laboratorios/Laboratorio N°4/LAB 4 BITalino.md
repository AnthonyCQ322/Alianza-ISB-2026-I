<div align="center">
  <h1><b>LABORATORIO N°4: Adquisición de señales sEMG</b></h1>
  <p>Universidad Peruana Cayetano Heredia</p>
  <h1><b>BITAlino para EMG</b></h1>
</div>

<div  align="center">
  <h1><b>INTRODUCCIÓN A SEÑALES BIOMÉDICAS</b></h1>
</div>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/bitalino.png" width="70%">
</p>

## Tabla de contenidos
1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Materiales y equipos](#3-materiales-y-equipos)
4. [Procedimiento](#4-procedimiento)
5. [Resultados](#5-resultados)
6. [Discusión](#6-discusión)
   - 6.1 [Análisis de Resultados](#61-análisis-de-resultados)
   - 6.2 [Limitaciones](#62-limitaciones)
7. [Quiz](#7-quiz)
8. [Bibliografía](#8-bibliografía)

---

## 1. Introducción
<div align="justify">
La electromiografía (EMG) es una técnica que se usa en gran medida para registrar la actividad eléctrica de los músculos, mediante la medición de los potenciales producidos durante la contracción muscular, siendo representativa la actividad neuromuscular y útil para análisis del movimiento, diagnóstico de enfermedades del sistema motor y rehabilitación [1].

Para la adquisición de señales EMG, se pueden aplicar técnicas invasivas, que utilizan electrodos introducidos en el músculo, o la electromiografía de superficie (sEMG), que utiliza electrodos ubicados en la superficie de la piel. Esta última técnica, muestra la actividad de varias unidades motoras superpuestas, además tiene un mayor uso debido a que es menos incómoda para el paciente y no es invasiva [1,2].

Las señales sEMG tienen amplitudes que varían entre microvoltios y milivoltios, lo cual las vuelve muy propensas a interferencias de ruido, como artefactos de movimiento. Por ello, necesitan ser procesadas para conseguir una señal de alta calidad [2]. A partir de estas señales se pueden medir parámetros como la coordinación entre grupos musculares, la fatiga y la activación muscular a partir de estas señales.

Para una correcta adquisición, es esencial garantizar que el sensor y la piel estén bien acoplados usando electrodos pregelificados. Además, dispositivos como BITalino permiten la adquisición portátil y accesible de señales sEMG, facilitando su registro en tiempo real y posterior análisis [3].

</div>


## 2. Objetivos
- Registrar señales de sEMG tanto en estados de reposo como de contracción muscular.
- Determinar las propiedades fundamentales de la señal, como su variabilidad y amplitud.
- Evaluar el nivel de calidad de la señal considerando la presencia de ruido y la ubicación de los electrodos.

## 3. Materiales y Equipos
### Hardware
- **Electrodos:** Superficie de Ag/AgCl desechables.
- **Placa de adquisición:** BITalino (incluye microcontrolador, módulo EMG y Bluetooth).
- **Cables:** Cable de electrodos de 3 vías con conectores tipo snap.
- **Batería:** Li-Po (3.7V).

### Software
- **OpenSignals (r)evolution:** Visualización y adquisición en tiempo real.
- **Google Colab (Python):** Procesamiento digital y análisis de datos.

## 4. Procedimiento
1. **Limpieza de Piel:** <br>Se buscó una zona de poca vellosidad y se procedió a limpiar la zona del músculo a evaluar.
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/Limpieza.png" width="80%">
</p>
<p align="center">
  Imágen 1: Materiales de limpieza con el brazo sin electrodos
</p>  

2. **Conexión del equipo:** <br>Se conecta el cable de 3 vías al puerto que indica EMG del BITalino (se puede visualizar en su datasheet) y se energiza la placa conectándolo a la batería Li-Po.

3. **Colocación de electrodos:** <br>Una vez identificado el músculo que se desea evaluar se procede a colocar los electrodos de medición en el músculo alineados en el sentido de las fibras musculares y el electrodo de referencia se coloca en una zona ósea eléctricamente neutra como el codo.
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/Electrodos%20en%20bicep.png" width="80%">
</p>
<p align="center">
  Imágen 2: Colocación de electrodos en el bíceps con la referencia en el codo.
</p>  

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/Electrodos%20en%20tricep.png" width="80%">
</p>
<p align="center">
  Imágen 3: Colocación de electrodos en el trícep con la referencia en el codo.
</p> 


4. **Conectividad del BITalino con Software:** <br>una vez encendido el BITalino se empareja mediante Bluetooth con la computadora para que posteriormente se use con el Software.
   
5. **Configuración del Software:** <br>se abre el software OpenSignals y se configura el dispositivo ingresando su dirección MAC, seleccionamos el canal correspondiente al sensor de EMG y se establece la frecuencia de muestreo.
   
6. **Tomas de movimiento:** <br>se inició la grabación en el OpenSignals con las tres repeticiones de contracciones para cada músculo (bicep y tricep), se realizó una en reposo, una sin fuerzas en contra del movimiento y una sometida a una fuerza al sentido contrario del recorrido del músculo, entre cada repetición hubo un minuto de reposo.
<p align="center">
  
https://github.com/user-attachments/assets/2694219f-ec41-4563-9e8a-908b10dbf7e5

</p>
<p align="center">
  Video 1: Grabación del brazo con el bíceps en reposo.
</p>  

<p align="center">

https://github.com/user-attachments/assets/5070b867-e1d1-4596-a6e3-b01c3ad91cf5
</p>
<p align="center">
  Video 2: Grabación del movimiento del brazo con el bíceps en contracción.
</p>  

<p align="center">

https://github.com/user-attachments/assets/9a7af7b2-5c45-4404-8cd5-7f5c67dce424
</p>
<p align="center">
  Video 3: Grabación del movimiento del brazo con el bíceps en contracción sometido a fuerzas en el sentido contrario al movimiento.
</p>  

<p align="center">

https://github.com/user-attachments/assets/f4e355d3-a776-402f-a6a8-03769794a1d7
</p>
<p align="center">
  Video 4: Grabación del brazo con el tricep en reposo.
</p>   

<p align="center">

https://github.com/user-attachments/assets/db4d7539-e163-4ded-ad6f-a7e125c66b2a
</p>
<p align="center">
  Video 5: Grabación del movimiento del brazo con el tricep en contracción sometido a fuerzas en el sentido contrario al movimiento.
</p>  

7. **Análisis y Procesamiento Digital:** <br>finalizando la grabación se exporto los datos a google collab, en python se importa la librería de opensignalsreader y se graficaron respecto al tiempo cada una de las señales y posteriormente se filtro la señal por Notch (Rechaza Banda) y Pasa Banda, para finalmente obtener transformada rápida de fourier de las distintas señales.


## 5. Resultados
1. **Bíceps – Reposo** 
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%201.png" width="70%">
</p>
<p align="center">
  Imágen 4: Señal EMG de bíceps en reposo (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%202.png" width="70%">
</p>
<p align="center">
  Imágen 5: Espectro de frecuencia – Bíceps en reposo (señal filtrada)
</p>

2. **Bíceps – Flexión**
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%203.png" width="70%">
</p>
<p align="center">
  Imágen 6: Señal EMG de bíceps durante flexión (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%204.png" width="70%">
</p>
<p align="center">
  Imágen 7: Espectro de frecuencia – Bíceps en flexión
</p>

3. **Bíceps – Flexión con peso**
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%205.png" width="70%">
</p>
<p align="center">
  Imágen 8: Señal EMG de bíceps durante flexión con peso (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%206.png" width="70%">
</p>
<p align="center">
  Imágen 9: Espectro de frecuencia – Bíceps en flexión con peso
</p>

4. **Tríceps – Reposo**
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%207.png" width="70%">
</p>
<p align="center">
  Imágen 10: Señal EMG de tríceps en reposo (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%208.png" width="70%">
</p>
<p align="center">
  Imágen 11: Espectro de frecuencia – Tríceps en reposo
</p>

5. **Tríceps – Extensión**
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%209.png" width="70%">
</p>
<p align="center">
  Imágen 12: Señal EMG de tríceps durante extensión (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%2010.png" width="70%">
</p>
<p align="center">
  Imágen 13: Espectro de frecuencia – Tríceps en extensión
</p>

6. **Tríceps – Extensión con peso**
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%2011.png" width="70%">
</p>
<p align="center">
  Imágen 14: Señal EMG de tríceps durante extensión con peso (cruda vs. filtrada)
</p>
<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/FIGURA%2012.png" width="70%">
</p>
<p align="center">
  Imágen 15: Espectro de frecuencia – Tríceps en extensión con peso
</p>

<div align="justify">
Se obtuvieron registros de la actividad eléctrica para los músculos bíceps y tríceps. Los resultados se dividen en el análisis morfológico de la señal en el dominio del tiempo y la distribución de su energía en el dominio de la frecuencia.
</div>

## 6. Discusión
### 6.1 Análisis de Resultados
<div align="justify">
  
- **Análisis en el Dominio del Tiempo:** Las gráficas representan la amplitud de la señal sEMG (en milivoltios) a lo largo del tiempo para las tres condiciones evaluadas: reposo, contracción sin carga y contracción con fuerza en contra.
  
- **Estado de Reposo:** La señal se mantuvo en una línea base estable con una amplitud mínima, promediando un valor de casi 0mV y este pequeño error es solo por picos mínimos en 8 y 20 segundos muy similar en ambos. Se observa únicamente un nivel bajo de ruido de fondo, lo cual indica un buen acoplamiento de los electrodos y ausencia de activación de unidades motoras.
  
- **Contracción sin fuerzas en contra:** Al iniciar el movimiento voluntario, se registró una ráfaga de potenciales de acción de unidad motora (MUAPs). La amplitud pico a pico aumentó significativamente, alcanzando rangos de -0.3mV a 0.4mV para bíceps, mientras que para los tríceps presentaron un gran aumento de amplitud [-1 ; 1.5]mV, ambos evidencias un patrón de interferencia moderado.

- **Contracción sometida a fuerza en contra:** Durante la contracción isométrica/isotónica con resistencia, la señal mostró su máxima amplitud, llegando a picos de [-0.7 ; 1]mV para los bíceps, mientras que los tríceps presentaron [-1.5 ; 1.7] siendo este pico máximo durante los 40 segundos, luego el músculo se relajo y presentó amplitudes menores.

- El patrón de interferencia se volvió mucho más denso, lo cual refleja un mayor reclutamiento de unidades motoras y un incremento en su tasa de disparo espacial y temporal para vencer la resistencia mecánica.

- **Análisis en el Dominio de la Frecuencia (Transformada de Fourier):** Para evaluar el contenido espectral de las señales, se aplicó la Transformada Rápida de Fourier (FFT), limitando la visualización del espectro al ancho de banda fisiológico útil de 0 a 500 Hz.

</div>

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/TABALA%20DE%20SEÑALES%20EMG.png" width="80%">
</p>
<p align="center">
  Imágen 16: Tabla de las distribuciones de las gráficas para los distintos movimientos de biceps y tricep.
</p>

<div align="justify">
En el dominio de la frecuencia, se comprueba que el contenido energético principal de las contracciones musculares del brazo (músculos grandes) se encuentra acotado en el rango de 50 Hz a 150 Hz. Asimismo, se observa una atenuación drástica de la señal al acercarse a los 300 Hz, lo que concuerda con la teoría fisiológica de la electromiografía de superficie
</div>

### 6.2 Limitaciones
<div align="justify">
Las señales de EMG superficial (sEMG) obtenidas en este experimento se enfrentaron a una serie de limitaciones inherentes a esta técnica de medición, así como a factores ambientales y metodológicos.

La sEMG mide la actividad muscular en el rango de microvoltios (μV), es extremadamente susceptible a la interferencia electromagnética (EMI) [4]. En la experiencia, esta susceptibilidad se vio incrementada por la presencia simultánea de varias fuentes de ruido, una situación que compromete la integridad de las señales y puede llevar a interpretaciones erróneas. Aunque se empleó un filtro notch para mitigar la interferencia de la red eléctrica, la presencia de múltiples dispositivos electrónicos cercanos generó ruido adicional que afecta la calidad de la señal.

Por otro lado, la señal presenta una limitación inherente en su resolución espacial debido al efecto de volumen conductor. La señal registrada en la superficie corresponde a una suma espacio-temporal de múltiples unidades motoras activas en la región de captación. Además, la señal se ve modificada al atravesar tejidos como piel, grasa y fascia, lo que altera su forma original. Esto impide localizar con precisión la fuente de la actividad eléctrica y limita el análisis detallado del control neuromuscular [5].

La calidad de la señal de sEMG depende críticamente de la impedancia en la interfaz piel-electrodo. Una alta impedancia dificulta la correcta transmisión de la señal eléctrica y favorece la aparición de ruido y artefactos [6]. Para la experiencia, los factores como la presencia de vello y la ausencia de gel electrolítico afectaron negativamente esta interfaz. La falta de una adecuada preparación de la piel redujo la estabilidad del contacto, comprometiendo la calidad del registro obtenido. Además se tiene se debe tener en cuenta el artefacto dado por el movimiento del cable de los electrodos que se encuentra en un rango de 1 a 50 Hz [6].

La proximidad anatómica y funcional de los músculos del brazo representa un riesgo significativo de diafonía o 'crosstalk', definida como una fuente importante de error en la interpretación de las señales de EMG superficial. Dado que el bíceps y el tríceps son músculos antagonistas y están muy próximos, existe la posibilidad de que la señal detectada sobre uno de ellos contenga actividad eléctrica proveniente del otro. Este riesgo es mayor durante las contracciones, cuando la actividad eléctrica en el músculo activo es sustancialmente mayor [7].

</div>

## 7. Quiz
1. **Q1.Which are the significant frequencies for EMG acquisitions? Are they the same in all body areas such as facial area?**
<br>La señal de electromiografía (EMG) se ve directamente afectada por la frecuencia (o velocidad) de disparo de las unidades motoras,en la mayoría de las condiciones, estas unidades motoras se activan o disparan en una región de frecuencia que generalmente está en el rango útil de 20-450 Hz, las señales más bajas de 20Hz representan artefactos, como el movimiento y la respiración, mientras que superiores a 500 Hz son principalmente ruido.
Aunque la frecuencia de disparo de las unidades motoras base puede moverse en rangos similares, los músculos faciales son mucho más pequeños y complejos que los músculos esqueléticos de las extremidades. Tienen una menor cantidad de fibras por unidad motora, lo que puede influir en su patrón de reclutamiento y en las frecuencias de interferencia.
En músculos grandes como los bíceps presentan señales más lentas, por el tamaño del músculo, entre 50 y 150 Hz, mientras que músculos más pequeños como los faciales tienen una activación más fina y rápida que se traduce en frecuencias más altas

3. **Q2. Which kind of filter is essential when working with EMG signals? Why do we need to apply such a filter?** <br>Utilizamos dos tipos de filtros para las señales EMG estos son el Filtro Notch (Rechaza Banda) y el filtro Pasa Banda.
Filtro Notch: Este ayuda a eliminar la interferencia de la red eléctrica, nuestro cuerpo humano, cables de los electrodos captan el ruido electromagnético de 60 Hz que irradia la red eléctrica local y los electrodomésticos cercanos. Entonces este filtro suprime esta frecuencia sin distorsionar la señal muscular.
Filtro Pasa Banda: Normalmente es usado en el rango de 20 a 500 Hz, necesitamos separar las frecuencias fisiológicos útiles, aquellas que son menores de 20 Hz se filtran para eliminar los artefactos de movimiento y las frecuencias mayores a 500 Hz se filtran para eliminar el ruido electrónico de alta frecuencia.

4. **Q3. How does the amplitude differ in each muscular contraction? Is there a difference for body locations?** <br>La amplitud de la señal de electromiografía de superficie (sEMG) aumenta cuando la contracción muscular es más intensa, debido al reclutamiento de más unidades motoras y al incremento de su frecuencia de disparo [8]. Sin embargo, esta relación no es lineal, por lo que la amplitud no permite estimar la fuerza muscular con precisión [9].
Respecto a la ubicación en el cuerpo, existen diferencias importantes. Los músculos que están más cerca de la piel (superficiales) dan una amplitud más grande que los profundos, porque la grasa y otros tejidos que hay por encima atenúan la señal eléctrica. Por ejemplo, Kuiken y colaboradores [10], comprobaron que con solo 9 mm de grasa subcutánea la amplitud de la señal sEMG se reduce más del 80%, y con 18 mm la reducción llega al 90%. Esto explica por qué músculos pequeños pero superficiales (como los de la mano) pueden tener una señal mucho más alta que músculos enormes pero profundos (como el glúteo).

4. **Q4.Show a screenshot of a relevant portion of Electromyography (EMG) data within the experiment proposed on Section D of a facial muscle of interest. Does this signal correspond to what you expected? Why? Which emotion and action did you perform to trigger the muscle? Which muscle did you trigger?** <br>La lectura y grafica del EMG en la seccion del musculo facial no se realizo en nuestro grupo pero para observar nuevos cambios en la gráfica, el usuario debe de de realizar gesticulaciones faciales como la sonrisa que es de las mas notorias, con este movimiento se activa los músculos del cigomático mayor.

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Im%C3%A1genes%20Laboratorio%20N%C2%B04/EMG%20facial.png" width="80%">
</p>

5. **Q5. To the best of your knowledge, does the EMG amplitude equal to the amount of force that you have generated with your muscle?** <br>No equivalen lo mismo, ya que la señal EMG mide la activación eléctrica generada por los músculos y no el resultado mecánico (la fuerza aplicada). Esta diferencia varía drásticamente en la fatiga ya que la señal eléctrica aumenta para poder mantener una misma fuerza, estos también cambia según la longitud del músculo y qué tipo de movimiento se realiza .


## 8. Bibliografía
1. Boyer M, Bouyer L, Roy JS, Campeau-Lecours A. Reducing noise, artifacts and interference in single-channel EMG signals: a review. Sensors (Basel). 2023;23(6):2927. doi: 10.3390/s23062927.
2. Rey Vicente N. Desarrollo de una solución hardware y software para la recogida y procesamiento de señales fisiológicas [trabajo de fin de grado]. Valladolid: Universidad de Valladolid; 2022.
3. BITalino. Home guide: EMG sensor [Internet]. PLUX Wireless Biosignals SA; 2022 [citado 2026 Abr 23]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf
4. Marcarian D. Protecting bioelectric signals from electromagnetic interference in a wireless world. En: Biomedical engineering. IntechOpen; 2022. doi: 10.5772/intechopen.105951.
5. Arekhloo NG, et al. Investigating the volume conduction effect in MMG and EMG during action potential recording. En: Proceedings of the 29th IEEE International Conference on Electronics, Circuits and Systems (ICECS); 2022 Oct. p. 1 doi: 10.1109/ICECS202256217.2022.9971020.
6. McManus L, De Vito G, Lowery MM. Analysis and biophysics of surface EMG for physiotherapists and kinesiologists: toward a common language with rehabilitation engineers. Front Neurol. 2020;11:576729. doi: 10.3389/fneur.2020.576729.
7. Germer CM, Farina D, Elias LA, Nuccio S, Hug F, Del Vecchio A. Surface EMG cross talk quantified at the motor unit population level for muscles of the hand, thigh, and calf. J Appl Physiol. 2021;131(2):808–20. doi: 10.1152/japplphysiol.01041.2020.
8. Farina D, Merletti R, Enoka RM. The extraction of neural strategies from the surface EMG. J Appl Physiol. 2004;96(4):1486-95. doi: 10.1152/japplphysiol.01070.2003.
9. Disselhorst-Klug C, Schmitz-Rode T, Rau G. Surface electromyography and muscle force: limits in sEMG-force relationship and new approaches for applications. Clin Biomech (Bristol, Avon). 2008;23(1):1-10. doi: 10.1016/j.clinbiomech.2008.09.003.
10. Kuiken TA, Lowery MM, Stoykov NS. The effect of subcutaneous fat on myoelectric signal amplitude and cross-talk. Prosthet Orthot Int. 2003;27(1):48-54. doi: 10.3109/03093640309167976.
