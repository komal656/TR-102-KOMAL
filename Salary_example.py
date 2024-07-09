import pandas as pd 
df = pd.read_excel(r"C:\Users\AMANDEEP SINGH\Desktop\Salaries_data_analysis.xlsx")
print (df)
"""print(df.head(15))
print(df.tail(5))"""
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
