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
    costDict[key] = sum(costTypePriceList)
    
grandTotal = sum([value for value in costDict.values()])
foodTotal = costDict['grocery'] + costDict['takeout'] + costDict['restaurant']

costDict['food total'] = foodTotal
costDict["total"] = grandTotal

categories = [category for category in costDict.keys()]
amounts = [amount for amount in costDict.values()]

line = plt.bar(categories, amounts)
plt.xticks(rotation=70)
plt.xlabel('Category')
plt.ylabel("Amount in CAD")
plt.title("Cost Breakdown")
for i in range(len(amounts)):
    plt.annotate("%.2f"%amounts[i], xy=(categories[i],amounts[i]), ha='center', va='bottom')
plt.gcf().subplots_adjust(bottom=0.30)

#automatically adjust ylim max
ylimMax = grandTotal + 200

plt.ylim(-1,ylimMax)
plt.show()






