#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

from decimal import Decimal
import constant
from money import Money

class Offer():

    def __init__(self, title, price, description, vb, url):
        self.title = title
        self.price = float(price) if str(price).__len__() > 0 else None
        self.description = description
        self.vb = vb
        self.compared_to_geizhals = None
        self.url = url

    def toJson(self):
        return {
            'url': self.url,
            'title': self.title,
            'price': Decimal(self.price) if self.price else None,
            'description': self.description,
            'vb': self.vb,
            #'compared_to_geizhals': Decimal(self.compared_to_geizhals) if self.compared_to_geizhals else None
        }

    def toItemKey(self):
        return {
            'url': self.url,
            'title': self.title
        }

    def toSlackMessage(self):
        return '*'+self.title + \
            ' (' +  ('VB ' if self.vb is True else '' ) + str(Money(amount=self.price, currency=constant.CURRENCY)) +\
            ' - ' +\
            ('{0:.2g}'.format(self.compared_to_geizhals)) + '%)*\n\n' +\
            '_'+self.description+ '_\n\n' +\
            constant.URL_KLEINANZEIGEN+'/'+ self.url +\
            '\n\n\n\n'