import pandas as pd
import numpy as np
testList=pd.read_csv("pgm40.csv")
for line in testList:
        for word in line.split():
       		if word.startswith("m"):
          		print(word)
