><p align="center"> # INTRODUCCIÓN A SEÑALES BIOMÉDICAS </p>
><p align="center"> Universidad Peruana Cayetano Heredia </p>


><p align="center"> <img src=https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Screenshot_2026-04-05-19-02-39-53_a1b1bbe5f63d5b96c1a0f87c197ebfae.jpg width="30%"> </p>

# Equipo 4:
## Integrantes
- Mishelle Llanos Guerrero
- Eliane Jhilary Borda Velasquez
- Luis Alejandro Luque Prado
- Sebastian Fabrizio Sulca Garay
- Anthony Frank Callupe Quispe

## 1. Introducción 
<div align="justify"> Las enfermedades cardiovasculares son la causa más frecuente de defunciones en el mundo. Según la Organización Mundial de la Salud (OMS), son responsables de 19,8 millones de muertes anuales. Las más frecuentes son las cardiopatías coronarias y los accidentes cerebrovasculares; además,  una tercera parte de ellas son prematuras, es decir, ocurren en personas menores de 70 años [1].

En el contexto peruano, las enfermedades cardiovasculares son la primera causa de muerte en el Perú y producen la mayor carga de enfermedad en el país [2] . El estudio: “Tendencias en la epidemiología del infarto agudo de miocardio en el Perú”, realizado entre 2018 y 2023, registró 28 088 eventos de infarto agudo de miocardio (IAM), con un incremento en la tasa nacional estandarizada por edad [3], lo que demuestra su alta prevalencia e importancia  en el país.

El electrocardiograma (ECG) es la principal prueba para detectar problemas cardiovasculares. Este registro de la actividad eléctrica del corazón se representa gráficamente mediante un trazado, donde se observan diferentes ondas que corresponden a los estímulos eléctricos de las aurículas y los ventrículos. Para su registro, se colocan electrodos sobre la piel del paciente (normalmente 10), conectados al electrocardiógrafo y se obtienen 12 derivaciones [4].
El segmento ST es la porción del ECG que conecta el final del complejo QRS con el inicio de la onda T [5]. En condiciones normales es isoeléctrico o plano, con variaciones menores de 0,5 mm. Su análisis permite identificar cardiopatía isquémica o infarto agudo de miocardio (IAM), siendo  la elevación aguda del segmento ST uno de los signos más tempranos del IAM y generalmente relacionada con la oclusión completa de una arteria coronaria [ 6 ]. </div>


><p align="center"> <img src=https://github.com/AnthonyCQ322/Alianza-ISB-2026-I/blob/main/Imagenes/Screenshot_2026-04-05-19-02-39-53_a1b1bbe5f63d5b96c1a0f87c197ebfae.jpg width="30%"> </p>
><p align="center"> Figura 1. Electrocardiograma con elevación del segmento T [6] </p>

## 2. Problemática a abordar
<div align="justify"> A pesar de que el análisis del segmento ST es el indicador importante, su detección automática en sistemas de monitorización continua presenta limitaciones importantes en la práctica clínica.  En entornos hospitalarios como unidades de cuidados intensivos, salas de hospitalización o servicios de emergencia, los monitores cardiacos registran al ECG de manera continua utilizando números reducidos de derivaciones (de 3 a 6 electrodos), a diferencia del ECG diagnóstico de 12 derivaciones [7]. Esta configuración simplificada permite la monitorización prolongada del paciente, pero produce mayores desafíos para la interpretación automatizada de la señal.

Uno de los principales problemas asociados a estos sistemas es la alta frecuencia de alarmas falsas generadas por los monitores de ECG. Este fenómeno es conocido como fatiga por alarmas que ocurre cuando el personal de salud se ve expuesto a un gran número de alertas que no corresponden a eventos clínicamente relevantes. Como consecuencia, se produce una sobrecarga sensorial, tensión emocional y una desensibilización gradual o una menor capacidad de respuesta entre los profesionales de la salud, lo que aumenta el riesgo de respuestas tardías o inadecuadas a las alarmas y compromete la seguridad del paciente [8].

Estadísticamente entre el 80% y el 99% de las alarmas de monitores ECG son falsas o clínicamente insignificantes [9]. La fatiga por alarmas ha sido documentada como responsable de más de 650 muertes hospitalarias, cifra probablemente subestimada por subregistro, y el 90% de las alarmas por arritmias falsas [10].  Esta situación se debe en gran medida a limitaciones en los algoritmos de detección utilizados en los sistemas de monitorización actuales.

Los algoritmos convencionales de detección del ST activan alarmas por cambios muy breves en la señal, originados por el movimiento del paciente, el cambio postural o la respiración, debido a que no incorporan criterios clínicos como duración mínima del episodio, umbral de la señal, ni confirmación en derivaciones contiguas [11].  Esto demuestra que la configuración del algoritmo impacta directamente en el ámbito clínico.

En ese entender, se identifica la necesidad de desarrollar algoritmos de procesamiento de señales que, utilizando un número limitado de derivaciones del ECG, permitan detectar episodios de elevación del segmento ST con mayor especificidad que los sistemas convencionales empleados en entornos hospitalarios. </div>

## 3. Propuesta de Solución
<div align="justify"> La propuesta de solución consiste en el desarrollo de un sistema de monitoreo basado	 en deep learning , diseñado para filtrar las fluctuaciones que causan las fatigas por alarma. El sistema tendría que eliminar la deriva de línea base, causado por la respiración, sin distorsionar la morfología del segmento ST,además de filtrar el ruido muscular. Presentaría un algoritmo que mediría el punto J de manera precisa, y una evaluación mediante IA para confirmar si se trata de un patrón de IAM. Si se trata de ello, emitirá una alarma sonora la cuál indicaría una emergencia
.Nos fijamos en que el diseño funcione con un numero reducido de derivaciones (ECG de 3 a 6 electrodos) ya que permitira que no sea solo usado en cuidados intensivos sino tambien en servicios de emergencia y salas de hospitalización donde la monitorización continua es vital.
  
</div>

## 4. Plan de Actividades
| Semana | Duración (h) | Actividad | Estado |
| :---: | :---: | :--- | :---: |
| 1 | 6 | 🔍 Comprensión, búsqueda de problemática y creación del repositorio | ✅ Completo |
| 2 | 6 | 💡 Posibles propuestas y elección del proyecto | ✅ Completo |
| 3 | 4 | 📅 Plan de trabajo | ⏳ En proceso |
| 4 | 2 | 📚 Estado del arte | 🟦 Pendiente |
| 5 | 4 | 🎤 Entrega y sustentación del 1er avance (Retroalimentación) | 🟦 Pendiente |
| 6 | 6 | 🛠️ Matriz morfológica y conceptos de solución | 🟦 Pendiente |
| 7 | 4 | 💻 Prototipado electrónico y revisión de PCB con profesores | 🟦 Pendiente |
| 8 | 2 | 📦 Petición de la PCB y recursos necesarios | 🟦 Pendiente |
| 9 | 2 | 🎤 Entrega y sustentación del 2do avance (Retroalimentación) | 🟦 Pendiente |
| 10 | 8 | 📝 Examen parcial | 🟦 Pendiente |
| 11 | 6 | 🤖 Programación y aplicación en Machine Learning | 🟦 Pendiente |
| 12 | 6 | 🔨 Construcción y calibración del prototipo funcional | 🟦 Pendiente |
| 13 | 8 | 🧪 Pruebas del prototipo | 🟦 Pendiente |
| 14 | 8 | ⚙️ Validación y corrección de prototipo funcional | 🟦 Pendiente |
| 15 | 2 | 📄 Avance del artículo académico y póster | 🟦 Pendiente |
| 16 | 2 | 🎤 Entrega y sustentación del 3er avance (Retroalimentación) | 🟦 Pendiente |
| **Final** | - | 🏆 Presentación Final y póster | 🟦 Pendiente |


## 5. Referencias
<div align="justify">
[1] World Health Organization: WHO, “Enfermedades cardiovasculares,” Jun. 11, 2019. https://www.who.int/es/health-topics/cardiovascular-diseases#tab=tab_1

[2] “Enfermedades cardiovasculares son la primera causa de muerte en nuestro país,” Noticias - Ministerio De Salud - Plataforma Del Estado Peruano. https://www.gob.pe/institucion/minsa/noticias/1030798-enfermedades-cardiovasculares-son-la-primera-causa-de-muerte-en-nuestro-pais

[3] A. Hernández-Vásquez, R. Vargas-Fernández, and M. Chacón-Díaz, “Tendencias en la epidemiología del infarto agudo de miocardio en el Perú: un análisis de los registros oficiales de SUSALUD,” Archivos Peruanos De Cardiología Y Cirugía Cardiovascular, vol. 5, no. 4, pp. 187–197, Nov. 2024,  https://doi.org/10.47487/apcyccv.v5i4.435

[4] M. Rodríguez, “Electrocardiograma,” Fundación Española Del Corazón. https://fundaciondelcorazon.com/informacion-para-pacientes/metodos-diagnosticos/electrocardiograma.html

[5] H. Parrales MD, “Segmento ST,” Cerebromedico, Dec. 16, 2018. https://cerebromedico.com/electrocardiograma/segmento-st/

[6] “Valoración del Segmento ST.” https://www.my-ekg.com/como-leer-ekg/segmento-st.php

[7] M. S. Holm et al., “The patient experience of in-hospital telemetry monitoring: a qualitative analysis,” European Journal of Cardiovascular Nursing, vol. 23, no. 3, pp. 258–266, Aug. 2023, doi: 10.1093/eurjcn/zvad082.

[8] E. A. M. Michels, S. Gilbert, I. Koval, and M. K. Wekenborg, “Alarm fatigue in healthcare: a scoping review of definitions, influencing factors, and mitigation strategies,” BMC Nursing, vol. 24, no. 1, p. 664, Jun. 2025, doi: 10.1186/s12912-025-03369-2.

[9] S. Jacques and E. Williams, “Reducing the safety hazards of monitor alert and alarm fatigue,” PSNet, May 01, 2016. https://psnet.ahrq.gov/perspective/reducing-safety-hazards-monitor-alert-and-alarm-fatigue

[10] M. M. Pelter, D. Mortara, and F. Badilini, “Computer Assisted Patient monitoring: associated patient, clinical and ECG characteristics and strategy to minimize false alarms,” Hearts, vol. 2, no. 4, pp. 459–471, Oct. 2021, doi: 10.3390/hearts2040036.

[11] M. M. Pelter, Y. Xu, R. Fidler, R. Xiao, D. W. Mortara, and H. Xiao, “Evaluation of ECG algorithms designed to improve detect of transient myocardial ischemia to minimize false alarms in patients with suspected acute coronary syndrome,” Journal of Electrocardiology, vol. 51, no. 2, pp. 288–295, Oct. 2017, doi: 10.1016/j.jelectrocard.2017.10.005
</div>

