#!/usr/bin/env python
# -*- coding: utf-8 -*-
from summa import summarizer


testText= "McDonald's gjør stadig endringer. Tidligere i år ble det kjent at burgergiganten setter nytt miljømål ved å endre emballasjen. Nå er det sunnhet som er i fokus. Målet er at minst halvparten eller mer av Happy Meal-menyalternativene i 120 av de internasjonale markedene skal inneholde 600 kalorier. Kun ti prosent av kaloriene skal komme fra mettet fett og ikke mer enn ti prosent av kaloriene skal inneholde tilsatt sukker. McDonald’s har tidligere prøvd andre grep for å gjøre barnemenyen litt sunnere, som å tilby juice i stedet for brus og frukt og grønnsaker i stedet for pommes frites. For å nå burgerkjedens nye målsetninger skal de blant annet fjerne cheeseburgeren fra den faste barnemenyen i USA. Amerikanske familier vil se endringene allerede i år; fra og med juni kan kundene velge mellom vanlig hamburger eller chicken nuggets som standardvalg i barnemenyen. Kristoffersen ledet med 0,21 sekunder på André Myhrer (35) etter første omgang."


def getSummary(text):
    print summarizer.summarize(text, words=30, language="norwegian")


getSummary(testText)
