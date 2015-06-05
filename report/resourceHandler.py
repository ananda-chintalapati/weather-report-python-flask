'''
Created on Jun 3, 2015

@author: Chintalapati
'''
from flask import request, jsonify
from datetime import datetime

baseUrl = "http://api.openweathermap.org/data/2.5/"

def buildUSZipUrl(zipCode, mode='forecast'):
    return baseUrl + mode + "?" + zipCode +",us"

def getCurrentWeather(zipCode, date=datetime.today()):
    url = buildUSZipUrl(zipCode, 'weather')
    weatherResponse = request.get(url)
    if weatherResponse.status_code == 200:
        return weatherResponse.content
    else:
        return jsonify("Error while collecting weather report")


def getForecastForZip(zipCode, forecastDays):
    url = buildUSZipUrl(zipCode)
    weatherResponse = request.get(url)
    if weatherResponse.status_code == 200:
        return weatherResponse.content
    else:
        return jsonify("Error while collecting weather report")