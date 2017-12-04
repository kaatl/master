#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import sys
sys.dont_write_bytecode = True # For å unngå .pyc metafiler

# Local files
from ner import runNER # Runs NLTK, Stanford, and Polyglot
from tweepy_collect_data import collect_data # Collect twitterdata, tweepy
from english_dataset_kaggle import english_dataset_main
from f1score.py import F1_score



# Collects data from Twitter, using the 100 most frequent Norwegian words and writes to file
# collect_data()

# Reads english dataset from kaggle
texts = english_dataset_main()

# Run NLTK, Stanford, and Polyglot
start = timeit.timeit()
runNER(texts)
end = timeit.timeit()

# Prints elapsed time
print "Time: ", (end-start)
