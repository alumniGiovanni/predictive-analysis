import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


ds = pd.read_csv('insurance.csv')

print (ds.head(15))


#checking for null numbers
count_nan = ds.isnull().sum()
print(count_nan[count_nan>0])

#filling null numbers
ds['bmi'].fillna(ds['bmi'].mean(), inplace = True)