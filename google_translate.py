#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored

from googletrans import Translator

translator = Translator()

def translateTweet(tweet):
    # TAR IKKE EMOJIIS
    try:
        return translator.translate(tweet, src='no', dest='en').text
    except ValueError:
        print colored("Mest sannsynelig en emojii i tekststrengen", 'red')


# tweets= [
#     "@AlexanderOsdal @LarsCBlast @carlarne1 @kkullebo Nei, jeg mener ikke det. Jeg mener bare at sammenhengen ikke finnes. Man kan ha suksess med, og uten, mange lokale spillere",
#     """Å revidere en bok innebærer at jeg møter meg selv i døren hele tiden" sier Vigdis...""",
#     "Leser du dette følger du meg allerede, men de andre på lista kan anbefales, selv om jeg kanskje ikke deler pol.ståsted. Skal sende epost til gamlelæreren &amp; fortelle hvilket celebert selskap klassens klovn har fått i denne tweeten. Lektor Dalens verden raser nok sammen kjapt",
#     "Jeg la til en video i en @YouTube-spilleliste –",
#     "@AlexanderOsdal @viks1981 @carlarne1 @kkullebo LAN utvikler ikke basen av talenter. Det har jeg sagt at han ikke skal ha ansvar for. Men LAN kvittet seg med Knudsen, Huse, Larsen, Hansson og flere. LAN hentet ikke Zachen, Glesnes m.fl. Det er objektive fakta. Det har han ansvar for.",
#     "@espenteigen @JuneLarsson @Rolf_k_y @frp_no @SVparti @Stortinget Da misforsto jeg, og da ser også min overnevnte tweet veldig feil ut.",
#     "@coys05091882 @OnkelErvin @GSkinnes @SV_Karin Det er vel derfor venstresida er venstresida: De har aldri brydd seg så mye om fakta. Kommer derfra selv, så jeg vet. Når man begynner å stille kritiske spørsmål til egne politiske oppfatninger, havner man fort mot høyre.",
#     """Her befinner jeg meg nok litt "midt på treet". Jeg kan ikke si meg HELT enig i alt Jan Schjetne kritiserer her,...""",
#     "@Ivarserdeg Om du ikke ser at det er en moralsk pekefinger som gir skylden til henne så er jeg veldig overrasket."
# ]

# with open('dataset/collected_data_twitter.txt', 'r') as f:
#     content = f.readlines()
#
#
# for tweet in content:
#     print tweet
#     translated_tweet = translateTweet(tweet)
#     print translated_tweet
#     print "-------"
#
#     try: translated_tweet = translated_tweet.encode("utf8")
#     except AttributeError: translated_tweet
#     with open('dataset/collected_data_twitter_english.txt', 'a') as file:
#         file.write(str(translated_tweet) + "\n")


print translateTweet("""Har feira vern av 10 unike skoger med Hans-Petter #Jacobsen i NRK p1+! Gikk du glipp av det hør det her, @VidarHelgesen """)
