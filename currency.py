#!/usr/bin/python
# Weather in terminal
# required module 'termcolor'

import xml.etree.ElementTree as ET
import urllib.request

import sys
from termcolor import colored, cprint

import calendar

def get_currency():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?d=0'
    # print(url)
    tree = ET.parse(urllib.request.urlopen(url))
    return tree.getroot()

if __name__ == '__main__':
    root = get_currency()
    for currency in root:
        currency_code = currency.find('CharCode').text
        if currency_code == 'USD' or currency_code == 'EUR':
            print("%s %s" % (currency_code, currency.find('Value').text))
    # ns = {'fc': 'http://weather.yandex.ru/forecast'}
    # fact = root.find('fc:fact', ns)
    # cond = fact.find('fc:weather_condition', ns)
