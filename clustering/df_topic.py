#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


import operator
import re
import pandas as pd

from nltk.stem.snowball import NorwegianStemmer

# CREDIT : https://github.com/EmilStenstrom/rippletagger
from rippletagger.tagger import Tagger


from nltk.tokenize import sent_tokenize

# df = pd.read_csv('thresh_1.3/cluster4.txt', sep="\t", header=0)
df = pd.read_csv('6_clusters/cluster_0.txt', sep="\t", header=0)
corpus = df['text'].values.tolist()

tagger = Tagger(language="no")
stemmer = NorwegianStemmer()


stopwords = []
with open('datasets/stopword.txt', 'r') as file: lines = file.readlines()
for x in lines: stopwords.append(str(x[:-1]).decode('utf-8'))



df_dict = {}

wordcloud_words = []
wordcloud_words_full = []

for doc in corpus:

    word_in_doc = []
    sentence_list = doc.decode('utf-8').split(".")
    # sentence_list = sent_tokenize(doc.decode('utf-8'))

    for sentence in sentence_list:
        sentence_pos = tagger.tag(sentence)

        for w in sentence_pos:
            #https://en.oxforddictionaries.com/grammar/word-classes-or-parts-of-speech
            if (w[1] != "PROPN") and (w[1] != "NOUN" ): continue
            # print (word[0])


            word = w[0]
            word = word.lower()
            word = re.sub(r'[.,=())—]','',word)

            # try:
            #     word = stemmer.stem(word)
            # except UnicodeDecodeError:
            #     message = "UnicodeDecodeError"

            # Ulykk => ulykke, korrupt? :D
            if word[-5:] == "ulykk":
                word += "e"

            wordcloud_words_full.append(word)

            if word in stopwords: continue # Hopp over hvis det er stoppord
            if word in word_in_doc: continue # Hopp over hvis den allerede er telt

            wordcloud_words.append(word)

            word_in_doc.append(word)

            if word in df_dict:
                df_dict[word] += 1
            else:
                df_dict[word] = 1

# for k, v in df_dict.items():
#     print(k,v)


sorted_dict = sorted(df_dict.items(), key=operator.itemgetter(1))

# for x in sorted_dict:
#
#     print(x[0].encode('utf-8'), x[1])

print()

top_three_terms = sorted_dict[-3:]

for x in top_three_terms:
    print (x[0], x[1])

# print (stemmer.stem("ulykke"))


"""
    WORDCLOUD
"""
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
def wordcloud_print():

    data = wordcloud_words # Document frequence
    # data = wordcloud_words_full # Term Frequency

    data = ' '.join(data)
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color='white',
                      width=1500,
                      height=1000
                     ).generate(data)
    plt.figure(1,figsize=(8, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

# wordcloud_print()

# print (tagger.tag("Dette skjedde på toget"))
