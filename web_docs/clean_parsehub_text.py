#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def read_file(filename):

    data = json.load(open(filename))
    articles = data['articles']

    for article in articles:
        title = article['title']
        text = ''
        url = article['url']

        if ('subtitle' in article):
            text = article['subtitle'] + ' '


        if 'paragraph' in article:
            paragraph = article['paragraph']

            for p in paragraph:
                text +=  p['text'] + ' '
        elif 'text' in article:
            text += article['text']

        append_to_tsv(title, text, url)


def append_to_tsv(title, text, url):
    with open('webdocs_content.tsv', 'a') as file:
        file.write(title.encode('utf8') + '\t' +
                    text.encode('utf8') + '\t' +
                    url.encode('utf8') + '\n')


aftenposten = 'parsehub_aftenposten_92.json'
nrk = 'parsehub_nrk_63.json'
nrk_dok = 'parsehub_nrkdok_93.json'
politiet = 'parsehub_politiet_150.json'
politilogg = 'parsehub_politilogg_72.json'

# read_file(politilogg)


# Data gathered 23. januar - 25.januar ish
