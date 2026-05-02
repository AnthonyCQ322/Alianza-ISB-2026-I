<div align="center">
  <h1><b>LABORATORIO N°5: Adquisición de señales ECG</b></h1>
  <p>Universidad Peruana Cayetano Heredia</p>
  <h1><b>BITAlino para ECG</b></h1>
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



## 1. Introducción
<div align="justify">
El electrocardiograma (ECG) es un método de registro que hace posible la medición de la actividad eléctrica del corazón producida en cada ciclo cardiaco [1]. Esta actividad surge de la propagación de potenciales de acción en el músculo cardíaco, los cuales generan diferencias de potencial que pueden ser registradas en la superficie del cuerpo a través de electrodos [2]. Para obtenerla, se amplifica y registra la señal, lo que posibilita el análisis de las diferentes etapas del ciclo cardíaco. 
  
El ECG se puede registrar a través de diferentes disposiciones de electrodos que se conocen como derivaciones, entre ellas se encuentran las derivaciones bipolares de Einthoven (I, II y III), que permiten ver la actividad eléctrica del corazón desde diferentes perspectivas en el plano frontal [3]. Estas derivaciones forman el denominado triángulo de Einthoven, cuya respuesta depende de la dirección del vector de despolarización cardíaca, influyendo en la amplitud y polaridad de las ondas registradas. 

En este laboratorio, la obtención de la señal ECG se lleva a cabo con el sistema BITalino (r)evolution y el programa OpenSignals, que hacen uso de electrodos de superficie del tipo Ag/AgCl. También se analiza cómo la elección de las derivaciones I, II y III, así como el cambio en la posición de los electrodos, impactan en la morfología y calidad de la señal ECG adquirida, siguiendo la metodología propuesta en la guía del sistema [4]. 
</div>


## 2. Objetivos
-  Comprender el origen fisiológico de la señal electrocardiográfica (ECG). Adquirir señales ECG en tiempo real utilizando el sistema BITalino y el software OpenSignals. 
- Adquirir señales ECG en tiempo real utilizando el sistema BITalino y el software OpenSignals. 
- Evaluar el efecto de la posición de los electrodos en las derivaciones I, II y III del ECG.
- Analizar la influencia del ruido y otros factores (movimiento, respiración) en la calidad de la señal ECG.


## 3. Materiales y Equipos
### Hardware
- **Placa BITalino (r)evolution Assembled Core BT**, es el sistema principal de adquisición de señales y que a su vez se comunica vía Bluetooth.
- **Sensor de Electrocardiografía (ECG)**, ayuda en capturar la actividad eléctrica cardíaca.
- **3 Electrodos de superficie,** en este caso se utilizó electrodos desechables pre gelificados de Ag/AgCl.
  

### Software
- **OpenSignals (r)evolution**, es el software que va en conjunto del BITalino para capturar, visualizar y guardar la señal ECG en tiempo real.
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
1. **Q1.What are the most typical types of noise sources affecting ECG?**
<br>Diversas fuentes de ruido pueden influir en las señales de ECG, lo que las degrada y complica su análisis. Algunas de las más frecuentes son:

Desviación de la línea base (BW, por sus siglas en inglés): Es una fluctuación de baja frecuencia provocada principalmente por la respiración, el movimiento del cuerpo o las alteraciones en el contacto entre el electrodo y la piel.

Interferencia de la red eléctrica (conocida como PLI): Ruido generado por campos electromagnéticos de aparatos eléctricos próximos, que se distingue por una señal sinusoidal con frecuencia de 50 o 60 Hz.
Ruido electromiográfico (EMG): Se produce por la actividad eléctrica de los músculos esqueléticos, en particular durante las contracciones o el movimiento, cuyos elementos de frecuencia pueden sobreponerse con el complejo QRS. 

Artefactos de movimiento y electrodos (EM/MA): Son generados por el movimiento de los electrodos o cables, que cambia la impedancia al entrar en contacto con la piel.

Ruido blanco gaussiano aditivo (AWGN): Ruido aleatorio que es generado por los sistemas electrónicos de adquisición.

Por consiguiente, el conjunto de estos ruidos tienen la posibilidad de alterar la interpretación de la señal ECG. Por lo que es crucial disminuirlos a través de una colocación apropiada de electrodos y condiciones de adquisición [A], [B].




2. **Q2.Why does the change of the positioning of the sensors (lead I-III) change the ECG signal components? How do the components change?** <br>
Para cada variación o cambio de posición de los sensores de ECG se observa la actividad eléctrica del corazón desde un ángulo espacial diferente.  
La excitación de las células musculares cardíacas genera un vector dipolo que se propaga a las células vecinas, las derivaciones bipolares (I, II, II) miden al vector bipolar en el plano frontal con las diferentes combinaciones de los electrodos positivos y negativos.
Los componentes cambian de la siguiente manera:
Dirección de la amplitud: Cuando el vector de despolarización se acerca hacia el electrodo positivo de la derivación entonces el componente en el ECG será una onda con deflexión positiva pero si se aleja del electrodo positivo entonces será una deflexión negativa.  
Tamaño de la amplitud: El tamaño depende del ángulo de dirección de la derivación respecto al vector eléctrico del corazón cuando el dipolo es paralelo a la línea de la derivación su amplitud será máxima.

3. **Q3.Describe if there are major differences in the signal when acquiring the signal from different body locations (e.g., wrist / collarbone/ chest). What could be the cause? Did you expect such changes in the signal? Store a signal segment of each to visualize the differences.** <br>
Si existen diferencias de la señal, sobre todo la amplitud y polaridad del complejo QRS si se cambia la posición de referencia de los electrodos.


-La actividad eléctrica del corazón surge de la propagación de potenciales de acción que generan un vector dipolar tridimensional cambiante. 
La amplitud y forma de la onda registrada dependen del ángulo de ese vector de despolarización relativo al eje de medición. Los electrodos en el pecho están físicamente más cerca del miocardio, por lo que registran una amplitud mucho mayor y capturan detalles específicos de las cámaras cardíacas (ventrículos). 
En cambio, las posiciones como las muñecas y cresta ilíaca proyectan este vector tridimensional en el plano frontal bidimensional (el triángulo de Einthoven), resultando en amplitudes menores atenuadas por la impedancia de un mayor volumen de tejido.


-Estos cambios morfológicos eran completamente esperados basándose en los principios teóricos del triángulo de Einthoven y las derivaciones bipolares, donde la magnitud proyectada alcanza su máximo cuando el dipolo cardíaco es paralelo a la línea trazada entre los electrodos [3].


4. **Q4.The cardiac and the respiratory systems are well interconnected as is well known. Do you expect that different types of breathing (e.g. faster, deeper) to influence the ECG signals? Show screenshots of ECG signals in different respiratory circumstances and described the variations if there are any.** <br>
Si se espera que los diferentes tipos de respiración afecten estas señales, ya que tanto el sistema respiratorio como el cardiovascular presentan una conexión. Al realizar una comparación entre nuestra linea basal y la hiperventilación se encuentran algunas diferencias:





5. **Q5. In Home-Guide #1 you have seen that different amounts of force produced in the muscle generated signals with different amplitudes. How does movement influence your ECG signal?** <br>
El ruido producido por la contracción de los músculos en el ECG se conoce como artefacto electromiográfico. Durante la adquisición de la señal, la actividad eléctrica de los músculos cercanos a los electrodos presenta un contenido espectral de banda ancha, extendiéndose predominantemente hacia frecuencias más altas (>10 Hz) y superponiéndose con el espectro del complejo QRS [M]. Como consecuencia, la presencia de ruido electromiográfico provoca una interpretación inexacta del ECG, lo que puede derivar en un diagnóstico erróneo de enfermedades cardíacas, decisiones de tratamiento inapropiadas y la generación de falsas alarmas [N].


6. **Q6.To the best of your knowledge, how can you detect bradycardia and tachycardia in the ECG signal?** <br>

Taquicardia: Se identifica en el ECG por un acortamiento evidente de los intervalos R-R. Se detecta cuando la frecuencia media constante supera los 100 lpm.
Bradicardia: Se identifica en el ECG por un alargamiento de los intervalos R-R, mostrando picos muy separados entre sí. 
Se detecta cuando la frecuencia media en reposo desciende por debajo de los 60 lpm.

La bradicardia y la taquicardia se detectan principalmente analizando la distancia temporal entre latidos consecutivos en la señal de ECG, específicamente calculando el intervalo R-R (el tiempo transcurrido entre dos picos R sucesivos del complejo QRS). Con este intervalo, se calcula la frecuencia cardíaca (FC) usando la relación [5].

FC =  60RR 
Donde FC está en latidos por minuto y RR en segundos.




## 8. Bibliografía
[1] Fundación Española del Corazón. Electrocardiograma [Internet]. Madrid: Fundación Española del Corazón; [citado 28 abr 2026]. Disponible en: https://fundaciondelcorazon.com/informacion-para-pacientes/metodos-diagnosticos/electrocardiograma.html 
[2] Zavala-Villeda JA. Descripción del electrocardiograma normal y lectura del electrocardiograma [Internet]. Revista Mexicana de Anestesiología. Ciudad de México: Colegio Mexicano de Anestesiología; 2017 [citado 28 abr 2026]. Disponible en: https://www.medigraphic.com/pdfs/rma/cma-2017/cmas171bj.pdf 
[3] Klabunde RE. Heart Failure - Introduction [Internet]. En: Cardiovascular Physiology Concepts. 2nd ed. [citado 28 abr 2026]. Disponible en: https://cvphysiology.com/heart-failure/hf002 
[4] BITalino. BITalino (r)evolution Lab Guide: Experimental Guides to Meet & Learn Your Biosignals [Internet]. [citado 28 abr 2026]. Disponible en: https://bitalino.com/storage/uploads/media/revolution-lab-guide.pdf
[5]J. Pan and W. J. Tompkins, "A Real-Time QRS Detection Algorithm," in IEEE Transactions on Biomedical Engineering, vol. BME-32, no. 3, pp. 230-236, March 1985, 
doi: 10.1109/TBME.1985.325532.
https://ieeexplore.ieee.org/document/4122029

[A] Midani W, Ltifi H, Ben Ayed M. A comprehensive review of noise removal techniques in ECG signal processing. Procedia Comput Sci. 2025;270:4134–4143. doi:10.1016/j.procs.2025.09.538.  
[B] Vinzio Maggio AC, Bonomini MP, Laciar Leber E, Arini PD. Cuantificación de la dispersión de la repolarización ventricular mediante procesamiento digital del ECG de superficie. Buenos Aires: Instituto Argentino de Matemática “A. Calderón”, CONICET; 2012 Jan. doi:10.5772/23050. 
 
[M] V. Atanasoski et al., “A Morphology-Preserving algorithm for denoising of EMG-Contaminated ECG signals,” IEEE Open Journal of Engineering in Medicine and Biology, vol. 5, pp. 296–305, Jan. 2024, doi: 10.1109/ojemb.2024.3380352.

[N] X. An, Y. Liu, Y. Zhao, S. Lu, G. K. Stylios, and Q. Liu, “Adaptive motion artifact reduction in wearable ECG measurements using impedance pneumography signal,” Sensors, vol. 22, no. 15, p. 5493, Jul. 2022, doi: 10.3390/s22155493.

