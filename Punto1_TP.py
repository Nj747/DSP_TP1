import numpy as np
import matplotlib.pyplot as plt
import librosa as lb
###############################################################################
""" Funciones """
###############################################################################
# fs -------> frecuencia de muestreo
# data -----> la saeñal perse
# filename -> nombre del archivo a guardar
###############################################################################
def GenerarWavLibrosa(fs,data,filename):
    lb.output.write_wav(filename + '.wav', data, fs)
    
def pdsexp(F0, R, Ar, phi_r, fs, t):
    x = []
    xt = []
    n = np.arange(0,t,1/fs); 
    for r in range(0,R): 
        x.append(Ar[r]*np.exp(1j*2*np.pi*r*F0*n + phi_r[r]))
    xt = [sum(i) for i in zip(*x)]        
    return n,np.real(xt),np.imag(xt);
###############################################################################
""" Implementacion Punto 1 """ 
###############################################################################
# Variables
# fs ----> frecuencia de muestreo
# t -----> duracion de la señal
# F0 ----> Frecuencia central
# R -----> numero entero que multiplica a F0
# Ar ----> amplitud de cada exponencial
# phi_r -> fase de cada exponencial
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
""" Ploteo de señales """
###############################################################################
plt.figure(figsize=(10,6.5))
plt.subplots_adjust(hspace=0.5)

plt.subplot(2,1,1)
plt.plot(n[100:400],xR[100:400],color = "blue")
plt.title("Parte Real")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")

plt.subplot(2,1,2)
plt.plot(n[100:400],xI[100:400], color = "red")
plt.title("Parte Imaginaria")
plt.grid(True)
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()
###############################################################################
""" Generar wavs de parte Real y parte Imaginaria """
# xRnorm -> señal normalizada de la parte Real (xR)
###############################################################################
xRnorm = xR/np.max(xR)
GenerarWavLibrosa(fs,xRnorm,'parteReal')
GenerarWavLibrosa(fs,xI,'parteImaginaria')