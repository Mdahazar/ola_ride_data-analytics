import pandas as pd

df = pd.read_excel("../data/OLA_DataSet.xlsx")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())