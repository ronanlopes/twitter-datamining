# -*- coding: utf-8 -*-

import sys
import tweepy
import twitter
import json
import twitter
import types
import funcoestwitter

twitter_api = funcoestwitter.autenticar()

resultados=funcoestwitter.get_user_profile(twitter_api, screen_names=sys.argv[1:])

