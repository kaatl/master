#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    CREDIT: https://github.com/facebookresearch/fastText
"""

import numpy as np
import time

def load_vector_model(path):
    with open(path, 'r') as file:
        print "Reading '{}' ...".format(path)
        lines = file.readlines()[1:]

        word_vec = {}

        print "Loading file to dictionary ..."
        for line in lines:
            line = line.split()

            word = line[0]
            vec = line[1:]

            vec2 = []
            for v in vec:
                vec2.append(float(v))
            # vec = line[1:]

            word_vec[line[0]] = vec2

            with open('fasttext_vectors.tsv', 'a') as file:
                file.write(word + '\t')
                for x in vec2:
                    file.write(str(x) + " ")

                file.write('\n')

        print "Done!\n"

    return word_vec


def fasttext_main():

    # s = 'arbeidsulykke'

    path = 'textrep_datasets/models/fasttext_no.vec' # https://github.com/facebookresearch/fastText
    model = load_vector_model(path) # Load model

fasttext_main()
