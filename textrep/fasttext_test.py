import fasttext

def load_model(path):
    return fasttext.load_model(path)

def get_v_for_w(model, word):
    return model[word]

def get_v_for_s(model, s):
    return [get_v_for_w(model, w) for w in s.lower().split()]


def fasttext_main2(s):
    path = 'models/kyubyoung_no.bin' # https://github.com/Kyubyong/wordvectors

    print "Loading model ..."
    model = load_model(path)
    print "Done!"


    v_for_s = get_v_for_s(model, s)

    return v_for_s

fasttext_main2("Dette er en test")
# https://pypi.python.org/pypi/fasttext
