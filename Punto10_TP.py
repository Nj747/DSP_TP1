import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
###############################################################################
""" Implementación Punto 10 """
###############################################################################
M = 1000
blackman = 0.42 - 0.5 * np.cos(2*np.pi * np.arange(0,M,1) / (M-1)) + 0.08 * np.cos(4*np.pi * np.arange(0,M,1)/(M-1)) 

 # Ventana rectangular
rectangular = np.ones(M)
n = np.arange(0,M,1)

blackman_fft = sp.fft(blackman)
rect_fft = sp.fft(rectangular)

rect_abs = np.abs(rect_fft)

mask = rect_abs>0 

###############################################################################
""" Ploteo de Señales"""
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.5, wspace = 0.5)

plt.subplot(2,2,1)
plt.plot(n,blackman)
plt.ylabel("Magnitud")
plt.title("Blackman")
plt.xlabel("Muestras")
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(n,rectangular)
plt.ylabel("Magnitud")
plt.title("Rectangular")
plt.xlabel("Muestras")
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(n,np.abs(np.log10(blackman_fft)))
plt.ylabel("Magnitud [dB]")
plt.title("fft(Blackman)")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(n[mask],np.abs(np.log10(rect_abs[mask])))
plt.ylabel("Magnitud [dB]")
plt.title("fft(Rectangular)")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)