'''
Created on Jun 3, 2015

@author: Chintalapati
'''
from flask import Flask, jsonify, request
from datetime import datetime
from report import resourceHandler

app = Flask(__name__)

@app.route('/report/today/<zipCode>', methods=['GET'])
def getZipCurrentWeather(zipCode=None):
    message = None
    if zipCode is None:
        message = "Please provide City, State or Zip"
        return jsonify(message)
    else:
        resourceHandler.getCurrentWeather(zipCode, datetime.today())


@app.route('/report/today', methods=['GET'])
def getCityCurrentWeather():
    city = request.args.get('city')
    state = request.args.get('state')
    if city is None and state is None:
        return jsonify("Both City and State are required")

@app.route('/forecast/<zipCode>/<forecastDays>', methods=['GET'])
def getZipForecast(zipCode=None, forecastDays=5):
    if zipCode is None:
        return jsonify("Please provide City, State or Zip")
    else:
        resourceHandler.getForecastForZip(zipCode, forecastDays)