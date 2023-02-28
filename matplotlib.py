import matplotlib.pyplot as plt
import numpy as np

country = ['INDIA','JAPAN','MEXICO','COLOMBIA','GERMANY']
population =[1000,800,900,1000,300]
plt.bar(country,population,width=0.5,color=['red','blue'])
plt.xticks(np.arange(5),('INDIA','JAPAN','MEXICO','COLOMBIA','ALEMANIA'), rotation=45)
plt.show()