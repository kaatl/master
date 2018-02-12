#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gensim

def w2v(sentences):
    model = gensim.models.Word2Vec(sentences, size=300, min_count=1, sg=1) #sg=1 er cbow, uten er det skip-gram. Skip-gram funker best på lite treningsdata.

    # model = gensim.models.Word2Vec(min_count=1)
    # model.build_vocab(sentences_list)
    # model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)

    print model
    # print model['bra']



def save_w2v_model(model):
    model.save('w2v_model')

def load_w2v_model():
    # Eventuelt KeyedVectors.load_word2vec_format('w2v_model')????
    return gensim.models.Word2Vec.load('w2v_model')


def load_training_data():
    with open('../web_docs/webdocs_content.tsv', 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            line_list = line.split('.')

            for sentence in line_list:
                words = sentence.split()
                data.append(words)

        return data

data = load_training_data()
w2v(data)

# Sources:
# https://radimrehurek.com/gensim/models/word2vec.html
# https://rare-technologies.com/word2vec-tutorial/
