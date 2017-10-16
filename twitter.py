import tweepy
import nltk

# KEYS
consumer_key = 'vORyHnmDqljgnzC0AakEpdrSb'
consumer_secret = 'cVAZHQjnd5mtYg3HP6TRoW2Ly0zfOZoZccLPtLF4rEIu7BCsK4'
access_token = '4745335103-g9wsWOWsxS2AzkTVQNPiH3t9CsUcCu1yCjgr95u'
access_token_secret = 'Pu4ZNFVefu5itcS15UW2QEPARoZsNBkFUpCZltAz7ZUt1'

# AUTH
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# TWEETS
def getTweets():
    tweets = api.home_timeline(count = 100)

    for tweet in tweets:
        if (not tweet.retweeted) and ('RT @' not in tweet.text) and (tweet.lang == "no"):
            print tweet.text
            print

# NAMED ENTITY RECOGNITION
def NER(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    print nltk.ne_chunk(pos_tags, binary=False)


sentence = "Let's meet tomorrow at Biltema";
#tweets = getTweets()
NER(sentence)
# http://nishutayaltech.blogspot.no/2015/02/penn-treebank-pos-tags-in-natural.html
