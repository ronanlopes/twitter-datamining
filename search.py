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

#XX: Set this variable to a trending topic, 
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.

q = 'UFSJ' 

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']


# Iterate through 5 more batches of results by following the cursor

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # No more results when next_results doesn't exist
        break
        
    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
resultados = json.loads(json.dumps(statuses, indent=1))
for resultado in resultados:
	print resultado["user"]["name"],": ",resultado["text"],"\n"
