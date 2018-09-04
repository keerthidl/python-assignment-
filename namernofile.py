import pandas as pd
import numpy as np 
from pandas import DataFrame

df = pd.DataFrame({'regno': ["001","002","003"], 'name': ["abc","bcd","cde"]})

df.columns = ['regno','name']
print(df)

regno=["001","002","003"]
name=["abc","bcd","cde"]
df = {'regno': [], 'name': []}
df['regno'].append(regno)
df['regno'].append(name)
print(df['regno'])