import json

with open("data.JSON","r") as f:
    data=json.load(f)
    print(data['records'][0])
    
    
# --------------- Reading from json as a Dataframe --------------- 
import pandas.io.json as pd_JSON
  
f=open('data.JSON','r')

data=pd_JSON.loads(f.read())
df=pd_JSON.json_normalize(data,record_path='records')

first_two = df.head(2).to_json()
df.head(2).to_JSON(orient='records')

print(first_two)

