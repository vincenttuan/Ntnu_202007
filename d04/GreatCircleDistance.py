import math
# 師大圖書館校區 25.027951, 121.528596
def cal_dis_meters(latitude1, longitude1,latitude2, longitude2):
    radius = 6378.137
    radLat1 = (math.pi/180)*latitude1
    radLat2 = (math.pi/180)*latitude2  
    radLng1 = (math.pi/180)*longitude1  
    radLng2= (math.pi/180)*longitude2  
    d=2.0*math.asin(math.sqrt(math.pow(math.sin((radLat1-radLat2)/2.0),2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin((radLng1-radLng2)/2.0),2)))*radius
    return d
