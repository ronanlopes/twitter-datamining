# -*- coding: utf-8 -*-

import sys
import tweepy
import twitter
import json


#Autenticações

CONSUMER_KEY = 'ILHhQAC4QB0WNUdoRqmEA'
CONSUMER_SECRET = 'rmmkGo4YHniiJRwkwxGu9S7l5ZfhG7CZDXHw9eUo'
ACCESS_TOKEN = '339362662-rU6CizVcSZCr6CqWIhFh40yE0gmQdgusPRiwcpOj'
ACCESS_TOKEN_SECRET = 'CW9UCTOqYpzA1dS9doKcow6Bnz95UwZGBskcOsF2M6yIp'

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
BRAZIL_WOE_ID = 23424768

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
brazil_trends = twitter_api.trends.place(_id=BRAZIL_WOE_ID)

trends = json.loads(json.dumps(brazil_trends, indent=1))

for trend in trends[0]["trends"]:
	print (trend["name"]).strip("#")
