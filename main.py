#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True # For å unngå .pyc metafiler

# Local files
from ner import runNER # Runs NLTK, Stanford, and Polyglot
from tweepy_collect_data import collect_data # Collect twitterdata, tweepy


# Example of list the different methods uses, a double list with [[santized_text, original text, language]]
texts = [["Daughter of Apple engineer says her father was fired after she posted video of iPhone X", "Daughter of Apple engineer says her father was fired after she posted video of iPhone X!!", "en"]] 



# Collects data from Twitter, using the 100 most frequent Norwegian words and write to file
# collect_data()

# Run NLTK, Stanford, and Polyglot
runNER(texts)
