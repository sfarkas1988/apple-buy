from http import simple_get
from bs4 import BeautifulSoup
import re

class Geizhals():
    def __init__(self, url):
        self.url = url

    def getBestPrice(self):
        response = simple_get(self.url)
        if response.statusCode != 200:
            return response.onError()
        html = BeautifulSoup(response.content, 'html.parser')

        bestOffer = html.select('#offer__price-0 .gh_price')
        for offer in bestOffer:
            return float(next(iter(re.findall(r'\d+', offer.contents.__getitem__(0)) or []), None))