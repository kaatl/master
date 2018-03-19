#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    CREDIT: https://github.com/stanfordnlp/GloVe
"""

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
            # with open('glove_vectors_test.tsv', 'a') as file:
                file.write(word + '\t')
                for x in vec2:
                    file.write(str(x) + " ")

                file.write('\n')



        print "Done!\n"

    return word_vec


glove_model = read_glove_model('textrep_datasets/models/glove_vec.txt') # 32285 words
