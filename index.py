#!/usr/bin/python -tt
# -*- coding: UTF-8 -*-

from iPhone import iPhone
from kleinanzeigen import *
import json
from geizhals import Geizhals
from dynamodb import dynamodb
import constant
from decimal import Decimal
import slack_webhook
from money import Money


iphones = [
    #iPhone('8', 256, 849),

    # iPhone('8 Plus', 64, 789),
    # iPhone('8 Plus', 256, 959),
    #
    iPhone('XS', 64, 'grau', 'https://geizhals.de/apple-iphone-xs-64gb-grau-a1887134.html'),
    # iPhone('XS', 256, 1319),
    # iPhone('XS', 512, 1549),
    #
    iPhone('XS Max', 64, 'grau', 'https://geizhals.de/apple-iphone-xs-max-64gb-grau-a1887140.html'),
    # iPhone('XS Max', 256, 1419),
    # iPhone('XS Max', 512, 1649),
    #
    iPhone('XR', 64, 'schwarz', 'https://geizhals.de/apple-iphone-xr-64gb-schwarz-a1887154.html'),
    #iPhone('XR', 128, 'schwarz', 'https://geizhals.de/apple-iphone-xr-128gb-schwarz-a1887151.html'),
    #iPhone('XR', 256, 'schwarz', 'https://geizhals.de/apple-iphone-xr-256gb-schwarz-a1887121.html'),
    #iPhone('X', 64, 'grau', 'https://geizhals.de/apple-iphone-x-64gb-grau-a1688629.html'),
]


for iphone in iphones:
    iphone.geizhals_price = Geizhals(iphone.geizhals_url).getBestPrice()
    offers = kleinanzeigen.getOffers(iphone.toKleinanzeigen())
    valuable_price = iphone.geizhals_price*float(0.9)

    messages = []
    for offer in offers:
        if offer.price < valuable_price:
            existing_offer = dynamodb.get_item(constant.TABLE_OFFERS, offer.toItemKey())
            if existing_offer is None:
                offer.compared_to_geizhals = 100 - (offer.price * 100 / iphone.geizhals_price) if offer.price is not None else None
                if (offer.compared_to_geizhals >= 15):
                    messages.append(offer.toSlackMessage())
                dynamodb.put_item(constant.TABLE_OFFERS, offer.toJson())
            else:
                print 'Exists: ' + existing_offer['title'] + ' ' + str(existing_offer['price'])

    if len(messages) > 0:
        slack_webhook.send_message(
            '*==========================================================*\n' +
            '*=========='+iphone.toString() +
            ' (' + str(Money(amount=iphone.geizhals_price, currency=constant.CURRENCY)) + ')==========*' +
            '\n' + iphone.toKleinanzeigen() +
            '\n*==========================================================*\n'
        )
        for message in messages:
            slack_webhook.send_message(message)