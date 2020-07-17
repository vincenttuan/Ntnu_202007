import requests

def getWeather(city):
    apikey = open('api.key', 'r').read()
    path = 'https://api.openweathermap.org/data/2.5/find?q=%s&appid=%s'
    resp = requests.get(path % (city, apikey))
    print(resp.text)

if '__main__' == __name__ :
    getWeather('Taipei')