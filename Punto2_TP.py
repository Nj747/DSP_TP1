import numpy as np
###############################################################################
def CalcularDesvio(noise):
    desvioPercentual = np.abs(1 - np.std(noise)) * 100
    return print(str(desvioPercentual) + " %")
###############################################################################
""" Implementación Punto 2 """
###############################################################################
noise0 = np.random.normal(0,1,5)
noise1 = np.random.normal(0,1,10)
noise2 = np.random.normal(0,1,100)
noise3 = np.random.normal(0,1,1000)
noise4 = np.random.normal(0,1,10000)
noise5 = np.random.normal(0,1,100000)
###############################################################################
# Muestra de las diferencias entre los desvios 
###############################################################################
CalcularDesvio(noise0)
CalcularDesvio(noise1)
CalcularDesvio(noise2)
CalcularDesvio(noise3)
CalcularDesvio(noise4)
CalcularDesvio(noise5)
