import numpy as np 
import pandas as pd
l1 = [1, 2, 3, 4, 5, 6]
labels = ['a', 'b', 'c', 'd', 'e', 'f']
d1 = {"A":10, "B":20, "C":30, "D":40, "E":50}
s1 = pd.Series(l1)
print(s1)
print(s1[5])
s2 = pd.Series(labels)
print(s2)
print(s2[4])
s3= pd.Series(data=l1, index=labels)
print(s3)
print(s3["e"])
arr = np.random.randint(low= 1, high = 100 , size= (5,4))
print(arr)
print(type(arr))
print(pd.DataFrame(arr))
df = pd.DataFrame(arr, index = ["A", "B", "C", "D", "E"], columns= ["D", "U", "B", "A"])
print(df)
print(type(df))
print(df["U"])
print(df.loc["D"])
print(df[["D","B", "A"]])
print(df.iloc[3])
print(np.__version__ )
print(pd.__version__)
print(df.iloc[2])
df['Bird'] = [10,20,30,40,50]
print(df)
print(df.drop('Bird', axis = 1))
df.drop('B', axis = 1, inplace = True)
print(df)
print((df['U'] % 2 == 0) & (df['D'] % 2 == 0))