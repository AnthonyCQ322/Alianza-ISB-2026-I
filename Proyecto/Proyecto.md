# Equipo 4:
## Integrantes
- Mishelle Llanos Guerrero
- Eliane Jhilary Borda Velasquez
- Luis Alejandro Luque Prado
- Sebastian Fabrizio Sulca Garay
- Anthony Frank Callupe Quispe

## 1. Introducción 
Las enfermedades cardiovasculares son la causa más frecuente de defunciones en el mundo. Según la Organización Mundial de la Salud (OMS), son responsables de 19,8 millones de muertes anuales. Las más frecuentes son las cardiopatías coronarias y los accidentes cerebrovasculares; además,  una tercera parte de ellas son prematuras, es decir, ocurren en personas menores de 70 años [1].

En el contexto peruano, las enfermedades cardiovasculares son la primera causa de muerte en el Perú y producen la mayor carga de enfermedad en el país [2] . El estudio: “Tendencias en la epidemiología del infarto agudo de miocardio en el Perú”, realizado entre 2018 y 2023, registró 28 088 eventos de infarto agudo de miocardio (IAM), con un incremento en la tasa nacional estandarizada por edad [3], lo que demuestra su alta prevalencia e importancia  en el país.

El electrocardiograma (ECG) es la principal prueba para detectar problemas cardiovasculares. Este registro de la actividad eléctrica del corazón se representa gráficamente mediante un trazado, donde se observan diferentes ondas que corresponden a los estímulos eléctricos de las aurículas y los ventrículos. Para su registro, se colocan electrodos sobre la piel del paciente (normalmente 10), conectados al electrocardiógrafo y se obtienen 12 derivaciones [4].
El segmento ST es la porción del ECG que conecta el final del complejo QRS con el inicio de la onda T [5]. En condiciones normales es isoeléctrico o plano, con variaciones menores de 0,5 mm. Su análisis permite identificar cardiopatía isquémica o infarto agudo de miocardio (IAM), siendo  la elevación aguda del segmento ST uno de los signos más tempranos del IAM y generalmente relacionada con la oclusión completa de una arteria coronaria [ 6 ].

## 2. Problemática a abordar
A pesar de que el análisis del segmento ST es el indicador importante, su detección automática en sistemas de monitorización continua presenta limitaciones importantes en la práctica clínica.  En entornos hospitalarios como unidades de cuidados intensivos, salas de hospitalización o servicios de emergencia, los monitores cardiacos registran al ECG de manera continua utilizando números reducidos de derivaciones (de 3 a 6 electrodos), a diferencia del ECG diagnóstico de 12 derivaciones [7]. Esta configuración simplificada permite la monitorización prolongada del paciente, pero produce mayores desafíos para la interpretación automatizada de la señal.

Uno de los principales problemas asociados a estos sistemas es la alta frecuencia de alarmas falsas generadas por los monitores de ECG. Este fenómeno es conocido como fatiga por alarmas que ocurre cuando el personal de salud se ve expuesto a un gran número de alertas que no corresponden a eventos clínicamente relevantes. Como consecuencia, se produce una sobrecarga sensorial, tensión emocional y una desensibilización gradual o una menor capacidad de respuesta entre los profesionales de la salud, lo que aumenta el riesgo de respuestas tardías o inadecuadas a las alarmas y compromete la seguridad del paciente [8].

Estadísticamente entre el 80% y el 99% de las alarmas de monitores ECG son falsas o clínicamente insignificantes [9]. La fatiga por alarmas ha sido documentada como responsable de más de 650 muertes hospitalarias, cifra probablemente subestimada por subregistro, y el 90% de las alarmas por arritmias falsas [10].  Esta situación se debe en gran medida a limitaciones en los algoritmos de detección utilizados en los sistemas de monitorización actuales.

Los algoritmos convencionales de detección del ST activan alarmas por cambios muy breves en la señal, originados por el movimiento del paciente, el cambio postural o la respiración, debido a que no incorporan criterios clínicos como duración mínima del episodio, umbral de la señal, ni confirmación en derivaciones contiguas [11].  Esto demuestra que la configuración del algoritmo impacta directamente en el ámbito clínico.

En ese entender, se identifica la necesidad de desarrollar algoritmos de procesamiento de señales que, utilizando un número limitado de derivaciones del ECG, permitan detectar episodios de elevación del segmento ST con mayor especificidad que los sistemas convencionales empleados en entornos hospitalarios. 
