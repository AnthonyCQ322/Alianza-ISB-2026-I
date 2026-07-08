@'
# Señales de ejemplo

Registros para probar la aplicación sin necesidad de datos externos.

## PhysioNet (base PTB)
- `s0036lre.hea` + `s0036lre.dat`: paciente con infarto de miocardio
  anterior (caso PATOLOGICO). Se sube el par .hea + .dat en la seccion
  Clasificacion, formato PhysioNet.

## BITalino
- `Senal_1.txt`, `Senal_2.txt`, `Senal_3.txt`: derivaciones I, II y III
  capturadas con hardware BITalino. Se suben en el formato BITalino
  (una por casilla).
'@ | Set-Content -Path "data\samples\README.md" -Encoding UTF8