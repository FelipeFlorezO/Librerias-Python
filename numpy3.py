import numpy as np
arr = np.random.randint(1,20,10)
matriz = arr.reshape(2,5)
matriz
print(arr)
print(arr.max())
print(matriz.max(0))
print(arr.argmax())
print(matriz.argmax(0))
