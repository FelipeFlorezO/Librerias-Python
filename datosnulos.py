import pandas as pd
import numpy as np

dict = {'col1':[1,2,3,np.nan],
 'col2':[4,np.nan,6,7],
 'col3':['a','b','c',None]}
df = pd.DataFrame(dict)
print(df)

df.isnull()
df.isnull()*1
df.fillna('Missing')
df.fillna(df.mean())
df.interpolate()
df.dropna()
