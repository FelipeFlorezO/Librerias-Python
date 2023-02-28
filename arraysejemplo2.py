import numpy as np
v1 = list(range(0,10))
v2 = np.arange(0,20,2)
print(v2)

v3 = np.zeros((10,5))
print(v3)

v4 = np.ones((10,5))

print(v4)

v5 = np.linspace((0,10), 100)
print(v5)

v6 = np.eye(4)
print(v6)

v7 = np.random.rand(4,4)
print(v7)

v8 = np.random.randint(1,100, (10,10))
print(v8)