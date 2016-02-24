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
    id_city = 27612             # https://pogoda.yandex.ru/static/cities.xml
    root = get_weather(id_city)
    ns = {'fc': 'http://weather.yandex.ru/forecast'}
    fact = root.find('fc:fact', ns)
    cond = fact.find('fc:weather_condition', ns)
    cprint('Yandex.Pogoda', 'red', attrs=['bold'])
    text = "Conditions for %s at %s" % (
        root.get('slug').capitalize(),
        fact.find('fc:observation_time', ns).text)
    cprint(text, 'cyan', attrs=['bold'])
    print("%s (%s), %s\u00b0C" %
          (cond.get('code').capitalize(), fact.find('fc:weather_type', ns).text,
           fact.find('fc:temperature', ns).text))
    for day in root.findall('fc:day', ns):
        cprint (day.get('date'), 'red', attrs=['bold'])
        for day_part in day.findall('fc:day_part', ns):
            cond = day_part.find('fc:weather_condition', ns)
            temp_data = day_part.find('fc:temperature-data', ns)
            avg_temp_str = temp_data.find('fc:avg', ns).text
            day_part_str = day_part.get('type')
            if day_part_str == "day_short" or day_part_str == "night_short":
                print ("%s\t%s %s" %
                       (day_part_str, cond.get('code').capitalize(), avg_temp_str))
