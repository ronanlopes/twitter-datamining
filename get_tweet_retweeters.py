# -*- coding: utf-8 -*-

import sys
import tweepy
import twitter
import json
import twitter
import types

#Autenticações

CONSUMER_KEY = 'ILHhQAC4QB0WNUdoRqmEA'
CONSUMER_SECRET = 'rmmkGo4YHniiJRwkwxGu9S7l5ZfhG7CZDXHw9eUo'
ACCESS_TOKEN = '339362662-rU6CizVcSZCr6CqWIhFh40yE0gmQdgusPRiwcpOj'
ACCESS_TOKEN_SECRET = 'CW9UCTOqYpzA1dS9doKcow6Bnz95UwZGBskcOsF2M6yIp'

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api.statuses.retweeters.ids(_id=533568021)['ids']
print
