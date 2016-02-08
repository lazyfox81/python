#!/usr/bin/python

import xml.etree.ElementTree as ET
import urllib.request

def get_weather():
    url = 'http://export.yandex.ru/weather-ng/forecasts/27612.xml'
    tree = ET.parse(urllib.request.urlopen(url))
    return tree.getroot()

if __name__ == '__main__':
    root = get_weather()
    ns = {'fc': 'http://weather.yandex.ru/forecast'}
    fact = root.find('fc:fact', ns)
    cond = fact.find('fc:weather_condition', ns)
    print(cond.get('code'), ",", end = ' ')
    print(fact.find('fc:temperature', ns).text, "\u00b0C")
