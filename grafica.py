import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("fecha_mancha.dat")
xaxis= datos[:,0]
yaxis = datos[:,1]

plt.plot(xaxis, yaxis, c ="m")
plt.xlabel("tiempo")
plt.ylabel("manchas")
plt.title("manchas vs tiempo")
plt.savefig("fecha_mancha.pdf")
