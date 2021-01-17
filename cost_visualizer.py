#importing modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

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

#creating and opening stats report
unique_days = {df.index[0].split("-")[2]}

for day in df.index:
    unique_days.add(day.split('-')[2])    

first_year, first_month, first_day = df.index[0].split("-")
first_year, first_month, first_day = int(first_year), int(first_month), int(first_day)
last_year, last_month, last_day = df.index[len(df)-1].split("-")
last_year, last_month, last_day = int(last_year), int(last_month), int(last_day)

first_date = date(first_year, first_month, first_day)
last_date = date(last_year, last_month, last_day)
delta = last_date - first_date
num_of_days = delta.days + 1

print("The average amount spent per day is $%.2f."%(grandTotal / num_of_days))
print("The average amount spent per month is $%.2f."%(grandTotal / num_of_days * 30.436875))
print("The average amount spent per year is $%.2f."%(grandTotal / num_of_days * 365.25))

plt.show()








