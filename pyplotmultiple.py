#SUBPLOTS: ORIENTADO A OBJETOS, MULTIPLES GRAFICAS

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)
fig, axes = plt.subplots()
axes.plot(x,y,'b')

fig, axes = plt.subplots(nrows=2, ncols=4)
axes[0,0].plot(x, np.cos(x))
axes[1].plot(y,x,'r')


