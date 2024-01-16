import pandas as pd

df=pd.read_csv('scooter.csv')

# # View the available columns in the dataset
# print(df.columns)

# # View the column datatypes
# print(df.dtypes)

# print(df.head(5))

# # Setting the number of columns to show
# pd.set_option('display.max_columns', 500)

# # Single column display
# df['Trip Duration']

# # Multi column display
# print(df[['Trip ID','Trip Duration','Start Community Area Name']]) 

# # Getting a random sample
# df.sample(5)

# # Frame slicing
# print(df[3:9])

# # Displaying a single row using its index
# print(df.loc[34221])

# # Finding a single column for a particular row                      NB: AT works similar with LOC based on index
# print(df.at[2, 'Trip Duration'])

# # Selecting of row using methods
# user = df.where(df['Vendor']=='spin')
# user = df[(df['Vendor']=='spin')]
# print(user)

print(df.columns)

# Combining 2 statements
one=df['Vendor']=='spin'
two=df['trip_ledger_id']==1488838
# print(df.where(one & two))

print(df[(one)&(two)])