#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import numpy
sys.dont_write_bytecode = True # For å unngå .pyc metafiler

# Local files
from ner import runNER # Runs NLTK, Stanford, and Polyglot
from tweepy_collect_data import collect_data # Collect twitterdata, tweepy
from english_dataset_kaggle import english_dataset_main
from f1score import F1_score



# Collects Norwegian data  from Twitter, using the 100 most frequent Norwegian words and writes to file
# collect_data()

# Reads english dataset from kaggle
# texts = english_dataset_main()
# # Run NLTK, Stanford, and Polyglot
# english_ner_test = runNER(texts)# Ish 25 minutter



with open('dataset/ner_result.txt', 'r') as file:
    lines = file.readlines()
    nltk_scores, stanford_scores, polyglot_scores = [], [], []
    nltk_precision, stanford_precision, polyglot_precision = [], [], []
    nltk_recall, stanford_recall, polyglot_recall = [], [], []


    for line in lines:
        print line
        s_list = line.replace("[","").replace("]","").replace(" '", "").replace("'", "").replace("\n","").split(";")

        solution = s_list[1].split(",")
        nltk = s_list[2].split(",")
        stanford = s_list[3].split(",")
        polyglot = s_list[4].split(",")

        nltk_f1 = F1_score(solution, nltk)
        stanford_f1 = F1_score(solution, stanford)
        polyglot_f1 = F1_score(solution, polyglot)

        nltk_precision.append(nltk_f1[1])
        stanford_precision.append(stanford_f1[1])
        polyglot_precision.append(polyglot_f1[1])

        nltk_recall.append(nltk_f1[2])
        stanford_recall.append(stanford_f1[2])
        polyglot_recall.append(polyglot_f1[2])


        nltk_scores.append(nltk_f1[0])
        stanford_scores.append(nltk_f1[0])
        polyglot_scores.append(nltk_f1[0])
        print
        print

    # print average
    print "F1 Score"
    print "NLTK -", numpy.mean(nltk_scores)
    print "STANFORD -", numpy.mean(stanford_scores)
    print "POLYGLOT -", numpy.mean(polyglot_scores)
    print

    print "Precision"
    print "NLTK -", numpy.mean(nltk_precision)
    print "STANFORD -", numpy.mean(stanford_precision)
    print "POLYGLOT -", numpy.mean(polyglot_precision)
    print

    print "Recall"
    print "NLTK -", numpy.mean(nltk_recall)
    print "STANFORD -", numpy.mean(stanford_recall)
    print "POLYGLOT -", numpy.mean(polyglot_recall)



# s = """Sentence: 1415;[];[];[];[]"""
# s_list = s.replace("[","").replace("]","").replace(" '", "").split(";")
