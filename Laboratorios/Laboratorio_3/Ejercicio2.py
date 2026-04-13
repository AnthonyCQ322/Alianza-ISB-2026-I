!pip install wfdb

import wfdb

# Descargar un registro (ej: 100)
record = wfdb.rdrecord('e0103', pn_dir='edb')

# Read a WFDB anno tation file record_name.extension and return an Annotation
annotation = wfdb.rdann('e0103', 'atr', pn_dir='edb')

# Tipo: numpy array
# Forma: (N, canales)
signal = record.p_signal
fs = record.fs

import matplotlib.pyplot as plt
import numpy as np

N = signal.shape[0]
n = np.arange(N)
t = n/fs

plt.figure(figsize=(10,5))
plt.plot(t[:2000], signal[:2000,0])
plt.title("ECG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(ls=":")
plt.show()


x = signal[:,0]

plt.magnitude_spectrum(x, Fs=fs, scale='dB')

x_dc_removed = x - np.mean(x)

plt.magnitude_spectrum(x_dc_removed, Fs=fs, scale='dB')

X = np.fft.fft(x_dc_removed)
freqs = np.fft.fftfreq(len(x_dc_removed), 1/fs)

plt.plot(freqs[:len(x_dc_removed)//2], np.abs(X[:len(x_dc_removed)//2]))
plt.xlabel("Hz")
plt.ylabel("Magnitude")
plt.show()

wfdb.plot_wfdb(record=record, annotation=annotation)
