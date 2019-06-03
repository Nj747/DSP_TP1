import scipy as sp
import librosa as lb
import matplotlib.pyplot as plt
import numpy as np
###############################################################################
""" Funciones """
###############################################################################
def GenerarWavLibrosa(fs,data,filename):
    lb.output.write_wav(filename + '.wav', data, fs)
###############################################################################
def ConvolucionCircular(f,g):
    # condicion para igualar convolucion lineal con circular
    fog = len(f) + len(g) - 1 
    cerosX = fog - len(f)
    cerosY = fog - len(g)
    # agregando ceros
    f = np.array(sp.append(f,sp.zeros(cerosX)))
    g = np.array(sp.append(g,sp.zeros(cerosY)))
    return np.real(sp.ifft(sp.fft(f) * sp.fft(g)))
###############################################################################
# ConvolucionCircularRespImp 
# calcula la conv circular con el largo de la respuesta al impulso
###############################################################################
def ConvolucionCircularRespImp(f,g):
    return np.real(sp.ifft(sp.fft(f[len(g)]) * sp.fft(g)))
###############################################################################
""" Implementación Punto 8 """
###############################################################################
# Variables
# xR ----------> señal generada en el punto 1
# fsRI --------> frecuencia de muestreo xR
# lineal ------> resultado de la convolucion lineal entre xR y respImp
# circular ----> resultado de la convolucion circular entre xR y respImp
# lrespImp ----> resultado de la convolucion circular entre xR y respImp con 
# -------------- señal (xR) igual al largo de respImp
###############################################################################
xR,fsR = lb.load("parteReal.wav", sr=None)
respImp, fsRI = lb.load("resp_imp.wav",sr=None)

lineal = sp.convolve(xR,respImp)
circular = ConvolucionCircular(xR,respImp)
lrespImp = ConvolucionCircularRespImp(xR,respImp)

n = np.arange(0,len(respImp),1)
###############################################################################
""" Ploteo de señales """
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.4, wspace = 0.5)

plt.subplot(3,2,1)
plt.plot(n[100:400],xR[100:400],color = "blue")
plt.title("Señal original")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,2,2)
plt.plot(n[100:400],respImp[100:400], color = "red")
plt.title("Resepuesta al impulso")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,2,3)
plt.plot(n[100:400],lineal[100:400], color = "green")
plt.title("Resultado Convolución Lineal")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,2,4)
plt.plot(n[100:400],circular[100:400], color = "black")
plt.title("Resultado Convolución Circular")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,2,5)
plt.plot(n[100:400],lrespImp[100:400], color="orange")
plt.title("Resultado Convolución Circular con largo igual a la RespImp")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.show()

###############################################################################
""" Generar wavs de convoluciones """
###############################################################################
fsConv = len(lineal)
GenerarWavLibrosa(fsConv,lineal,"convLineal")
GenerarWavLibrosa(fsConv,circular,"convCircular")