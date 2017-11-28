#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

# ===== KEYS =====
consumer_key = 'vORyHnmDqljgnzC0AakEpdrSb'
consumer_secret = 'cVAZHQjnd5mtYg3HP6TRoW2Ly0zfOZoZccLPtLF4rEIu7BCsK4'
access_token = '4745335103-g9wsWOWsxS2AzkTVQNPiH3t9CsUcCu1yCjgr95u'
access_token_secret = 'Pu4ZNFVefu5itcS15UW2QEPARoZsNBkFUpCZltAz7ZUt1'

# ===== AUTH =====
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track=['hei'], languages=["no"])
