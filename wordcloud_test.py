#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from rippletagger.tagger import Tagger
tagger = Tagger(language="no")


import pandas as pd

df = pd.read_csv('clustering/thresh_1.3/cluster4.txt', sep="\t", header=0)

stopwords = []
with open('clustering/stopword.txt', 'r') as file: lines = file.readlines()
for x in lines: stopwords.append(str(x[:-1]))

def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=1500,
                      height=1000
                     ).generate(words)
    plt.figure(1,figsize=(8, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()




# data = data.split()
data_list = df['text'].values.tolist()
data = ""
for d in data_list:
    data += d

data = data.split(".")
words = []

for sent in data:
    pos_sent = tagger.tag(sent)

    for word in pos_sent:
        if word[1] == "NOUN":
            if word[0] in stopwords: continue

            words.append(word[0])



wordcloud_draw(words, 'white')


for doc in data_list:
