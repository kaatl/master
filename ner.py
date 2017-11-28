import nltk
from pycorenlp import StanfordCoreNLP
from polyglot.text import Text

from termcolor import colored


"""
***** NLTK *****
"""

def nltkNER(sentence):
    print colored('========NLTK=======\n', 'blue')
    print sentence
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    chunked = nltk.ne_chunk(pos_tags, binary=False)
    print getNERList(chunked), '\n'

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
                continuous_chunk.append(named_entity)
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

def stanfordCoreNLPNER(sentence, lang):
    print colored('\n=========Stanford CoreNLP======\n', 'blue')
    print sentence
    if (lang == 'en'):
        output = nlp.annotate(sentence, properties={
            # 'annotators': 'tokenize,ssplit,pos,depparse,parse',
            'annotators': 'ner',
            'outputFormat': 'json'
        })

        # print(output['sentences'][0]['parse'])
        print getCoreNLPList(output['sentences'][0]['tokens'])

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
                named_entities.append(named_entity)
    return named_entities



"""
***** POLYGLOT *****
"""

def polyglotNER(sentence, lang):
    print colored('\n========POLYGLOT========\n', 'blue')
    print sentence
    if (lang == 'no'):
        text = Text(sentence, hint_language_code='no')
    else:
        text = Text(sentence, hint_language_code='en')

    for entity in text.entities:
        print entity.tag, entity



def runNER(texts):
    print texts
    for text in texts:
        print colored('\n\n\n\n NEW TWEET \n\n', 'green')
        print colored(text[1], 'cyan'), '\n'
        nltkNER(text[0])
        stanfordCoreNLPNER(text[0], text[2])
        polyglotNER(text[0], text[2])
