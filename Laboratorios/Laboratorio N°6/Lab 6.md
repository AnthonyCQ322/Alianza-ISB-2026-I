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
  
#- **Filtro Notch**
Los filtros digitales notch, son componentes esenciales en el procesamiento de bioseñales, diseñados para suprimir frecuencias de interferencia específicas, generalmente provenientes de la red eléctrica (50 o 60 Hz), es un tipo de filtro rechazabanda fabricado a partir de una combinación de filtros pasa altos y pasa bajos, también se denominan "filtros de rechazo de banda" [1].

<div  align="center">
  <h1><b>IMAGEN</b></h1>
</div>

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

# **Filtro Pasa Altas**

# **Filtro basado en Transformada Wavelet (DWT Shrinkage)**

# **Filtro Adaptativo**

</div>

<div align="justify">
  
**Bibliografía:**
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
