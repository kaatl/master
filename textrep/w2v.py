#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    CREDIT: https://github.com/Kyubyong/wordvectors
"""

import gensim

def load_w2v_model_tsv():
    # Eventuelt KeyedVectors.load_word2vec_format('w2v_model')????
    model = gensim.models.Word2Vec.load('textrep_datasets/models/w2v/no.bin')

    with open('textrep_datasets/trainingset.tsv', 'r') as file:
    # with open('textrep_datasets/testset.tsv', 'r') as file:
        lines = file.readlines()[1:]

        with open('trainingset_w2v.tsv', 'a') as f:
        # with open('testset_w2v.tsv', 'a') as f:

            for line in lines:
                row = line.split('\t')

                input_text = row[0].split()
                input_label = row[1]

                s = ""

                for word in input_text:
                    word = word.replace(",", "")
                    word = word.replace("«", "")
                    word = word.replace("»", "")
                    word = word.replace(".", "")
                    word = word.replace(":", "")
                    word = word.replace(":", "")
                    word = word.replace("–", "")
                    word = word.replace("_", "")
                    word = word.replace("?", "")
                    word = word.replace("!", "")
                    word = word.replace("\n", "")

                    word = word.lower()

                    if (word == ""):
                        # print "word er en tom streng"
                        continue
                    try:
                        vec = model[word]

                        vec2 = []
                        for v in vec:
                            vec2.append(float(v))
                    except KeyError:
                        continue;

                    # print vec2[0]
                    for dim in vec2:
                        s += str(dim) + " "
                    s = s[:-1] # Ignore last space
                    s += ","

                label = ""
                s = s[:-1]
                if input_label.find("Ja"):
                    label = "1"
                elif input_label.find("Nei"):
                    label = "0"
                else:
                    print input_label

                if len(input_text) <= 1:
                    print input_text
                    print "HEIHEI"
                    s += "0.0"

                s += "\t" + label



                f.write(s + "\n")

load_w2v_model_tsv()

# Sources:
# https://radimrehurek.com/gensim/models/word2vec.html
# https://rare-technologies.com/word2vec-tutorial/


# 380 og 432
