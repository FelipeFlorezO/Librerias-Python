import numpy as np
import matplotlib.pyplot as plt

N = 1000

def f(x):
    
    return x**2

c = 5
x = np.linspace(-10,10,num=N)
y = f(x + c)
fig, ax = plt. subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')