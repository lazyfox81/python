#!/usr/bin/python
# Weather in terminal
# required module 'termcolor'

import xml.etree.ElementTree as ET
import urllib.request

import sys
from termcolor import colored, cprint

import calendar

def get_root():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?d=0'
    tree = ET.parse(urllib.request.urlopen(url))
    return tree.getroot()

def get_currency(root):
    rate = {}
    for currency in root:
        currency_code = currency.find('CharCode').text
        rate[currency_code] = currency.find('Value').text
    return rate

if __name__ == '__main__':
    # ns = {'fc': 'http://weather.yandex.ru/forecast'}
    # fact = root.find('fc:fact', ns)
    # cond = fact.find('fc:weather_condition', ns)
    currency_rate = get_currency(get_root())
    title = "Currency rate at %s" % (get_root().get('Date'))
    cprint(title, 'magenta', attrs=['bold'])
    cprint(("USD:\t%s" % (currency_rate['USD'])), 'cyan', attrs=['bold'])
    cprint(("EUR:\t%s" % (currency_rate['EUR'])), 'cyan', attrs=['bold'])
