from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate("I really hate the new book so much, I can't even speak",
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
for s in res["sentences"]:
    print "%d: '%s': %s %s" % (
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"],
        s["sentiment"]
    )

# Se denne linken for start av server osv https://stackoverflow.com/questions/32879532/stanford-nlp-for-python
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
