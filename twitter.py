#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import re
from termcolor import colored
import nltk
from polyglot.text import Text

# Local files
from ner import ner_main

# ===== KEYS =====
consumer_key = 'vORyHnmDqljgnzC0AakEpdrSb'
consumer_secret = 'cVAZHQjnd5mtYg3HP6TRoW2Ly0zfOZoZccLPtLF4rEIu7BCsK4'
access_token = '4745335103-g9wsWOWsxS2AzkTVQNPiH3t9CsUcCu1yCjgr95u'
access_token_secret = 'Pu4ZNFVefu5itcS15UW2QEPARoZsNBkFUpCZltAz7ZUt1'

# ===== AUTH =====
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ===== TWEETS ====
def getTweets():
    return api.home_timeline(tweet_mode = 'extended', count = 5) # Sample

# ==== SANITIZING ====
def sanitizeText(tweets):
    texts = []
    for tweet in tweets:
        # if (not tweet.retweeted) and ('RT @' not in tweet.full_text): # and (tweet.lang == "no"):
        text = tweet.full_text
        text = removeIllegalUnicode(text)
        texts.append([str(text), tweet.full_text, tweet.lang])

    return texts

def removeIllegalUnicode(text):

    # Fjerner nordiske chars (nltk klarer ikke å ha æøå)
    # text = re.sub(u'(\u00C6|\u00E6)', 'ae', text)
    # text = re.sub(u'(\u00C5|\u00E5)', 'aa', text)
    # text = re.sub(u'(\u00D8|\u00F8)', 'oe', text)

    # Tar bort url på slutten av setningen, bare for å gjøre det enkelt nå i starten
    urlIndex = text.find('http')
    if urlIndex != -1:
        text = text[0:urlIndex]


    text = re.sub(u"(\u2018|\u2019)", "'", text) # Erstatter fnutter til å bare bruke ', og ikke ´` osv.
    text = re.sub(u"(\u201c|\u201d)", "'", text) # Få bort dobbelfnutt
    text = re.sub(u"(\u00F1)", "n", text) # Fjerner tilde
    text = re.sub(u"(\u00E9)", "e", text) # Fjerner é
    text = re.sub(u"(\u2014)", "", text) # Fjerner dash
    text = re.sub(u"(\u2026)", "", text) # Ellipsis


    # Fjerne emojiis unicode
    emoji_pattern = re.compile(
        u'(\ud83d[\ude00-\ude4f])|'  # emoticons
        u'(\ud83c[\udf00-\uffff])|'  # symbols & pictographs (1 of 2)
        u'(\ud83d[\u0000-\uddff])|'  # symbols & pictographs (2 of 2)
        u'(\ud83d[\ude80-\udeff])|'  # transport & map symbols
        u'(\ud83c[\udde0-\uddff])|'
        u'(\u2728)'  # flags (iOS)
        '+',
        flags=re.UNICODE
    )
    text = ' '.join([re.sub(emoji_pattern, '', w) for w in text.split()])

    return text

ner_main([["This is a test for Trump", "This is a test for Trump!!!", "en"]]) #Takes double list with [santized_text, original text, language]
