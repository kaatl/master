#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def read_file(filename):

    data = json.load(open(filename))
    articles = data['Artikkel']

    for article in articles:
        title = article['name']
        text = ''
        url = article['url']

        if ('subtitle' in article):
            text = article['subtitle'] + ' '


        if 'artikkel' in article:
            paragraph = article['artikkel']

            for p in paragraph:
                text +=  p['paragraph'] + ' '
        elif 'paragraph' in article:
            text += article['paragraph']

        append_to_tsv(title, text, url)


def append_to_tsv(title, text, url):
    with open('webdocs_content.tsv', 'a') as file:
        file.write(title.encode('utf8') + '\t' +
                    text.encode('utf8') + '\t' +
                    url.encode('utf8') + '\n')


bergensTidende = 'bergesTidende_results.json'
stavangerAftenblad = 'stavangerAftenblad_resultat.json'
dagensNaeringsliv = 'dn_resultater.json'

read_file(stavangerAftenblad)


# Data gathered 23. januar - 25.januar ish
