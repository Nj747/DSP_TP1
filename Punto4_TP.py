import numpy as np
import librosa as lb
###############################################################################
""" Funciones """
###############################################################################
# el parámetro n es la cantidad de señales q quiero generar
def NoiseGenerator(n):    
    noise = []
    # genero las n señales
    for i in range(0,n):
        noise.append(np.random.normal(0,3,88200))        
    return noise,n
###############################################################################
# xR-> señal calculada en el punto 1    
def SignalSum(xR,noise,n):
    result = []
    for i in range(0,n):
        result.append(noise[i] + xR)
        return result
###############################################################################
def Relsnr(r):
    snr = np.max(r)/np.std(r)
    return snr
###############################################################################
""" Implementación Punto 4 """
###############################################################################
xR,fs = lb.load("parteReal.wav",sr=None)
# prueba con 10 señales
ruidos,n = NoiseGenerator(10)
r = SignalSum(xR,ruidos,n) 
# señal/ruido 
print("Relación snr con 10 señales de ruido con desvio 3")
print(Relsnr(r))
# prueba con 100 señales de ruido
ruidos2,n2 = NoiseGenerator(100)
r2 = SignalSum(xR,ruidos2,n2)
# señal/ruido 
print("Relación snr con 100 señales de ruido con desvio 3")
print(Relsnr(r2))
# prueba con 1000 señales de ruido
ruidos3,n3 = NoiseGenerator(1000)
r3 = SignalSum(xR,ruidos3,n3)
# señal/ruido 
print("Relación snr con 1000 señales de ruido con desvio 3")
print(Relsnr(r3))
""" Leer: los valores de snr dan parecidos porque la cantidad de ruido (n) 
no varía el cálculo del snr, sino más bien el desvío de las señales generadas 
que en dicho caso, poseen el mismo desvío estándar de 3 """