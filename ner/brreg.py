#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from polyglot.text import Text

stoppord = set(stopwords.words('norwegian'))

path = 'ner_datasets/hovedenheter.310320181752.csv'
# path = 'brreg1.csv'

colnames = ['organisasjonsnummer','navn','stiftelsesdato','registreringsdatoEnhetsregisteret','organisasjonsform','hjemmeside','registrertIFrivillighetsregisteret','registrertIMvaregisteret','registrertIForetaksregisteret','registrertIStiftelsesregisteret','frivilligRegistrertIMvaregisteret','antallAnsatte','institusjonellSektorkode.kode','institusjonellSektorkode.beskrivelse','naeringskode1.kode','naeringskode1.beskrivelse','naeringskode2.kode','naeringskode2.beskrivelse','naeringskode3.kode',
'naeringskode3.beskrivelse','postadresse.adresse','postadresse.postnummer','postadresse.poststed','postadresse.kommunenummer','postadresse.kommune','postadresse.landkode','postadresse.land','forretningsadresse.adresse','forretningsadresse.postnummer','forretningsadresse.poststed','forretningsadresse.kommunenummer','forretningsadresse.kommune','forretningsadresse.landkode','forretningsadresse.land','sisteInnsendteAarsregnskap','konkurs','underAvvikling',
'underTvangsavviklingEllerTvangsopplosning','overordnetEnhet','målform','orgform.kode','orgform.beskrivelse']
data = pandas.read_csv(path, sep=';', names=colnames, low_memory=False)
#Dette er gitt datasettet brreg1_utf8 (1).csv. Endres hvis annet datasett.

navn = data.navn.tolist()
ansatte = data.antallAnsatte.tolist()


def getNERList(chunked):
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == nltk.tree.Tree:
            current_chunk.append(' '.join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = ' '.join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity.lower())
                current_chunk = []
        else:
            continue

    return continuous_chunk


def nltk_ner(sentence):
    tokens = nltk.word_tokenize(sentence)

    pos_tags = nltk.pos_tag(tokens)
    chunked = nltk.ne_chunk(pos_tags, binary=False)
    named_entities = getNERList(chunked)
    # print colored(named_entities, "green")
    print named_entities


# removedStopwordsListe = sentenceList[:] #lager en kopi av setningListe
# for word in sentenceList:
#     if word in stoppord:
#         removedStopwordsListe.remove(word)
#
# print removedStopwordsListe
#
# for index, x in enumerate(navn):
#     for ord in removedStopwordsListe:
#
#
#
#         match = re.search(r'\b'+ re.escape(ord) + r'\b', x, re.IGNORECASE)
#         # if match and int(ansatte[index]) < 1:
#         if match:
#             print (x)
sentences = [
    "The name of the deceased in the accident at Maerks Interceptor is released. It was Freddy Olsen (43) from Arendal who died in the accident at Maersk Interceptor on Thursday, December 7, 2017.",
    "Killengreen claimed he had many stakeholders among developers who were willing to pay a high price for the residence. They agreed that he could buy the house in the attractive area of Nordberg in Oslo for NOK 10.5 million.",
    "Arvid Dahm believes Killengreen broke good brokerage when he advised selling to a buyer directly for 10.5 million. Real Estate Agent Jens Christian Killengreen does not want to comment on the matter before it is dealt with by the district court, but writes the following in an email to NRK: 'We do not know either",
    "Rica Hell Hotel is housed for 100 million.",
    "A man was transported to Ullevål hospital with a clamp injury after a work injury at the Loe concrete factory in Nedre Eiker. The Labor Inspectorate was notified of the incident.",
    "Bypassed after driving dumps with defective brakes. An appeal has been made against two persons in Grunn og Fjellentreprenøren AS for several violations of the Working Environment Act and regulations for this after 20-year-old Mathias Fors Olsen died of a work injury at E16 at Filefjell in November 2012.",
    "Work Accident. A 58-year-old man lost several fingers in a work injury at Partnertech. Both little accident happened at Solgaard Forest 17.09. by 12 o'clock when the man was to cut metal with a belt saw",
    "It sparkled around the strike at the Bobbos kiosk in Tromsø when the police officer was reported to have threatened one of the strike guards with violence. On Saturday the level of conflict between employees and bosses reached a new peak.",
    "Eight minutes to toilet visits. DNB's subsidiary DNB Liv puts new record in the monitoring of employees.",
    "Work accident at Elkem. A person died in a work accident at Elkem Thamshavn's silicon factory at Orkanger, informs the company. Three others must be injured.",
    "Danger of occupational injury. A Polish man in his 40s died while working on a platform in Ølensvåg in Vindafjord municipality in Rogaland. The helmet under the arm The man dropped a hoax hunt while working on a platform at the Westcon Yard farm in Ølensvåg, the police reported.",
    "Lost life in an occupational accident. A man died after a work injury at the box factory Styro Nor in Tana.",
    "Warned about illegal Adecco relationship a year ago. Following the disclosure that illegal accommodation in the basement of a nursing home in Moss has been committed and that employees have also worked overtime without getting overtime pay, questions were asked about the municipality's warning routines in the city council.",
    "Do they violate the Working Environment Act? The joint association suspects that the concrete contractor Brødrene Vangstad AS, which builds a rock hotel in Namsos, uses its foreign labor in violation of the Working Environment Act.",
    "Record record for TV 2. The background is an occupational accident last summer, where an employee was injured during the recording of a promo video on the TV 2 house in Bergen.",
    "Central to Network Company Without Employees and Content 'Earned' 40 Million in 17 Months One of the biggest accusations concerns the so-called Zvonko Network, where there has been money laundering of more than 40 million after the proprietor disappeared from Norway. Accordingly, the charge has Active Templates Service white washed close to NOK 16 million via",
    "Here is a report from Kosovo, which shows the family values: Bankruptcy in Norway, Kosmos kitchens The targeted painter company was subcontractor One of the companies belonging to the family, Saba Malerservice AS, was hired as a subcontractor during the renovation at Eidsvoll. The company was charged in May this year, linked to money laundering and helmets",
    "The German woman started a business in Norway to wash black money for companies that painted housing companies and washed at Hard Rock Cafe. The 62-year-old wanted her to wash money for several companies. 'But they were not serious,' said 36-year-old in court.",
    "Alliero received the contract on behalf of Schibsted Eiendom when Aftenposten's premises in Akersgata 55 were refurbished, and it was Alliero who hired the sole proprietor Bon Bygg. Very regrettable and found that a company suspected of crime has been used in our premises; says Rikter.",
    "Gjenganger In 2010, Malmester Harald Askautrud was involved in a social dumping case with the same actors who run Ås carpentry and painting service, Frank Remi Wang and Arvydas Danilevicius. In the afternoon on Sunday afternoon Bergstrøm says in an email: 'After we had been informed by Aftenposten of possible breach of'",
    "Police: How criminal networks work in the painter industry Claims he's cheated The accused 30-year-old, whom the prosecution believes is a spider, admits that there has been black work, but he claims he did not know it. The witness denounces a verdict for Heleri, and confirms that cash he raised for Zvonko Bygg",
    "No longer allowed to move trains or work machines on the skins themselves, after the Norwegian Railway Inspectorate has revealed 24 security deficiencies at the company. Kraaka1 The Baneservice company, which builds and maintains the railway, is no longer allowed to drive a single carriage.",
    "Bankruptcy in Norway, cakes in Kosovo Confirming Police Report One of the brothers, Isa Gerbeshi, was considered a real driver of Wara Malerservice. 'This is not the first time we hear about layoffs of this kind of thing.",
    "It is the Ministry of Defense, the responsible commissioner for the cleaners. 'Defense Buildings know that there have been challenges, and we are in dialogue with both the Abo Clean and the Ministry of Defense to solve these,'' says Arve Rosland, Communications Adviser in Defense Agency for the newspaper.",
    "On the same day as the last check takes place, Linstow confirms the check of September 2: - None of these were directly employed by the Fund, but six of them were employed by subcontractors of the Fund. Lotila has long spell as a business journalist in Estonia, and believes it is naive to believe this",
    "The Petroleum Safety Authority Norway, PSA, has given Aibel AS and Norisol Norge AS notice of order following an audit where the management of the working environment in relation to particularly risky groups was the target of the survey. Aibel was the main supervisor in the audit, but Statoil as operator and Aibel's subcontractor Norisol were also involved.",
    "LO reports Norsk Helsepersonell AS and four municipalities in Rogaland and Hordaland for slave labor and traffic. Now it is important to ensure that helpers from Ukraine do not travel home.",
    "Nurses received 100 kroner the day. Ukrainian nurses have been working for hundreds of dollars in the municipality of Karmoy since November last year, via the recruitment company 'Norsk Helsepersonell AS'.",
    "Got doors over them. A 19 year old was injured in a work accident at Nor-Dan in Egersund. - During the packing of doors at the Nor-Dance facility in Egersund, 19-year-olds received more of their doors.",
    "'We in the Commonwealth are pleased that this accident did not take life or lead to personal injuries. He has previously criticized StatoilHydro for the use of night work on the relevant work operation that triggered leakage on Statfjord A.",
    "In Kosovo, the big brother expelled from Norway in 2008 with a false ID has become rich in record time. According to the police, Kosovo striker Shkelzen Shala and his company Aktiv Maler Service AS have had a 40 million turnover over four years. In Drenas is one of several stores in the Active chain",
    "About the sights in Select Bygg and Active Templates Service, Bergstrøm says: 'What they are aiming for is far from what we want to stand for. They emphasize that they have only paid for work done.",
    "Used by all major All the four largest construction companies in Norway, Veidekke, Skanska, AF Group and NCC Construction AS have used Malerservice Norge AS as subcontractor for the last ten years. Police Attorney Andreas Meeg-Bentzen says that this case is the hitherto biggest case related to the organization of black and illegal",
    "The two believe this is a conscious pressure on prices from the contractor and that the AF Group is not alone in acting like this. Entrepreneurs are keen on price.",
    "Gigantbot. Stangeland Machine has been charged NOK 4 million after a work accident in Risavika almost two years ago.",
    "Cut the pulmonary veins. A 39-year-old man cut his pulmonary vein in an occupational accident at Spangereid. Hjelm 2 The man, who according to fvn.no is employed by Repstad Anlegg, cut his wrist with a knife working in a ditch at Høllen at Spangereid.",
    "Poor working environment in Norwegian Church Aid. Church Aid employees have been exposed to acts they perceive as deeply offensive.",
    "Kavli has to pay 1 million kroner for a breach of the Working Environment Act after a fatal accident at the factory in Bergen last March. Constitutional lawyer Arild Oma believes the palletizing machine was not well secured.",
    "Nurses received 100 kroner the day. Ukrainian nurses have been working for hundreds of dollars in the municipality of Karmøy since November last year, via the recruitment company 'Norsk Helsepersonell AS'.",
    "No control over heavy metal-leakage. SFT: - It is surprising that Hydro has not corrected deficiencies.",
    "Ten employees at Kafe Mirakel in Drammen lend a quarter of salary to the employer. Now the owner of Kafe Mirakel, Jan Martin Nilsen, has asked the employees to sacrifice.",
    "In the course of a year, four employees at Mortens Kro will have worked 1,686 overtime hours. According to the accusation of the Romerike police chief, the worst relationship is about a female employee who worked 582.5 hours beyond normal working hours in a year.",
    "Read also: The Renovation Manager in Oslo goes by Rødt requires the Oslo City Council to terminate the contract with the renovation company Veireno and threatens to distrust. 'The contract clearly states that breach of the terms of pay and working conditions gives the contracting authority the right to cancel the contract - even if the supplier corrects the situation,'' says Bjørnar Moxnes, chairman of the Red Cross.",
    "The Petroleum Safety Authority Norway has notified the drilling company North Atlantic Drilling of orders, after a survey on the West Phoenix rig revealed a number of deviations. The PSA also warns that North Atlantic will be required to take action so that the results and learning of this order will also apply to other company rigs that",
    "Professional federations believe Subsea7 violates the law. The dive contracts under which Subsea7 operates, violates the Working Environment Act, believes Industry Energy, the Federation calls the Petroleum Safety Authority Norway to clean up",
    "Appeals and culprits after death sucks. Daily Leiar and Chairman of Tunnelservice AS has been charged with the death penalty in Køsnesfjorden power plant in 2009.",
    "Pure madness in downtown Oslo. The cleaner from the company Gold Clean washed windows unsecured 12 meters above the ground.",
    "A spark from disaster. Several nuclear disasters at Gullfaks show that Statoil has not taken the security seriously, writes editor-in-chief Tormod Haugstad in Technical Weekly Bulletin.",
    "Two companies in Mo i Rana are fined with a total of 800 000, and a replacement of 300 000, after a construction worker died in an occupational accident. Ruukki Profiler has a fine of 500,000 kroner while Momek Service has been charged a fine of 300,000 kroner for breach of provisions",
    "Thumbs off. A 59-year-old man was injured in a work accident at Moelven Limtre AS and drove to Lillehammer Hospital for treatment.",
    "Got soil over it. A man in the 50's died in a work accident at Rykkin in Bærum Gravemaskingrabb 1 The man dug a drainage trench when he got earthquakes over him.",
]


# nltk(sentence)

for sentence in sentences:
    print sentence
    nltk_ner(sentence)
    print
