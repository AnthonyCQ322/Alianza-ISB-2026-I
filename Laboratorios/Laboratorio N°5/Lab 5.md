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
1. **Limpieza de Piel y Ubicación de electrodos** <br>Delimitamos la ubicación necesaria para los tres electrodos (dos cerca a la clavícula y uno en la cresta ilíaca izquierda). Luego se limpia el área de colocación de los electrodos para hacer uso junto al BITalino para las mediciones después de las actividades físicas. Con el software OpenSignals (r)evolution, se inició el proceso de grabación de datos.

[FOTO LIMPIANDO*[)
Imágen 1: Materiales de limpieza con el brazo sin electrodos

2. **Conexión del equipo y Primera medición**<br> Se conectó el sensor de ECG al canal analógico de la placa BITalino. Posteriormente, se realiza la medida del ECG en reposo así que se colocaron los 3 conectores de los electrodos a sus electrodos (IN+, IN- y REF) según corresponda para cada medida de derivada (I, II, III) .
Derivación I:
Cable Negativo (IN-): Se coloca en la Clavícula Derecha.
Cable Positivo (IN+): Se coloca en la Clavícula Izquierda.
Referencia (REF): Se coloca en la Cresta Ilíaca Izquierda.
	Derivación II:
Cable Negativo (IN-): Se coloca en la Clavícula Derecha.
Cable Positivo (IN+): Se coloca en la Cresta Ilíaca Izquierda.
Referencia (REF): Se coloca en la Clavícula Izquierda.
	Derivación III:
Cable Negativo (IN-): Se coloca en la Clavícula Izquierda.
Cable Positivo (IN+): Se coloca en la Cresta Ilíaca Izquierda.
Referencia (REF): Se coloca en la Clavícula Derecha.

[FOTO COLOCANDO*[)
Imágen 2: Medición de la señal ECG en posición de reposo
[VIDEO MAYBE]

3. **Tomas de movimiento con el ECG** <br> El usuario realiza secuencialmente una serie de actividades y al finalizar su actividad se mide inmediatamente con los electrodos para cada derivación I, II y III.
Se repitió 3 veces un ciclo de respiración: Inhalación - retener la respiración - exhalación - retener la respiración.
El usuario realizó un esfuerzo físico intenso 2 minutos de burpees para observar los cambios en la frecuencia cardíaca después del ejercicio.
[vido burpee]

Video : Grabación de la señal ECG registrando el aumento de la frecuencia cardíaca tras el ejercicio.
Inhalación larga y profunda seguida de la máxima retención de la respiración que pueda el usuario.
[vido hipoventialcion]
Video : Grabación de la señal ECG registrando el aumento de la frecuencia cardíaca tras el ejercicio.

4. **Última medición del sensor de ECG** <br> El usuario descansa por 2 minutos luego de las actividades físicas y posteriormente se le vuelve a realizar mediciones mientras está en reposo para las 3 derivaciones (i, II, III).
[vido o imagen segundo descanso]
imágen XX : Medición de la señal ECG en la fase de recuperación del usuario.
Análisis y Procesamiento Digital: Tras finalizar el protocolo, se detuvo la grabación y se guardaron los datos y con ayuda de la programación empleando la librería opensignalsreader podemos graficar la señal ECG en el dominio del tiempo y aplicar la Transformada Rápida de Fourier (FFT) para su análisis en frecuencia




## 5. Resultados
5.1.1. Señal basal en 1era derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/0.png" width="70%">	
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/1.jpg" width="70%">
</p> 
<p align="center">	  
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/2.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/3.jpg" width="70%">
</p> 
<p align="center">	  
Figura 4. Frecuencia cardiaca instantánea (basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/4.jpg" width="70%">
</p> 
<p align="center">	  
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (basal, derivación I).
</p> 

5.1.2. Señal basal en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/5.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/6.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/7.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/8.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/9.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (basal, derivación II).
</p> 

5.1.3. Señal basal en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/10.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/11.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/12.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/13.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/14.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (basal, derivación III).
</p> 

5.2.1.1. Primera Hiperventilación en 1ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/15.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Primera hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/16.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Primera hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/17.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Primera hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/18.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Primera hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/19.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Primera hiperventilación, derivación I).
</p> 

5.2.1.2. Primera Hiperventilación en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/20.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Primera hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/21.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Primera hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/22.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Primera hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/23.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Primera hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/24.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Primera hiperventilación, derivación II).
</p> 

5.2.1.3. Primera Hiperventilación en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/25.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Primera hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/26.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Primera hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/27.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Primera hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/28.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Primera hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/29.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Primera hiperventilación, derivación III).
</p> 

5.2.2.1. Segunda Hiperventilación en 1ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/30.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/31.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/32.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/33.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda hiperventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/34.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda hiperventilación, derivación I)..
</p> 

5.2.2.2. Segunda Hiperventilación en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/35.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/36.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/37.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/38.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda hiperventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/39.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda hiperventilación, derivación II).
</p> 


5.2.2.3. Segunda Hiperventilación en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/40.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/41.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/42.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/43.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda hiperventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/44.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda hiperventilación, derivación III).
</p> 

5.3.1. Segunda Señal basal en 1ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/45.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda Señal basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/46.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda Señal basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/47.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda Señal basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/48.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda Señal basal, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/49.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda Señal basal, derivación I).
</p> 

5.3.2. Segunda Señal basal en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/50.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda Señal basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/51.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda Señal basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/52.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda Señal basal, derivación II.
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/53.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda Señal basal, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/54.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda Señal basal, derivación II).
</p> 

5.3.3. Segunda Señal basal en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/55.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Segunda Señal basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/56.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Segunda Señal basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/57.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Segunda Señal basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/58.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Segunda Señal basal, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/59.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Segunda Señal basal, derivación III).
</p> 

5.4.1. Burpee en 1ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/60.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (burpee, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/61.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (burpee, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/62.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (burpee, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/63.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (burpee, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/64.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (burpee, derivación I).
</p> 

5.4.2. Burpee en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/65.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (burpee, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/66.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (burpee, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/67.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (burpee, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/68.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (burpee, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/69.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (burpee, derivación II).
</p> 

5.4.3. Burpee en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/70.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (burpee, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/71.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (burpee, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/72.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (burpee, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/73.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (burpee, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/74.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (burpee, derivación III).
</p> 

5.5.1. Hipoventilación en 1ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/75.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Hipoventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/76.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Hipoventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/77.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Hipoventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/78.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Hipoventilación, derivación I).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/79.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Hipoventilación, derivación I).
</p> 

5.5.2. Hipoventilación en 2da derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/80.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Hipoventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/81.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Hipoventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/82.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Hipoventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/83.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Hipoventilación, derivación II).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/84.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Hipoventilación, derivación II).
</p> 

5.5.3. Hipoventilación en 3ra derivación
<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/85.jpg" width="70%">
</p> 
<p align="center">	
Figura 1. Comparativa de la señal ECG: cruda vs. filtrada (Hipoventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/86.jpg" width="70%">
</p> 
<p align="center">	
Figura 2. Segmento de 5 segundos (20‑25 s) de la señal filtrada (Hipoventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/87.jpg" width="70%">
</p> 
<p align="center">	
Figura 3. Detección de picos R sobre la señal filtrada (puntos rojos) (Hipoventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/88.jpg" width="70%">
</p> 
<p align="center">	
Figura 4. Frecuencia cardiaca instantánea (Hipoventilación, derivación III).
</p> 

<p align="center">	
  <img src="https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Imágenes%20Laboratorio%20N°5/89.jpg" width="70%">
</p> 
<p align="center">	
Tabla 1. Métricas de variabilidad de la frecuencia cardíaca (señal completa) (Hipoventilación, derivación III).
</p> 





## 6. Discusión

### 6.1. Análisis de Resultados:
- Primera basal: Con esta etapa nosotros definimos nuestro punto de referencia para luego compararlas con los demás ejercicios. Se muestra una frecuencia cardiaca (HR) esperada , alrededor de 83.9 y 106 lpm lo que indica un funcionamiento relajado donde predomina el sistema parasimpático.
- Primera hiperventilación: La frecuencia cardiaca media  aumenta hasta 112 lpm y la variabilidad disminuye bruscamente en la derivación II. Esto sucede porque la respiración profunda expulsa demasiado CO2 de la sangre. Este desbalance alerta al sistema nervioso simpático, acelerando el corazón.
- Segunda hiperventilación: La HR media aumenta hasta los 116.4 lpm debido al estrés respiratorio que se intensifica debido al esfuerzo acumulado. El cuerpo sigue bajo el estímulo de la hipocapnia, obligando al sistema simpático a mantener el control para compensar esta alteración,volviendo los latidos más rápidos
- Segunda basal: A pesar de que en esta fase nuestro compañero esta en reposo, sus valores no regresan a la línea base inicial. El HR media se mantiene alto (hasta los 113.5 lpm). Esto nos indica que no se recuperó totalmente, por lo cuál el sistema simpático sigue mandando y nos indica que necesita aún más tiempo para que vuelva a su estado basal
- Burpees: Se observa el cambio más drástico del experimento ya que el HR medio se dispara a 162.5 lpm y la variabilidad cae de manera súbita (pNN50 entre 0 y 4.9%). Este enorme carga física hace que la actividad parasimpática sea nula y en cambio una activación simpática en su máximo límite para aumentar el gasto cardíaco y compensar la enorme demanda de oxígeno por parte de los músculos 
- Hipoventilación: Finalmente en este último experimento se nota que nuevamente hay un estado de estrés cardíaco ya que hay una HR elevada y una baja variabilidad. Al retener la respiración de forma repetida, se acumula una fuerte acumulación de CO2(hipercapnia) y un déficit de oxígeno en la sangre. Esta alteración hace que se active el sistema simpático. Como las muestras se realizaron ni bien terminó el ejercicio,se vio como el corazón se esforzó en compensarlo, este bombea de manera rápida para oxigenar nuevamente los tejidos lo más pronto posible tras la apnea

### 6.2. Limitaciones
- Artefactos de Movimiento y adherencia: Al utilizar electrodos de superficie de
Ag/AgCl, la señal es altamente susceptible a los cambios en la impedancia de la
interfaz piel-electrodo. 
Durante las pruebas de esfuerzo físico ,la generación de sudor provocaron pérdidas
temporales de adherencia, lo que se traduce en variaciones de amplitud y ruido en la
señal cruda.


- Ruido Electromiográfico : Debido a la cercanía de los electrodos a los músculos
del torso y las extremidades, la actividad de contracción muscular se superpone a la
señal cardíaca, especialmente visible como un ruido de alta frecuencia en los
espectros de las fases post-ejercicio.
También destaca PLI como ruido generado por artefactos electrodomésticos



- Influencia de la respiración en el ECG:
La respiración afecta al ECG principalmente de dos formas. 
En primer lugar, genera la desviación de la línea base (Baseline Wander). A medida
que los pulmones se llenan y vacían de aire, el volumen torácico cambia, alterando
la impedancia eléctrica entre los electrodos y moviendo físicamente el corazón en
relación con la posición de los sensores. Esto se observa en los resultados crudos
como una oscilación lenta de baja frecuencia sobre la cual "monta" el complejo QRS. 
En segundo lugar, produce un fenómeno fisiológico conocido como Arritmia Sinusal
Respiratoria (RSA). Durante la inhalación, el tono vagal disminuye y la frecuencia
cardíaca aumenta de forma natural; durante la exhalación, el tono vagal se restaura
y la frecuencia cardíaca disminuye.


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

