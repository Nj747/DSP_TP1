import numpy as np
import librosa as lb
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve
###############################################################################
""" Implementación Punto 6 """
###############################################################################
xR,fs = lb.load("parteReal.wav",sr=None)
 # largo de ventana = 1% de la señal
M = (len(xR)/100)

blackman = 0.42 - 0.5 * np.cos(2*np.pi*np.arange(0,M,1) /(M-1)) + 0.08 * np.cos(4*np.pi*np.arange(0,M,1) /(M-1)) 

y = fftconvolve(xR,blackman,'full') 
n = np.arange(0,len(y))

# Normalizacion
xmax = np.max(y)
y = y/xmax
###############################################################################
""" Ploteo de señales """
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,1,1)
plt.plot(n[100:300],xR[100:300], color = "blue")
plt.xlabel("Muestras")
plt.ylabel("Amplitud Normalizada")
plt.title("Señal original")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(n[100:300],y[100:300], color = "red")
plt.title("Señal Filtrada")
plt.xlabel("Muestras")
plt.ylabel("Amplitud Normalizada")
plt.grid(True)
plt.show()
""" Leer:
Como dicha señal tiene componentes de alta frecuencia, para el ventaneo con la 
blackman de 882 muestras, al convolucionar funciona como un filtro pasa bajos, 
por lo que hay una "destrucción" de la señal original. Para una mejor 
visualización deberían utilizarse valores de 5 o 10 inclusive para M. 
"""