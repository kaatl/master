import numpy as np
import time

def load_vector_model(path):
    with open(path, 'r') as file:
        print "Reading '{}' ...".format(path)
        lines = file.readlines()[1:]

        word_vec = {}

        print "Loading file to dictionary ..."
        for line in lines:
            line = line.split()

            word = line[0]
            vec = np.array(line[1:])
            # vec = line[1:]

            word_vec[line[0]] = vec

        print "Done!\n"

    return word_vec

def get_v_for_w(model, word):
    return model.get(word)

def get_v_for_s(model, s):
    return [get_v_for_w(model, w) for w in s.lower().split()]




def fasttext_main(s):

    path = 'models/fasttext_no.vec' # https://github.com/facebookresearch/fastText
    # s = "Dette er en test"

    start_time = time.time() # Takes 20 - 30 seconds
    model = load_vector_model(path) # Load model
    time_used = int(round(time.time() - start_time))
    print "Time for loading the data is: {} seconds".format(time_used)


    vec_for_s = get_v_for_s(model, s) # Get vectors for sentence

    return vec_for_s
    # print vec_for_s

print fasttext_main('Dette er en test')
