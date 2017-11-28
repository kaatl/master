#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Local files
from ner import runNer # Runs NLTK, Stanford, and Polyglot
from sanitize_data import sanitizeText # Santize unicode etc.
from tweepy_collect_data import collect_data # Collect twitterdata, tweepy


# Example of list the different methods uses:
# texts = [["This is a test for Trump", "This is a test for Trump!!!", "en"]] #Takes double list with [santized_text, original text, language]



# Collects data from Twitter, using the 100 most frequent Norwegian words and write to file
# collect_data()


# Sanitize a lists of tweets
# sanitizeText(texts)

# Run NLTK, Stanford, and Polyglot
# runNER(texts)
