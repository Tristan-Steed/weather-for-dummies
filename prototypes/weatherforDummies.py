import getWeather
from flask import Flask,jsonify,request
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)



# get the weather
@app.route('/getWeatherReport/<string:Strlat>/<string:Strlongitude>',methods=['GET'])
def getWeatherReport(Strlat,Strlongitude):
    lat=float(Strlat)
    longitude=float(Strlongitude)
    returnResponse=[]
    returnResponse.append(getWeather.getTodaysWeather(lat,longitude))
    return jsonify({"weatherForecast":returnResponse})




if __name__=='__main__':
    app.run(debug=True)