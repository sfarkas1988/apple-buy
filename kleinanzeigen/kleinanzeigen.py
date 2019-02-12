#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

from http import simple_get
from bs4 import BeautifulSoup
from offer import Offer
import re

def getOffers(url):
    offers = []
    response = simple_get(url)
    if response.statusCode != 200:
        return response.onError()
    html = BeautifulSoup(response.content, 'html.parser')

    items = html.select('.ad-listitem')
    for item in items:
        details = item.select('.aditem-details')
        main = item.select('.aditem-main')
        if details.__len__() == 0:
            continue
        price_label = details[0].select('strong')
        if len(price_label) == 0 or len(price_label[0].contents) == 0:
            continue

        price = price_label[0].contents[0]
        vb = True if "VB" in price else False

        price = u' '.join(price).encode('utf-8').replace(' ', '').replace('€', '').replace('VB', '').replace('.', '')
        title = main[0].select('h2')[0].select('a')[0].contents[0]
        url = main[0].select('h2')[0].find('a', href=True)
        url = url['href']
        description = main[0].select('p')[0].contents[0]
        #keywords = ['tausche', 'Tausch']
        #if any(re.findall('|'.join(keywords), description)) or any(re.findall('|'.join(keywords), title)):
        if price:
            offers.append(Offer(title, price, description, vb, url))
    return offers