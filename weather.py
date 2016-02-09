#!/usr/bin/python
# Weather in terminal
# required module 'termcolor'

import xml.etree.ElementTree as ET
import urllib.request

import sys
from termcolor import colored, cprint

def get_weather(req_id):
    url = 'http://export.yandex.ru/weather-ng/forecasts/%s.xml' % (req_id)
    # print(url)
    tree = ET.parse(urllib.request.urlopen(url))
    return tree.getroot()

if __name__ == '__main__':
    id_city = 27612 #https://pogoda.yandex.ru/static/cities.xml
    root = get_weather(id_city)
    ns = {'fc': 'http://weather.yandex.ru/forecast'}
    fact = root.find('fc:fact', ns)
    cond = fact.find('fc:weather_condition', ns)
    text = "Weather from %s" % (root.get('link'))
    cprint(text, 'magenta', attrs=['bold'])
    text = "Conditions for %s at %s" % (fact.find('fc:station', ns).text,
                                       fact.find('fc:observation_time', ns).text)
    cprint(text, 'blue', attrs=['bold'])
    print("Current conditions:\n%s(%s), %s\u00b0C" %
          (cond.get('code'), fact.find('fc:weather_type', ns).text,
           fact.find('fc:temperature', ns).text))
