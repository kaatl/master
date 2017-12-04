#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from sanitize_data import removeIllegalUnicode

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
def getTweets(query):
    # return api.home_timeline(tweet_mode = 'extended', count = 5) # Sample
    # return api.search(geocode = "59.911,10.757,1000km", rpp = 1000, tweet_mode = 'extended', lang="no") # Oslo
    # return api.search(q = "jobb", geocode = "63.446,10.421,50km", rpp = 100, tweet_mode = 'extended', lang="no") # Trondheim og query
    # return api.search(q = "og", rpp = 100, tweet_mode = 'extended', lang = "no") # Uten geolocation og med query
    return api.search(q = query, rpp = 100, tweet_mode = 'extended', lang = "no") # Uten geolocation og med query

def collect_data():
    # Most frequent words
    # https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Norwegian_Bokm%C3%A5l_wordlist
    common_words = ["jeg","det","er","du","ikke","en","og","har","vi","på","til","med","han","deg","for","meg","at","hva","den","så","som","kan","de","var","vil",
    "av","om","skal", "men", "et","her","ja","bare","må","hun","dere","noe","ham","dette","min","nei","nå","vet","kom","der","din","ut","hvor","da","fra",
    "oss","være","dem","se","ha","gjør","noen","hvis","ville","kommer","igjen", "ta","alle","hvorfor","få","tror","hvordan","går","alt","opp","sa","ingen","gå","når","får",
    "hvem","seg","gjøre","eller","la","ser","blir","takk","bli","hadde","bra","si","denne","henne","inn","litt","etter","kunne","vel","jo","to","skulle","ved","aldri","hei",
    "tilbake","over","kanskje","ble","hvad","god","man","også","selv","nok","sier","mig","før","ok","dig","hans","gi","sammen","godt","gang","ned","trenger","tar","mer","dag",
    "vært","mitt","mine","gjorde","mye","andre","sett","helt","vær","siden","hele","enn","år","ditt","komme","deres","mr","hold","af","mann","fordi","fikk","mot","dine","far",
    "mener","vent","faen","ting","tre","gjort","snakke","mange","greit","folk","hjem","liker","sant","tid","rett","dra","alltid","sir","sånn","lkke","unnskyld","morgen","bedre",
    "virkelig","elsker","tok","burde","vår","nu","hit","uten","veldig","død","finne","beklager","mor","står","livet","trodde","ingenting","snakker","sin","akkurat","gikk","kveld",
    "nej","samme","først","hør","kjenner",]

    f = open("dataset/collected_data_twitter.txt", "a")
    tweets_id = []
    print "Iterating through common words"
    for i in range(1): # index of the common words, får rate limit på 180 kall hvert 15 minutt. https://developer.twitter.com/en/docs/basics/rate-limiting
        print i, "Next word:", common_words[i]
        texts = getTweets(common_words[i])
        for text in texts:
            tweet_id = text.id_str
            if (not text.retweeted) and ('RT @' not in text.full_text) and (tweet_id not in tweets_id):
                tweets_id.append(tweet_id)
                tweet = text.full_text
                tweet = removeIllegalUnicode(tweet)
                f.write(tweet.encode('utf8') + "\n")

    f.close()

#collect_data()
