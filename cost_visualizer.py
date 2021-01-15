#importing modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cost_sheet.csv', header = 0, index_col = 0)

costDict = {}

for costType in df["Type"].unique():
    costDict[costType] = []

for key in costDict.keys():
    dfType = df[df["Type"] == key]
    costTypePriceList = [float(price.replace("$", "")) for price in dfType['Amount']]
    costDict[key] = "$%.2f"%sum(costTypePriceList)
    
print(costDict)






