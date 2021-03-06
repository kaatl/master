import nltk
from pycorenlp import StanfordCoreNLP
from polyglot.text import Text

from termcolor import colored


"""
***** NLTK *****
"""

def nltkNER(sentence):
    # print colored('========NLTK=======\n', 'blue')
    # print sentence
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    chunked = nltk.ne_chunk(pos_tags, binary=False)
    named_entities = getNERList(chunked)
    # print colored(named_entities, "green")
    return named_entities

# Returnerer en liste med Named Entities fra en tweet (for nltk)
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

    # for chunk in chunked:
    #     if hasattr(chunk, 'label'):
    #         print(chunk.label(), ' '.join(c[0] for c in chunk))
    # print
    return continuous_chunk

"""
***** STANFORD CORENLP *****
"""
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
nlp = StanfordCoreNLP('http://localhost:9000')
error_sentences = []

def stanfordCoreNLPNER(sentence, sentence_id):
    lang = 'en'
    # print colored('\n=========Stanford CoreNLP======\n', 'blue')
    # print sentence
    if (lang == 'en'):
        try:
            output = nlp.annotate(sentence, properties={
                # 'annotators': 'tokenize,ssplit,pos,depparse,parse',
                'annotators': 'ner',
                'outputFormat': 'json'
            })

            # print(output['sentences'][0]['parse'])
            named_entities = getCoreNLPList(output['sentences'][0]['tokens'])
            # print colored(named_entities, "green")
            return named_entities
        except UnicodeDecodeError:
            error_sentences.append(sentence_id)

def getCoreNLPList(tokens):
    named_entities = []
    token_count = 0
    for i in range(len(tokens)):
        if token_count < len(tokens):
            named_entity = ''
            token = tokens[token_count]
            if token['ner'] == 'PERSON' or token['ner'] == 'ORGANIZATION' or token['ner'] == 'LOCATION':
                named_entity += token['ner'] + ',' + token['word'].lower()
                checking = True
                while checking == True:
                    if token_count + 1 < len(tokens):
                        if tokens[token_count + 1]['ner'] == 'PERSON' or tokens[token_count + 1]['ner'] == 'ORGANIZATION' or tokens[token_count + 1]['ner'] == 'LOCATION':
                            token_count += 1
                            named_entity += ' {}'.format(tokens[token_count]['word'].lower())
                        else:
                            checking = False
                            token_count += 1
                    else:
                        checking = False
                        token_count += 1
            else:
                token_count += 1
            if named_entity != '':
                named_entity = named_entity.split(',')
                named_entities.append(named_entity[1].encode("utf8"))
    return named_entities



"""
***** POLYGLOT *****
"""

def polyglotNER(sentence, sentence_id):
    # print colored('\n========POLYGLOT========\n', 'blue')
    # print sentence
    # text = Text(sentence, hint_language_code='no')
    try:
        text = Text(sentence, hint_language_code='en')
        named_entities = []
        for entity in text.entities:
            # print entity.tag, entity
            # print entity[0] + " " + entity[1]
            name = " ".join(n.encode("utf8") for n in entity)
            named_entities.append(name.lower())

        # print colored(named_entities, "green")
        return named_entities
    except UnicodeDecodeError, UnboundLocalError:
        error_sentences.append(sentence_id)


import json


import time
import sys
import numpy
sys.dont_write_bytecode = True # For å unngå .pyc metafiler
def runNER(texts):
    for t in texts:
        named_entities = {}
        text = t[1]
        print t[0]
        # print colored('\n\n\n\n NEW TWEET \n\n', 'green')
        # print '\n', t[0], '\n', colored(text, 'cyan')
        # print t[2], '\n'
        nltk = nltkNER(text)
        stanford = stanfordCoreNLPNER(text, t[0])
        polyglot = polyglotNER(text, t[0])

        named_entities['solution'] = t[2]
        named_entities['nltk'] = nltk
        named_entities['stanford'] = stanford
        named_entities['polyglot'] = polyglot

        # with open ('ner_result.txt', 'a') as file:
        #     file.write(t[0] + ";" + str(t[2]) + ";" + str(nltk) + ";" + str(stanford) + ";" + str(polyglot) + "\n")
            # e('\n')
    print named_entities
    return named_entities

    # print "\n ERROR MESSAGES:", error_sentences



runNER([[1, """WH chief of staff John Kelly says he will "absolutely not" apologize for comments about Rep. Frederica Wilson""", ["WH", "John Kelly", "Fredrica Wilson"]]])


#8332
def compute_f1score():
    with open('../dataset/ner_result.txt', 'r') as file:
        lines = file.readlines()
        nltk_scores, stanford_scores, polyglot_scores = [], [], []
        nltk_precision, stanford_precision, polyglot_precision = [], [], []
        nltk_recall, stanford_recall, polyglot_recall = [], [], []


        for line in lines:
            print line
            s_list = line.replace("[","").replace("]","").replace(" '", "").replace("'", "").replace("\n","").split(";")

            solution = s_list[1].split(",")
            nltk = s_list[2].split(",")
            stanford = s_list[3].split(",")
            polyglot = s_list[4].split(",")

            nltk_f1 = F1_score(solution, nltk)
            stanford_f1 = F1_score(solution, stanford)
            polyglot_f1 = F1_score(solution, polyglot)

            nltk_precision.append(nltk_f1[1])
            stanford_precision.append(stanford_f1[1])
            polyglot_precision.append(polyglot_f1[1])

            nltk_recall.append(nltk_f1[2])
            stanford_recall.append(stanford_f1[2])
            polyglot_recall.append(polyglot_f1[2])


            nltk_scores.append(nltk_f1[0])
            stanford_scores.append(nltk_f1[0])
            polyglot_scores.append(nltk_f1[0])
            print
            print

        # print average
        print "F1 Score"
        print "NLTK -", numpy.mean(nltk_scores)
        print "STANFORD -", numpy.mean(stanford_scores)
        print "POLYGLOT -", numpy.mean(polyglot_scores)
        print

        print "Precision"
        print "NLTK -", numpy.mean(nltk_precision)
        print "STANFORD -", numpy.mean(stanford_precision)
        print "POLYGLOT -", numpy.mean(polyglot_precision)
        print

        print "Recall"
        print "NLTK -", numpy.mean(nltk_recall)
        print "STANFORD -", numpy.mean(stanford_recall)
        print "POLYGLOT -", numpy.mean(polyglot_recall)
