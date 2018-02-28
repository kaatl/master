import numpy as np
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

from subprocess import check_output

data = pd.read_csv('../dataset/imdb_sentiment.txt', sep=";;", engine = 'python')
# testData = pd.read_csv('dataset/sentiment1.csv')
train = data[['text','sentiment']]
# test = testData[['text']]

print train

# Fjerner alle noytrale tweets
train = train[train.sentiment != "Neutral"]

tweets = []
stopwords_set = set(stopwords.words("english"))

for index, row in train.iterrows():
    words_filtered = [e.lower() for e in row.text.split() if len(e) >= 3]
    words_cleaned = [word for word in words_filtered
        if 'http' not in word
        and not word.startswith('@')
        and not word.startswith('#')
        and word != 'RT']
    words_without_stopwords = [word for word in words_cleaned if not word in stopwords_set]
    tweets.append((words_cleaned,row.sentiment))

def get_words_in_tweets(tweets):
    all = []
    for (words, sentiment) in tweets:
        all.extend(words)
    return all

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    features = wordlist.keys()
    return features

w_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in w_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

print "trainingset"
training_set = nltk.classify.apply_features(extract_features,tweets)
print "classifier"
classifier = nltk.NaiveBayesClassifier.train(training_set)

print "Classify the sentences:"
test_sentence = """I hate you"""
print classifier.classify(extract_features(test_sentence.split()))
test_sentence = """I love you"""
print classifier.classify(extract_features(test_sentence.split()))
test_sentence = """You are not my best friend"""
print classifier.classify(extract_features(test_sentence.split()))

#print classifier.classify(extract_features(test_sentence.split()))
