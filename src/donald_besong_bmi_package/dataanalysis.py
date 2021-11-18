import pandas as pd

class DataAnalysis():
 def __init__(self, data):
  self.data = data
  self.pandasDf = ''
  self.results = None
  
 def createDf(self, nMin, nMax):
  i = nMin
  df = None
  col_names = ''
  while i < nMax:
   x = next(self.data,None)
   if i == nMin:
    df = pd.DataFrame(x, index=[0])
   else:
    df = df.append(x, ignore_index=True)

   i += 1
  self.pandasDf = df
  
 def calcBmi(self):
  self.pandasDf['Bmi'] = self.pandasDf.WeightKg/pow(self.pandasDf.HeightCm/100, 2)
  
 def createDfByFilter(self, mydf):
  df = mydf
  return(df)
 

  





