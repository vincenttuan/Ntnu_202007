import requests

path = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
resp = requests.get(path)
print(resp.text)