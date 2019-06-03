import librosa as lb
import numpy as np
import matplotlib.pyplot as plt
###############################################################################
" Función: Media Movil convolucionada "
###############################################################################
def mediamovilconv(x,M):
    r = np.ones(M)/(M) # Ventana rectangular
    y2 = np.convolve(x,r) # Convolucion
    return y2
###############################################################################
""" Implementación Punto 6 """
###############################################################################
# lb.load -> importa la señal generada en el punto 1
xR,fs = lb.load("parteReal.wav",sr=None)

# M -> largo de ventana = 1% de la señal
M = int(len(xR)/100) 

n = np.arange(0,len(xR),1)
xfconv = mediamovilconv(xR,M)
###############################################################################
""" Ploteo de señales """
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,1,1)
plt.plot(n[100:400],xR[100:400], color = "red")
plt.title("Señal original")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(n[100:400],xfconv[100:400])
plt.title("Media móvil convolucionada")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()
""" Leer:
Como dicha señal tiene componentes de alta frecuencia, para el ventaneo con la 
rectangular de 882 muestras, al convolucionar funciona como un filtro pasa bajos, 
por lo que hay una "destrucción" de la señal original. Para una mejor 
visualización deberían utilizarse valores de 5 o 10 inclusive para M. 
"""