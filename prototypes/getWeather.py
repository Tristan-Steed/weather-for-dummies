import requests
import json

def getCurrentTemp(lat,lon):
    url="https://api.weatherbit.io/v2.0/current?lat={}6&lon={}&key=ae508f5c8f1f4a5f9f8920a3f3e19c5a".format(lat,lon)
    return requests.get(url)

def getTodaysWeather(lat,lon):
    datas=getCurrentTemp(lat,lon).json()
    data=datas['data'][0]
    description=data['weather']['description']
    city=data['city_name']
    tempriture=data['app_temp']
    tempriture_descriptor='default';
    if(tempriture>40):
        tempriture_descriptor="very hot"
    elif(tempriture<40 and tempriture>30):
        tempriture_descriptor="hot"
    elif(tempriture<30 and tempriture>20):
        tempriture_descriptor="warm"
    elif(tempriture<20 and tempriture>10):
        tempriture_descriptor="chilly"
    elif(tempriture<10 and tempriture>0):
        tempriture_descriptor="cold"
    else:
        tempriture_descriptor="freezing cold"
    return {'info':"It is going to be a {} day today in {} ,{} has also been forecasted for today.".format(tempriture_descriptor,city,description),'temp':tempriture}
    

print(getTodaysWeather(-33.917419, 18.386274)['temp'])
