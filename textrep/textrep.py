#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def read_model_tsv(path):

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

def read_dataset_to_vector(model):
    # with open('trainingset.tsv', 'r') as file:
    with open('testset.tsv', 'r') as file:
        lines = file.readlines()[1:]

        # with open('trainingset_glove.tsv', 'a') as f:
        # with open('testset_glove.tsv', 'a') as f:
        # with open('trainingset_fasttext.tsv', 'a') as f:
        with open('testset_fasttext.tsv', 'a') as f:

            for line in lines:
                row = line.split('\t')

                if len(row) < 2:
                    print row
                    continue
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

    # vectors = 'textrep_datasets/models_tsv/fasttext_vectors.tsv'
    # vectors = 'textrep_datasets/models_tsv/glove_vectors.tsv'

    # model = read_model_tsv(vectors)
    model = gensim.models.Word2Vec.load('textrep_datasets/models/w2v/no.bin')

    read_dataset_to_vector(model)


glove_main()
