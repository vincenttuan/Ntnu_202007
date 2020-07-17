import requests
import json

path = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
resp = requests.get(path)
print(resp)
list = json.loads(resp.text)
#print(list)
for data in list:
    if data['品名'].__contains__("日本"):
        print(data['品名'], data['不合格原因'])