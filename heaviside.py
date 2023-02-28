import numpy as np
import matplotlib.pyplot as plt

def H(x):
    Y = np.zeros(len(x))
    for  idx,x in enumerate(x):
        if x>= 0:
            Y[idx]=1
        return Y
N = 1000

x = np.linspace(-10, 10, num=N)

y = H(x)
plt.plot(x,y)
