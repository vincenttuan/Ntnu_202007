import requests
import json

def getWeather(city):
    #apikey = open('api.key', 'r').read()
    apikey = '5b683d3872361d3b14e7df105df6a27d'
    path = 'https://api.openweathermap.org/data/2.5/find?q=%s&appid=%s'
    resp = requests.get(path % (city, apikey))
    # 分析 json
    data = json.loads(resp.text)
    main = data['list'][0]['main']
    description = data['list'][0]['weather'][0]['description']
    return main['temp'], main['feels_like'], main['humidity'], description

if '__main__' == __name__ :
    temp, feels_like, humidity, description = getWeather('Taipei')
    print("溫度: %.2f 體感: %.2f 濕度: %d %% %s" % (temp, feels_like, humidity, description))