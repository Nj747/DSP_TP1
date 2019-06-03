import numpy as np
import librosa as lb 
import matplotlib.pyplot as plt
###############################################################################
""" Funciones """
###############################################################################
# Variables
# filename -> nombre del archivo a guardar
# data -----> la señal en sí misma
# fs -------> frecuencia de muestreo
###############################################################################
def GenerarWavLibrosa(fs,data,filename):
    lb.output.write_wav(filename + '.wav', data, fs)
###############################################################################
# Variables
# r ---------------> señal + ruido
# desvioRuido -----> desvio del ruido que se suma con la señal
###############################################################################
def Relsnr(r,desvioRuido):
    snr = np.max(r)/np.std(desvioRuido)
    return snr
###############################################################################
""" Implementación Punto 3 """
###############################################################################
# lb.load -> para importar wav generado en el punto 1
xR,fs = lb.load("parteReal.wav",sr = None)

n = np.arange(1,2,1/fs)
###############################################################################
# Generación de ruido normalizado
###############################################################################
# Variables
# Ruidos generados por librería numpy ----> ruido01, ruido10, ruido30
# Sumas de señales + ruidos normalizados -> xRs01, xRs10, xRs30
# Desvíos de cada ruido generado ---------> des01,des10, des30
###############################################################################
ruido01 = np.random.normal(0,0.1,88200)
des01 = 0.1
ruido10 = np.random.normal(0,1,88200)
des10 = 1
ruido30 = np.random.normal(0,3,88200)
des30 = 3

xRs01 = xR + ruido01 
xRs10 = xR + ruido10
xRs30 = xR + ruido30
###############################################################################
""" Ploteo de señales """
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=1)

plt.subplot(3,1,1)
plt.plot(n[100:400],xRs01[100:400],color = "blue")
plt.title("Señal + Ruido 1")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,1,2)
plt.plot(n[100:400],xRs10[100:400], color = "red")
plt.title("Señal + Ruido 2")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(3,1,3)
plt.plot(n[100:400],xRs30[100:400], color = "green")
plt.title("Señal + Ruido 3")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()
###############################################################################
""" Generar wavs de señales + ruidos """
###############################################################################
#GenerarWavLibrosa(fs,xRs01,"xRs01")
#GenerarWavLibrosa(fs,xRs10,"xRs10")
#GenerarWavLibrosa(fs,xRs30,"xRs30")
###############################################################################
""" Calculo de relacion señal ruido (snr)"""
###############################################################################
snrRs01 = Relsnr(xRs01,des01)
snrRs10 = Relsnr(xRs10,des10)
snrRs30 = Relsnr(xRs30,des30)
###############################################################################
# para mostrar por consola los distintos resultados descomentar lo siguiente:
print("Relación Señal + Ruido con desvío 0.1")
print (snrRs01)
print("Relación Señal + Ruido con desvío 1")
print (snrRs10)
print("Relación Señal + Ruido con desvío 3")
print (snrRs30)
