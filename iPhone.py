import urllib
import constant

class iPhone():
    def __init__(self, label, capacity, color, geizhals_url):
        self.label = label
        self.capacity = capacity
        self.color = color
        self.geizhals_url = geizhals_url
        self.geizhals_price = None
        self.kleinanzeigen_offers = []

    def toString(self):
        return "iPhone " + self.label + " " + str(self.capacity)+"GB " + self.color

    def toGeizhalsSearchUrl(self):
        return constant.URL_GEIZHALS+'/?fs='+ urllib.quote_plus(self.toString()).lower()
    def toKleinanzeigen(self):
        return constant.URL_KLEINANZEIGEN + '/s-anzeige:angebote/iphone-'+str(self.label).lower()+'-'+str(self.capacity)+'gb/k0'

