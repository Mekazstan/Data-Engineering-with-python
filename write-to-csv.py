from faker import Faker
import csv

output=open('data.CSV','w')
fake=Faker()

header=['name','age','street','city','state','zip','lng','lat']

mywriter=csv.writer(output)
mywriter.writerow(header)

for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18,
    max=80, step=1), fake.street_address(), fake.city(),fake.
    state(),fake.zipcode(),fake.longitude(),fake.latitude()])
output.close()




# --------------- Writing as a Dataframe ---------------
import pandas as pd

data={'Name':['Paul','Bob','Susan','Yolanda'],
      'Age':[23,45,18,21]}

df=pd.DataFrame(data)
df.to_csv('fromdf.CSV',index=False)