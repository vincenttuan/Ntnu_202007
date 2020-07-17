import requests
import json

def getWeather(city):
    apikey = open('api.key', 'r').read()
    path = 'https://api.openweathermap.org/data/2.5/find?q=%s&appid=%s'
    resp = requests.get(path % (city, apikey))
    # 分析 json
    data = json.loads(resp.text)
    main = data['list'][0]['main']
    return main['temp'], main['feels_like'], main['humidity']

if '__main__' == __name__ :
    temp, feels_like, humidity = getWeather('Taipei')
    print("溫度: %.2f 體感: %.2f 濕度: %d %%" % (temp, feels_like, humidity))