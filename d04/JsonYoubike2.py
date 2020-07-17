import requests
import json
import d04.GreatCircleDistance as gcd
path = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
resp = requests.get(path)
data = json.loads(resp.text)
retVal = data['retVal']
sbi = 10
bemp = 10
for i in range(1, 405):
    sno = '%04d' % i
    try:
        youbike = retVal[sno]
        if(int(youbike['sbi']) >= sbi and int(youbike['bemp']) >= bemp):
            # 計算距離
            # 站台的經緯度
            lat = float(youbike['lat'])
            lng = float(youbike['lng'])
            d = gcd.cal_dis_meters(25.027951, 121.528596, lat, lng)
            print(d, youbike)
    except:
        #print('無此站台', sno)
        pass
