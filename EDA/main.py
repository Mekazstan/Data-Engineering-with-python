import pandas as pd

df=pd.read_csv('scooter.csv')

# View the available columns in the dataset
print(df.columns)

# View the column datatypes
print(df.dtypes)

print(df.head(5))

# Setting the number of columns to show
pd.set_option('display.max_columns', 1500)