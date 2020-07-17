import requests
import json

path = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
resp = requests.get(path)
data = json.loads(resp.text)
retVal = data['retVal']
sbi = 30
bemp = 30
for i in range(1, 405):
    sno = '%04d' % i
    try:
        youbike = retVal[sno]
        if(int(youbike['sbi']) >= sbi and int(youbike['bemp']) >= bemp):
            print(youbike)
    except:
        #print('無此站台', sno)
        pass
