import numpy as np
import scipy.signal 
import librosa as lb
import matplotlib.pyplot as plt
###############################################################################
x,fsR = lb.load("parteReal.wav", sr=None)
#T1 = len(xR)/fsR

h, fsRI = lb.load("resp_imp.wav",sr=None)

y1 = scipy.convolve(x,h)
y2 = scipy.signal.fftconvolve(x,h, mode = 'full')