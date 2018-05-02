#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
import numpy as np
import re

corpus = ["Men på vårt spørsmål om det er tariffavtale i bedriften svarer Ørbeck at det er det ikke. – Vi skulle ønske at arbeidsmiljølovens hovedkrav ble oppfylt, at det bare var faste ansettelser, men når arbeidsmiljøloven åpner for innleie kan ikke vi gjøre noe med det, sier sjefingeniør i DSB, Runar",
"Alt ser fint ut Gansmo sier hun forstår at det kan virke urettferdig at det er løpeguttene som blir dømt til fengselsstraffer, mens de som styrer virksomheten går fri. Inntjeningen er høyere for alle siden hele kontraktskjeden er basert på svart arbeid i bunnen, og gevinsten øker i større nettverk.",
"— Ja, det brer om seg, og min bekymring er at sosial dumping skal spre seg til vanlige, seriøse norske bedrifter fordi de presses på pris, sier Støstad, som nå jobber i LO. Vi i Oslo kommune er opptatt av å bidra til ryddige forhold i bransjen, derfor gjør vi"]

# Read stopword list
stoppord = []
with open('stopword.txt', 'r') as file: lines = file.readlines()
for x in lines:
    stoppord.append(str(x[:-1]))


# Fjerner tegn og stoppord
corpus_trimmed = []
for c in corpus:
    s = ""
    c_split = c.split()
    for w in c_split:
        w = re.sub(r'[.,=())-]','',w)
        if w.lower() not in stoppord:
            s += w + " "

    corpus_trimmed.append(s)


# Creates vectorized TFIDF
vectorizer = TfidfVectorizer()
txt_fitted = vectorizer.fit(corpus_trimmed)
X = vectorizer.fit_transform(corpus_trimmed)
feature_names = txt_fitted.get_feature_names()



# Creates list of word with tfidf score
for doc in range(len(corpus_trimmed)):
    feature_index = X[doc,:].nonzero()[1]
    tfidf_scores = zip(feature_index, [X[doc, x] for x in feature_index])
    tfidf_scores.sort()

    for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
        print w, s

    print
