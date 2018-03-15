import numpy as np
import matplotlib.pyplot as plt

datomancha = np.loadtxt("monthrg.dat")
anio = datomancha[:,0]
mes = datomancha[:,1]
dia = datomancha[:,2]
manchas = datomancha[:,3]
date = datomancha[:,0] +(datomancha[:,1]-1)/12.0
ii = date >1900


e = np.array([date[ii], manchas[ii]])
np.savetxt("fecha_mancha.dat", e.T)
