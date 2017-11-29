import csv

english_ner_dataset = {}
ner_tags = ['geo', 'org', 'per', 'gpe']

current_key = ""
with file('dataset/ner_dataset.csv') as f:
    reader = csv.reader(f, delimiter='|')
    for line in reader:
        line = line[0].split(';')
        # print(line)
        # print(line[0], line[1], line[2], line[3], current_key)
        if ("Sentence" in line[0]):
            current_key = line[0]
            english_ner_dataset[current_key] = [[line[1], line[2], line[3]]]
        else:
            english_ner_dataset[current_key].append([line[1], line[2], line[3]])

# for k,v in english_ner_dataset.iteritems():
#     print k, v
#     print

def makeSentenceFromDict(dict):
    texts = []
    for key, value in english_ner_dataset.iteritems():
        s = ''
        named_entities = findNamedEntitiesInValue(value)

        for v in value:
            word = v[0]
            tag = v[2]
            # Concatinate words to a sentence:
            if len(word) > 0:
                s = s[0:-1] + word + " " if word[0] in ".,'" else s + word + " "

        #key, sentence, list of named entities
        texts.append([key, s, named_entities])

    print texts[0]
    return texts

def findNamedEntitiesInValue(value):
    named_entity = ""
    named_entities = []

    for v in value:
        word = v[0]
        tag = v[2]

        if tag[-3:] in ner_tags:
            if tag[0] == 'B': # B for beginning of named entity, I if a part of previous word.
                if len(named_entity):
                    named_entities.append(named_entity)
                named_entity = word
            else:
                named_entity += " " + word

    if len(named_entity):
        named_entities.append(named_entity)

    return named_entities





makeSentenceFromDict(english_ner_dataset)
print findNamedEntitiesInValue(english_ner_dataset["Sentence: 1"])


# geo = Geographical Entity
# org = Organization
# per = Person
# gpe = Geopolitical Entity
