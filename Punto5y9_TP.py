import librosa as lb
import numpy as np
import matplotlib.pyplot as plt
###############################################################################
""" Funciones """
###############################################################################
# fs -------> frecuencia de muestreo
# data -----> la saeñal perse
# filename -> nombre del archivo a guardar
###############################################################################
def GenerarWavLibrosa(fs,data,filename):
    lb.output.write_wav(filename + '.wav', data, fs)
###############################################################################
""" Media Móvil """
###############################################################################
# M ---------------> largo de la ventana
# iteraciones -----> movilidad de la ventana 
# k ---------------> variable auxilar para delimitar ventaneo
# acum ------------> acumulador de valores dentro de la ventana
# prom ------------> promedio
###############################################################################
def mediamovild(x,M):
    prom =[]
    k = 0
    iteraciones = len(x) - M + 1
    for i in range(iteraciones):
        acum = 0
        for j in range(k,k + M):
            acum = acum + x[j]
        prom.append(acum/M)
        k = k + 1
    return prom
###############################################################################
""" Media Móvil Recursiva """ 
###############################################################################
def mediamovildr(x,M):
   y=[0 for x in range(len(x))]
   if M%2 == 0:
       acum = 0
       for i in range(M):
           acum=acum+x[i]
       y[M//2]=acum/M        
       for n in range((M//2)+1,len(x)-((M//2)-1)):
           acum=acum - x[n-((M//2)+1)] + x[n + ((M//2)-1)]
           y[n]=acum/M              
   else:
       acum=0
       for i in range(M):
           acum=acum+x[i]
           y[M//2]=acum/M
           
       for n in range((M//2)+1,len(x)-(M//2)):
            acum=acum - x[n-((M//2)+1)] + x[n + ((M//2))]
            y[n]=acum/M
   return y
###############################################################################
""" Implementación de Punto 5 """
###############################################################################
def pdsexp(F0, R, Ar, phi_r, fs, t):
    x = []
    xt = []
    n = np.arange(0,t,1/fs); 
    for r in range(0,R): 
        x.append(Ar[r]*np.exp(1j*2*np.pi*r*F0*n + phi_r[r]))
    xt = [sum(i) for i in zip(*x)]        
    return n,np.real(xt),np.imag(xt);
###############################################################################
fs = 44100 
t = 2 
F0 = 440 
R = 5
Ar = [1, 1/2, 1/3, 1/4, 1/5] 
phi_r = [0, 0, 0, 0, 0] 
###############################################################################   
n,xR,xI = pdsexp (F0, R, Ar, phi_r, fs, t)
###############################################################################
n = np.arange(0,len(xR),1)
# con un tamaño de ventana de 30 se reduce muchisimo los armónicos 4 y 5
M = 30 
###############################################################################
import timeit
start_time = timeit.default_timer()
xfd = mediamovild(xR,M) # media movil
tiempo_xfd = timeit.default_timer() - start_time

start_time = timeit.default_timer()
xfr = mediamovildr(xR,M) # media movil recursiva
tiempo_xfr = timeit.default_timer() - start_time
###############################################################################
""" Resultados de comparación de los tiempos de ejecución """
###############################################################################
print ("La media movil tarda: " + str(tiempo_xfd) + " segundos")
print ("La media movil recursiva tarda: " + str(tiempo_xfr) + " segundos")
# Leer: la media móvil recursiva tarda menos que la media móvil hecha por 
#       iteraciones.    
###############################################################################
""" Ploteo de las señales """ 
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,2,1)
plt.plot(n[100:400],xR[100:400])
plt.plot(n[100:400],xfd[100:400])
plt.title("Media Movil")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo [s]")
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(n[100:400],xR[100:400])
plt.plot(n[100:400],xfr[100:400])
plt.title("Media Movil Recursivo")
plt.ylabel("Amplitud")
plt.xlabel("Tiempo [s]")
plt.grid(True)

# fft de la señal original y la filtrada con media movil
from numpy.fft import fft, fftfreq

freq = fftfreq(88200)
fftval = fft(xR)
fft_theo = np.abs(fftval/88200)

fftval_filtrada = fft(xfd)
fft_theo2 = np.abs(fftval_filtrada/88200)

mask = freq>0

plt.subplot(2,2,2)
plt.plot(freq[mask],fft_theo[mask])
plt.title("FFT señal sin filtrar")
plt.ylabel("Amplitud")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(freq[mask],fft_theo2[0:44099])
plt.title("FFT señal filtrada")
plt.ylabel("Amplitud")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)

plt.show()
###############################################################################
""" Generar wavs """
###############################################################################
GenerarWavLibrosa(fs,np.array(xfd),"senalFiltrada.wav")