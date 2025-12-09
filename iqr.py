import pandas as pd
import numpy as np
#Outliers

df = pd.DataFrame({'K':[1,2,3,10000]})
q1 = df['K']. quantile(0.25)
q3 = df['K']. quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df = df[(df['K'] >= lower_bound) & (df['K'] <= upper_bound)]
mean_value = df['K'].mean()
print(df['K'])

