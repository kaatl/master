#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import re
from termcolor import colored
import nltk
from polyglot.text import Text

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
    return api.home_timeline(tweet_mode = 'extended', count = 5)

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
    # Det går ikke an å strippe bort "-" hvis det er mellomrom på begge sider. Eks. "Her har du - et eksempel"
    # text = ' '.join([w.replace('-', ' ') for w in text.split()])

    # Fjerner punctuation, usikker på om vi må gjøre dette "manuelt"
    # text = " ".join([w.strip(',."$?!:;-') for w in text.split()])

    # Fjerner nordiske chars (nltk klarer ikke å ha æøå)
    text = re.sub(u'(\u00C6|\u00E6)', 'ae', text)
    text = re.sub(u'(\u00C5|\u00E5)', 'aa', text)
    text = re.sub(u'(\u00D8|\u00F8)', 'oe', text)

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


# ==================== NLTK ========================
def nltkNER(sentence):
    print colored('\n========NLTK=======', 'blue')
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    chunked = nltk.ne_chunk(pos_tags, binary=False)
    print getNERList(chunked), '\n'

# Returnerer en liste med Named Entities fra en tweet (for nltk)
def getNERList(chunked):
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == nltk.tree.Tree:
            current_chunk.append(' '.join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = ' '.join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk

# ==================== Polyglot ========================
def polyglotNER(sentence):
    print colored('\n\n========POLYGLOT========\n', 'blue')
    print sentence, '\n'
    text = Text(sentence, hint_language_code='no')

    for entity in text.entities:
        print entity.tag, entity

tweets = getTweets()
texts = sanitizeText(tweets)

for text in texts:
    print colored("\n=================NEW TWEET=================\n", 'cyan')
    print text[1]
    if (text[2] == 'en'):
        nltkNER(text[0])
    else:
        polyglotNER(text[0])
