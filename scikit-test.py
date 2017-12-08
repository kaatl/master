import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

import nltk
from nltk.tokenize import word_tokenize
from itertools import chain
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
#%matplotlib inline

from subprocess import check_output

data = pd.read_csv('dataset/sentiment1.csv')
testData = pd.read_csv('dataset/test.csv')
train = data[['text','sentiment']]
#test = testData[['text']]

# Splitting the dataset into train and test set
#train, test = train_test_split(data, testData)
# Removing neutral sentiments
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

#train_pos = train[ train['sentiment'] == 'Positive']
#train_pos = train_pos['text']
#train_neg = train[ train['sentiment'] == 'Negative']
#train_neg = train_neg['text']

#test_pos = test[ test['sentiment'] == 'Positive']
#test_pos = test['text']
#test_neg = test[ test['sentiment'] == 'Negative']
#test_neg = test['text']

# Extracting word features
def get_words_in_tweets(tweets):
    all = []
    for (words, sentiment) in tweets:
        #The method extend() appends the contents of seq to list.
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
        features[word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features,tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

test_sentence = "This is the worst band I've ever heard!"
#test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}

print classifier.classify(extract_features(test_sentence.split()))

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
