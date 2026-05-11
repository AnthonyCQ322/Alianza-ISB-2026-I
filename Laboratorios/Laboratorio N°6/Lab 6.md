<div align="center">
  <h1><b>LABORATORIO N°6: Filtros Digitales</b></h1>
  <p>Universidad Peruana Cayetano Heredia</p>
  <h1><b>Filtros Digitales</b></h1>
</div>

<div  align="center">
  <h1><b>INTRODUCCIÓN A SEÑALES BIOMÉDICAS</b></h1>
</div>

<div align="justify">
En el procesamiento de señales biomédicas como ECG, EEG, EMG, se han desarrollado diferentes filtros digitales con la finalidad de reducir el ruido y mejorar la calidad de la señal adquirida. 
Estos filtros permiten eliminar interferencias indeseables, facilitando un análisis más preciso de la información fisiológica; dentro de los principales filtros digitales utilizados encontramos los filtros pasa-bajos, pasa-altos, pasa-banda, notch, FIR e IIR, los cuales se presentarán y describirán a continuación:
</div>

<div align="justify">
  
# **Filtro Notch**
Los filtros digitales notch, son componentes esenciales en el procesamiento de bioseñales, diseñados para suprimir frecuencias de interferencia específicas, generalmente provenientes de la red eléctrica (50 o 60 Hz), es un tipo de filtro rechazabanda fabricado a partir de una combinación de filtros pasa altos y pasa bajos, también se denominan "filtros de rechazo de banda" [1].

<p align="center">
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°4/bitalino.png" width="70%">
</p>

<div  align="center">
  <h1><b>Fig 1. Filtro Notch (Fuente: MathWorks)</b></h1>
</div>

1. **Aplicación en Electrocardiografía (ECG)**
   
El problema principal en el ECG consiste en eliminar el ruido de la red eléctrica, sin distorsionar los componentes morfológicos importantes de la señal, como el complejo QRS.
Los filtros notch digitales pueden suprimir ruido a niveles mayores de 40 dB, y usando filtros IIR se han mostrado eficaces para rechazar interferencias de 50 Hz con bajos errores cuadráticos medios (aproximadamente 0.225) [2]

2. **Aplicación de Electromiografía (EMG)**
   
En el procesamiento de las señales EMG, el filtrado es más complejo ya que la energía de la señal muscular se solapan significativamente con la frecuencia de la red eléctrica. Para reducir este ruido se utilizan habitualmente filtros Butterworth de segundo orden que permiten atenuar los componentes de baja frecuencia (por ejemplo < 50 Hz) y de alta frecuencia (por ejemplo > 150 Hz). 
Para el EMG superficial (sEMG), se han sugerido diseños de filtravdo más avanzados que incluyen filtros “band-stop” para eliminar la frecuencia fundamental de la red eléctrica y sus armónicos. Estos sistemas suelen tener un filtro pasa alto de segundo orden con frecuencia de corte de 10 Hz, un filtro pasa bajo de octavo orden con corte a 400 Hz y seis filtros banda detenida de segundo orden centrados en 60 Hz y sus armónicos hasta 360 Hz.
En este sentido, los filtros FIR pueden ofrecer mejores resultados que los filtros IIR en sistemas de reconocimiento de patrones basados en sEMG, ya que preservan mejor los detalles de la señal y presentan una respuesta de fase lineal [3].

3. **Aplicación en Electroencefalografía (EEG)**

El EEG es muy sensible a interferencias periódicas, que pueden ser difíciles de reconocer visualmente porque las ondas cerebrales son irregulares.
El proceso estándar consiste en identificar el impulso de 60 Hz en el espectro de potencia de la señal antes de aplicar el filtro.
Los filtros digitales notch, al ser implementados, proporcionan atenuaciones significativas, mayores de 40 dB, preservando así la señal cerebral útil del ruido eléctrico [4].

  
# **Filtro Pasa - bajos**
El filtro pasa-bajos es uno de los componentes más fundamentales en el procesamiento digital de bioseñales. Su función principal es permitir el paso de frecuencias por debajo de una frecuencia de corte (fc) y atenúa las componentes de alta frecuencia no deseadas. En bioseñales, este filtro es esencial para eliminar ruido de alta frecuencia como artefactos musculares, interferencias electromagnéticas ambientales y ruido térmico de los electrodos [5]. 

1. **Aplicación en Electrocardiografía (ECG)**
   
La señal ECG registra la actividad eléctrica cardíaca en un rango fisiológico de 0.05 a 120 Hz [6]. Las componentes de frecuencia por encima de este rango corresponden a ruido de alta frecuencia de baja amplitud, interferencias electromagnéticas y potenciales miográficos que contaminan la señal cardíaca útil. El filtro pasa-bajos actúa eliminando estas componentes no deseadas, preservando la morfología de componentes importantes como el complejo QRS, la onda P y el segmento ST. Su implementación sobre señales reales de la base de datos MIT-BIH demuestra una reducción del error cuadrático medio (MSE) de 202.83 a 127.25 respecto al filtrado Gaussiano convencional, preservando las ondas características de la señal ECG [7]. 

2. **Aplicación de Electromiografía (EMG)**
   
La señal EMG superficial (sEMG) contiene energía fisiológica útil principalmente en el rango de 0 a 400 Hz, dependiendo del espaciado de electrodos y el tipo de músculo. En el procesamiento de esta señal, el filtro pasa-bajos cumple un rol complementario dentro de un sistema de filtrado más amplio, actuando principalmente en el extremo de alta frecuencia del espectro para eliminar ruido eléctrico de equipos e interferencias electromagnéticas que no aportan información muscular relevante. La frecuencia de corte del filtro pasa-bajos debe situarse en el rango de 400–450 Hz, punto donde la amplitud de las componentes de ruido supera a la de la señal sEMG, siendo esta determinación siempre un compromiso entre la reducción del ruido y la preservación del contenido espectral útil de la señal [8]. 

3. **Aplicación en Electroencefalografía (EEG)**

El EEG registra actividad cerebral en un rango fisiológico que abarca desde 0.1 Hz hasta aproximadamente 50 Hz [6].  Las componentes por encima de este rango corresponden a artefactos de alta frecuencia como ruido muscular facial o cervical, interferencias de electrodos y artefactos de línea, que pueden contaminar gravemente la señal cerebral útil. El filtro pasa-bajos es una etapa estándar en el preprocesamiento de EEG para mejorar la relación señal-ruido. Se recomienda aplicar frecuencias de corte superiores a 40 Hz, preservando así componentes de alta frecuencia como el pico P1 de corta latencia. Sin embargo, su aplicación requiere cuidado en el diseño, ya que frecuencias de corte demasiado bajas pueden introducir distorsiones en la señal, como adelanto en el inicio de los componentes y reducción de amplitudes de pico [9]. 

# **Filtro Pasa Altas**
El filtro digital pasa-altos está diseñado para atenuar las componentes de frecuencia que se encuentran por debajo de un valor específico, conocido como frecuencia de corte (fc) y permitiendo el paso de las frecuencias superiores a dicho umbral. La implementación de este filtro en el procesamiento de bioseñales, como el ECG, EMG y EEG, suprime un tipo de ruido de muy baja frecuencia denominado fluctuación de la línea base o de deriva de contorno, así como los artefactos de movimiento [10].

1. **Aplicación en Electrocardiografía (ECG)**
   
Se utiliza principalmente para eliminar la deriva de la línea base, se origina por la respiración del paciente y el cambio de impedancia en el contacto electrodo-piel. Su frecuencia de corte es de 0.5 Hz, lo que permite limpiar la señal sin distorsionar el segmento ST y es vital para diagnósticos isquémicos [10].

2. **Aplicación de Electromiografía (EMG)**
   
Es utilizado para suprimir los artefactos de movimiento que son causados por el balanceo de los cables o el desplazamiento mecánico de los electrodos sobre el músculo durante la contracción, se suelen aplicar frecuencias de corte entre 10 Hz y 20 Hz, ya que la energía útil del músculo está por encima de este rango [11].

3. **Aplicación en Electroencefalografía (EEG)**

Se emplea para filtrar potenciales lentos no corticales, como los producidos por la sudoración o movimientos oculares lentos. Generalmente se configura entre 0.5 Hz y 1.5 Hz para mantener la integridad de las ondas delta del cerebro [12]. 

# **Filtro basado en Transformada Wavelet (DWT Shrinkage)**
En lugar de cortar frecuencias de tajo, Wavelet descompone la señal en distintas resoluciones. Luego, aplica un "umbral" (thresholding) para atenuar solo las partes de la señal que parecen ruido aleatorio, conservando los picos agudos naturales (como el complejo QRS del corazón o las puntas epilépticas del cerebro) intacto.
La DWT analiza la señal en tiempo y frecuencia simultáneamente. Esto permite separar el ruido de la señal útil incluso si comparten la misma banda de frecuencia. 

1. **Aplicación en Electrocardiografía (ECG)**
   
Preservación morfológica para el diagnóstico clínico preciso y detección del complejo QRS en entornos ruidosos,la técnica Wavelet descompone el ECG y aplica el shrinkage solo a los coeficientes que representan ruido aleatorio.
Entonces, logra limpiar el ruido blanco y la interferencia sin reducir la amplitud de la onda R ni alterar la duración de los intervalos PR o QT [13].

2. **Aplicación de Electromiografía (EMG)**
   
Sirve principalmente para la extracción de Potenciales de Acción de Unidad Motora (MUAPs) y control de prótesis mioeléctricas,la señal EMG de superficie (sEMG) es por naturaleza no estacionaria y estocástica (parece ruido aleatorio).Si se usa un filtro tradicional muy fuerte, destruyes la información de la fuerza muscular, pero la DWT permite aislar las "espinas" reales de la contracción muscular del ruido térmico de los amplificadores o del ruido de fondo[14].

3. **Aplicación en Electroencefalografía (EEG)**

Eliminación de artefactos oculares (parpadeos) y detección de eventos transitorios (como espigas epilépticas).
El EEG es la señal más pequeña y compleja. Un simple parpadeo (artefacto EOG) genera una onda masiva de baja frecuencia que tapa completamente las ondas cerebrales frontales. Con Wavelet, se puede descomponer el EEG, identificar exactamente los coeficientes (el nivel de resolución) donde reside la onda del parpadeo, "apagar" o umbralizar esos coeficientes específicos, y luego reconstruir la señal[15].

# **Filtro Adaptativo**
A diferencia de los filtros pasa bajas o pasa altas los cuales presentan sus umbrales fijos, este filtro ajusta sus parámetros en tiempo real. Utiliza algoritmos de optimización como Mínimos Cuadrados Medios (LMS) o Mínimos Cuadrados Recursivos (RLS), para disminuir la diferencia entre la señal contaminada y una señal de referencia del ruido. El uso principal de este tipo de filtros es para eliminar el ruido no estacionario y artefactos que comparten la misma banda de frecuencia que la señal fisiológica útil, situaciones en los que los filtros convencionales no funcionarían ya que distorsionarían también la señal original.

1. **Aplicación en Electrocardiografía (ECG)**
   
La señal ECG es susceptible a la fluctuación de la referencia y a los artefactos de movimiento como la respiración o actividad física. Estos ruidos son de baja frecuencia (0.1 Hz-0.5Hz) , se solapan en la señal ECG, y un filtro pasa altas podría distorsionar el segmento ST. El filtro actúa estimando y cancelando esta interferencia sin alterar la morfología de la señal. Esto permite garantizar la máxima precisión, para que posteriormente se puedan usar algoritmos a exactitud, como por ejemplo, el de Pan -Tompkins. Gracias a este filtro se puede calcular de manera precisa métricas temporales complejas como la frecuencia cardíaca (HRV) y el tiempo de tránsito de pulso (PTT) [16]

2. **Aplicación de Electromiografía (EMG)**
   
En el registro superficial de EMG (sEMG), específicamente al querer evaluar los músculos del tronco (como los pectorales), el principal problema radica en la contaminación de ruido por parte del corazón, conocida como interferencia de ECG o cross-talk. Dado a que ambos comparten la banda útil, los filtros clásicos no pueden separar ambas señales. El filtro adaptativo se usa en canal ECG secundario como referencia para aprender la interferencia cardíaca y restarla dinámicamente del registro EMG. Esto permite limpiar la señal sEMG conservando la totalidad de la energía fisiológica muscular, siendo fundamental para estudios de fatiga y biomecánica [17] 

3. **Aplicación en Electroencefalografía (EEG)**

El EEG registra una actividad cerebral de muy baja amplitud (uV) , lo que lo hace muy susceptible a artefactos fisiológicos, en particular los oculares (como el parpadeo y el movimiento brusco de los ojos) y musculares (movimiento de la frente y mandíbula). Un parpadeo genera una onda de baja frecuencia que puede enmascarar por completo las señales theta y alfa frontales. El filtro adaptativo se usa para la eliminación de estos artefactos oculares, ya que usa como referencia esta señal y mejora significativamente la preservación de las características transitorias del cerebro, las cuales son usadas en investigación del sueño o interfaces cerebro-computadora [18] 

</div>

<div align="justify">
  
# **Bibliografía:**

[1] “Notch Filter,” MathWorks. https://la.mathworks.com/discovery/notch-filter.html

[2] T. T. C. Choy and P. M. Leung, “Filtro muesca de 50 Hz basado en microprocesador en tiempo real para ECG,” ScienceDirect. https://www.sciencedirect.com/science/article/abs/pii/0141542588900131

[3] R. G. T. Mello, L. F. Oliveira, and J. Nadal, “Digital Butterworth filter for subtracting noise from low magnitude surface electromyogram,” Computer Methods and Programs in Biomedicine, vol. 87, no. 1, pp. 28–35, Jun. 2007, doi: 10.1016/j.cmpb.2007.04.004.

[4] R. E. García García, González Alfonso, M. Sánchez Castillo, and E. Barbará Morales, “Filtro digital adaptativo supresor de interferencias periódicas para registros de electroencefalografía,” INGENIERÍA BIOMÉDICA, 2013.(PDF) Filtro digital adaptativo supresor de interferencias periódicas para registros de electroencefalografía 

[5] R. Srinivasagan, "Advanced low-power filter architecture for biomedical signals with adaptive tuning," PLOS ONE, vol. 20, no. 1, p. e0311768, Jan. 2025. doi: 10.1371/journal.pone.0311768

[6] R. S. Khandpur, Handbook of Biomedical Instrumentation, 3rd ed. New Delhi: McGraw Hill Education, 2014, pp. 46, 469. 

[7] I. Petráš, "Novel generalized low-pass filter with adjustable parameters of exponential-type forgetting and its application to ECG signal," Sensors, vol. 22, no. 22, p. 8740, Nov. 2022. doi: 10.3390/s22228740

[8] C. J. De Luca, L. D. Gilmore, M. Kuznetsov, and S. H. Roy, "Filtering the surface EMG signal: Movement artifact and baseline noise contamination," Journal of Biomechanics, vol. 43, no. 8, pp. 1573–1579, May 2010. doi: 10.1016/j.jbiomech.2010.01.027

[9] A. Widmann, E. Schröger, and B. Maess, "Digital filter design for electrophysiological data – a practical approach," Journal of Neuroscience Methods, vol. 250, pp. 34–46, Jul. 2015. doi: 10.1016/j.jneumeth.2014.08.002

[10] E. Ahmad y A. K. Singh, "Base Line Wander, Breathing, Power Line Interference Noise Removal in ECG Signals," International Journal of Computer Applications, vol. 175, no. 29, pp. 10-15, 2020. doi: 10.5120/ijca2020920829.

[11] J. S. Kumar y P. Bhuvaneswari, "Preprocessing ECG Signal by Eliminating Various Noises Using Filter Techniques," AIP Conference Proceedings, vol. 2393, no. 1, p. 080003, 2022. doi: 10.1063/5.0076807.

[12] I. Petráš, "Novel generalized low-pass filter with adjustable parameters of exponential-type forgetting and its application to ECG signal," Sensors, vol. 22, no. 22, p. 8740, Nov. 2022. doi: 10.3390/s22228740.

[13 ]Tiwari, V., Jain, D., Sharma, D., Hassan, M. M., Althobaiti, F., Varkale, A., Al-Khasawneh, M. A., & Tirandasu, R. K. (2025). An efficient sparse code shrinkage technique for ECG denoising using empirical mode decomposition. Technology and health care : official journal of the European Society for Engineering and Medicine, 33(4), 1773–1786. 
https://doi.org/10.1177/09287329241302749 

[14] Phinyomark, A., Phukpattaranont, P., & Limsakul, C. (2011). Wavelet-based denoising algorithm for robust EMG pattern recognition. Fluctuation and Noise Letters, 10(02), 157-167.
https://www.worldscientific.com/doi/abs/10.1142/S0219477511000466

[15] Kaur, C., Singh, P., & Sahni, S. (2021). EEG Artifact Removal System for Depression Using a Hybrid Denoising Approach. Basic and clinical neuroscience, 12(4), 465–476. https://doi.org/10.32598/bcn.2021.1388.2

[16] X. An and G. K. Stylios, “Comparison of Motion Artefact Reduction Methods and the Implementation of Adaptive Motion Artefact Reduction in Wearable Electrocardiogram Monitoring,” Sensors (Basel, Switzerland), vol. 20, no. 5, Mar. 2020, doi: https://doi.org/10.3390/s20051468. 

[17] S Abbaspour and A. Fallah, “Removing ECG Artifact from the Surface EMG Signal Using Adaptive Subtraction Technique,” Journal of Biomedical Physics & Engineering, vol. 4, no. 1, p. 33, Mar. 2014, Available: https://pmc.ncbi.nlm.nih.gov/articles/PMC4258854/ 

[18] X. Jiang, G.-B. Bian, and Z. Tian, “Removal of Artifacts from EEG Signals: A Review,” Sensors (Basel, Switzerland), vol. 19, no. 5, p. 987, 2019, doi: https://doi.org/10.3390/s19050987. 


</div>
