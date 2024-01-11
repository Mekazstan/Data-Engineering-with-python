import pandas as pd

df=pd.read_csv('data.CSV')
first_ten = df.head(10)

print(first_ten)