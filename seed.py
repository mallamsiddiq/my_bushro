import mysql.connector
import pandas as pd
from requests.auth import HTTPBasicAuth
import requests
import json

url = 'https://api.quickbutik.com/v1/orders'
headers = {'Accept': 'application/json','Authorization': 'Basic V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJpI2g6V0MwKSlrODNOUm00ZE10KmYzI3guNHJSb1ZVaDJ pI2g='
}
#auth = HTTPBasicAuth('apikey', 'YXBpX2tleV9oZXJlOmFwaV9rZXlfaGVyZQ')


d=requests.get(url, headers=headers).json()
data = pd.DataFrame.from_records(d)
m=data.columns
text = json.dumps(d,sort_keys=True, indent=4)

#data=df[['id','login','url','avatar_url','type','html_url']]
data2=data.to_json(orient='records')
data2=json.loads(data2)

data.to_json('data.json', orient='records', lines=True)

text = json.dumps(d,sort_keys=True, indent=4)

f = open("text.json", "wt")
f.write(text)


print (data2)
print(d)