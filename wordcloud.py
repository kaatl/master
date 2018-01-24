#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt


def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      width=1500,
                      height=1000
                     ).generate(words)
    plt.figure(1,figsize=(8, 5))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


data = "I 2013 var det om lag 2,7 millioner yrkesaktive i Norge. Andelen av befolkningen i arbeidsstyrken er blant den høyeste i OECD-området, og den har økt fra 61 prosent i 1972 til 71 prosent i 2013. Norske yrkesaktive trives og er motivert på jobb, men det er ikke dermed sagt at alle har et fullt ut forsvarlig arbeidsmiljø i betydningen at de ikke utsettes for helseskadelige påvirkninger. I faktaboken gir vi kunnskap om status og trender for sentrale arbeidsrelaterte helseutfordringer, fordelt på yrke, næring, kjønn, alder og utdanning, med tilhørende relevante risikofaktorer med dokumentert betydning for arbeidshelsen. Selv om mange indikatorer viser at norske yrkesaktive har generelt gode arbeidsforhold og at utviklingen i norsk arbeidsmiljø går i positiv retning er det ikke slik at uheldige arbeidsforhold forsvinner fra norsk arbeidsliv, og vi ser også at det foreligger særlige utfordringer i enkelte yrker og næringer De største helseutfordringene i Norge både når det gjelder omfang og kostnader i form av redusert helse, sykefravær og uførhet er knyttet til muskel- og skjelettplager og psykiske helseplager. Seks av ti legemeldte sykefraværsdagsverk skyldes muskel- og skjelettplager og psykiske plager. Muskel- og skjelettplager er om lag like utbredt i dag som for tjue år siden og det er ingen holdepunkter for at forekomsten av psykiske plager og lidelser verken har avtatt eller økt i Norge i løpet av de siste tiårene. Nærmere halvparten av alle som rapporter om slike plager oppgir at plagene helt eller delvis skyldes jobben, og internasjonale og nyere norske studier viser at både psykososiale og mekaniske faktorer i arbeidsmiljøet spiller en vesentlige rolle. Selvrapporterte arbeidsrelatert luftveisplager er mindre utbredt enn for tjue år siden, men det er symptomer fra lunger og luftveier som oftest utredes ved de arbeidsmedisinske avdelingene i Norge. Beregninger viser at om lag 20 prosent av all lungekreft blant menn i Norge, og mellom 10 og 20 prosent av KOLS-tilfellene skyldes eksponeringer i arbeidet. Hudplager oppgis å være om lag like utbredt i dag som for tjue år siden mens arbeidsrelaterte plager avtar. Ser vi på utviklingstrekk i eksponeringen for hudirriterende stoffer de siste ti årene, er det ingen endring i andelen som oppgir hudkontakt med oljer /smøremidler eller hyppig kontakt med vann, mens eksponering for rengjøringsmidler/avfettingsmidler har avtatt. Selv om den totale eksponeringen for sterk støy er betydelig redusert de siste årene er det fortsatt slik at støyskader er den arbeidsrelaterte sykdommen som hyppigst blir meldt til Arbeidstilsynet. Arbeidsskader antas å utgjøre ca. 12 prosent av alle skadetilfeller i Norge, og det er særlig høy skaderisiko blant unge menn. Tallet på arbeidsskadedødsfall har gått betydelig ned i et lengre tidsperspektiv, men denne nedgangen ser ut til å ha flatet ut i løpet av det siste tiåret."

data = data.split()

stopwords_set = set(stopwords.words("norwegian"))

words = []
for w in data:
    if w not in stopwords_set:
        words.append(w)

wordcloud_draw(words, 'white')
