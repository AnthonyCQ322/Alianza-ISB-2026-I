import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# valores de la señal
Aa = 5
Ab = 7
Ac = 11
fa = 100
fb = 300
fc = 66           #  hz
wa = 2*np.pi*fa     #  rad/s
wb = 2*np.pi*fb     #  rad/s
wc = 2*np.pi*fc     #  rad/s
phia = 0
phib = 15
phic = 55
fs = 10*f
Ts = 1/fs

n = np.arange(1000)
t = n*Ts

# señal senoidas
xa = Aa*np.sin(wa*t + phia)
xb = Ab*np.sin(wb*t + phib)
xc = Ac*np.sin(wc*t + phic)
xtotal = xa + xb + xc


plt.plot(t, xtotal)
plt.xlim(0,0.1)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.stem(n, xtotal)
#plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Senoidal')
plt.xlim(0,100)

plt.magnitude_spectrum(xtotal, Fs=fs, scale='dB')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud (dB)')
plt.grid(ls=":")
