import iterdata
import dataanalysis
import main_argparser
import argparse

#*****************begin reading arguments
data_source = main_argparser.data_source
nMin = main_argparser.nMin
nMax = main_argparser.nMax
category = main_argparser.category
fullMessage = main_argparser.fullMessage   
#*****************end reading arguments

x = iterdata.IterData(data_source)
x.iterRead()

A = dataanalysis.DataAnalysis(x.jsonProperty)
A.createDf(nMin,nMax)
A.calcBmi()

#below if to help with filtering
x_low = [0, 18.5, 25, 30, 35, 40]
x_high = [18.5, 25, 30, 35, 40, 10000]
x_cat = ["under_weight", "normal_weight", "over_weight", "moderately_obese", "severely obese", "very_severely_obese"]
x_risk = ["malnutrition risk", "low risk", "enhanced risk", "medium risk", "high risk", "very high risk"]

categoryTable = {cat: {"high":high, "low":low, "risk":risk} for cat, high, low, risk in zip(x_cat, x_high, x_low, x_risk)}

B = A.pandasDf.loc[A.pandasDf.Bmi.between(categoryTable[category]['low'], categoryTable[category]['high'])]
message = categoryTable[category]['risk']

if __name__ == '__main__':
    if fullMessage > 0:
     print('The following have %s' % message)
     print(B)
    print('***Number of people with %s is %s ***' % (message, len(B)))
    




