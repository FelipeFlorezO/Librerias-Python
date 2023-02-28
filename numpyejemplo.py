import numpy as np
arr = np.random.randint(1,10, (3,2))
arr.shape
print(arr)
arr2 = arr.reshape(1,6)
print(arr)
print(arr2)
arr3 = arr.reshape(2,3)
print(arr3)
arr4 = np.reshape(arr, (1,6))
print(arr4)
