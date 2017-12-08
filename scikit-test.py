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

data = pd.read_csv('dataset/sentiment1.csv')
testData = pd.read_csv('dataset/sentiment1.csv')
train = data[['text','sentiment']]
test = testData[['text']]

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

training_set = nltk.classify.apply_features(extract_features,tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

test_sentence = """Bromwell High is a cartoon comedy. It ran at the same time as some other programs about school life, such as "Teachers". My 35 years in the teaching profession lead me to believe that Bromwell High's satire is much closer to reality than is "Teachers". The scramble to survive financially, the insightful students who can see right through their pathetic teachers' pomp, the pettiness of the whole situation, all remind me of the schools I knew and their students. When I saw the episode in which a student repeatedly tried to burn down the school, I immediately recalled ......... at .......... High. A classic line: INSPECTOR: I'm here to sack one of your teachers. STUDENT: Welcome to Bromwell High. I expect that many adults of my age think that Bromwell High is far fetched. What a pity that it isn't!"""
print classifier.classify(extract_features(test_sentence.split()))

#print classifier.classify(extract_features(test_sentence.split()))

#neg_cnt = []
#pos_cnt = []
#pos_cntS = 0
#pos_cntS = 0
#for obj in test_neg:
#    res =  classifier.classify(extract_features(obj.split()))
#    print res
#    if(res == 'Negative'):
#        neg_cnt.append(obj)
#for obj in test_pos:
#    res =  classifier.classify(extract_features(obj.split()))
#    print 'positive', res
#    if(res == 'Positive'):
#        pos_cnt.append(obj)
#print 'Negative', neg_cnt
#print 'Positive', pos_cnt

#print('[Negative]: %s/%s '  % (len(test_neg),neg_cnt))
#print('[Positive]: %s/%s '  % (len(test_pos),pos_cnt))

#def wordcloud_draw(data, color = 'black'):
#    words = ' '.join(data)
#    cleaned_word = " ".join([word for word in words.split()
#                            if 'http' not in word
#                                and not word.startswith('@')
#                                and not word.startswith('#')
#                                and word != 'RT'
#                            ])
#    wordcloud = WordCloud(stopwords=STOPWORDS,
#                      background_color=color,
#                      width=1500,
#                      height=1000
#                     ).generate(cleaned_word)
#    plt.figure(1,figsize=(13, 13))
#    plt.imshow(wordcloud)
#    plt.axis('off')
#    plt.show()

#print wordcloud_draw(w_features)

#print("Positive words")
#wordcloud_draw(train_pos,'white')
#print("Negative words")
#wordcloud_draw(train_neg)
