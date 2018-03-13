#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def read_glove_model(path):
    with open(path, 'r') as file:
        print "Reading '{}' ...".format(path)
        lines = file.readlines()

        word_vec = {}

        print "Loading file to dictionary ..."
        for line in lines:
            line = line.split()

            word = line[0]
            vec = line[1:]

            word_vec[word] = vec


            vec2 = []

            for i in vec:
                vec2.append(float(i))


            with open('glove_vectors.tsv', 'a') as file:
                file.write(word + '\t')
                for x in vec2:
                    file.write(str(x) + " ")

                file.write('\n')



        print "Done!\n"

    return word_vec

def read_glove_tsv(path):

    with open(path, 'r') as file:
        print "Reading '{}' ...".format(path)
        lines = file.readlines()

        word_vec = {}

        print "Loading file to dictionary ..."
        for line in lines:
            line = line.split('\t')

            word = line[0]
            vec = line[1].split()

            word_vec[word] = vec

        print "Done!\n"

    return word_vec


def get_v_for_w(model, word):
    return model.get(word)

def get_v_for_s(model, s):
    return [get_v_for_w(model, w) for w in s.lower().split()]

def read_dataset_to_glove(model):
    with open('trainingset.tsv', 'r') as file:
        lines = file.readlines()[1:]

        with open('trainingset_glove.tsv', 'a') as f:

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
                    except KeyError:
                        continue;

                    for dim in vec:
                        s += dim + " "
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

                s += "\t" + label

                f.write(s + "\n")







def glove_main():

    # glove_model = read_glove_model('models/glove_vec.txt') # 32285 words
    glove_model = read_glove_tsv('glove_vectors.tsv')
    read_dataset_to_glove(glove_model)

    # vec_for_s = get_v_for_s(glove_model, s) # Get vectors for sentence
    # return vec_for_s

glove_main()

# print test

# for t in test:
#     print t
#     print


# df = pd.read_csv('glove_vectors.csv')
#
# df['vectors'] = df['vectors'].apply(lambda x: [int(e) for e in x.split()])
# df = df.reindex(np.random.permutation(df.index))
