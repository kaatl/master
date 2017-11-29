# -*- coding: utf-8 -*-
import pandas
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

stoppord = set(stopwords.words('norwegian'))

colnames = ['organisasjonsnummer','navn','stiftelsesdato','registreringsdatoEnhetsregisteret','organisasjonsform','hjemmeside','registrertIFrivillighetsregisteret','registrertIMvaregisteret','registrertIForetaksregisteret','registrertIStiftelsesregisteret','frivilligRegistrertIMvaregisteret','antallAnsatte','institusjonellSektorkode.kode','institusjonellSektorkode.beskrivelse','naeringskode1.kode','naeringskode1.beskrivelse','naeringskode2.kode','naeringskode2.beskrivelse','naeringskode3.kode',
'naeringskode3.beskrivelse','postadresse.adresse','postadresse.postnummer','postadresse.poststed','postadresse.kommunenummer','postadresse.kommune','postadresse.landkode','postadresse.land','forretningsadresse.adresse','forretningsadresse.postnummer','forretningsadresse.poststed','forretningsadresse.kommunenummer','forretningsadresse.kommune','forretningsadresse.landkode','forretningsadresse.land','sisteInnsendteAarsregnskap','konkurs','underAvvikling',
'underTvangsavviklingEllerTvangsopplosning','overordnetEnhet','målform','orgform.kode','orgform.beskrivelse']
data = pandas.read_csv('brreg1_utf8 (1).csv', sep=';', names=colnames, low_memory=False)
#Dette er gitt datasettet brreg1_utf8 (1).csv. Endres hvis annet datasett.

navn = data.navn.tolist()
ansatte = data.antallAnsatte.tolist()

setning = "Biltema er hos Åshild og er kjempe gøy"
setningListe = setning.split(' ')

removedStopwordsListe = setningListe[:] #lager en kopi av setningListe
for word in setningListe:
  if word in stoppord:
    removedStopwordsListe.remove(word)

print removedStopwordsListe

for index, x in enumerate(navn):
    for ord in removedStopwordsListe:
        match = re.search(r'\b'+ re.escape(ord) + r'\b',x,re.IGNORECASE)
        if match and int(ansatte[index]) < 1:
            print (x)
