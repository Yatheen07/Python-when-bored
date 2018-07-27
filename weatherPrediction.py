# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 20:29:14 2018

@author: kmy07
"""
next_week = []

def predict_weather():
    from weather import Weather,Unit
    from collections import Counter
    next_week = []
    weather = Weather(Unit.CELSIUS)
    lookup = weather.lookup_by_latlng(13.009575, 80.004243)
    condition = lookup.condition
    print(condition.text)
    
    location = weather.lookup_by_location('chennai')
    forecasts = location.forecast
    
    for forecast in forecasts:
        next_week.append(forecast.text)
        print(forecast.date)
        print(forecast.high)
        print(forecast.low) 
        
    c=Counter(next_week)
    print(c)
        
predict_weather()




