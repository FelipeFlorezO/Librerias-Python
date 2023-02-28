import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig, axes = plt.subplots(1,2,figsize=[5,5])
axes[0].plot(x,y,label="$sin(x)$")
axes[0].set_title('Relacion X-Y')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].legend()

axes[1].plot(y,x)
axes[1].set_title('Relacion Y-X')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')