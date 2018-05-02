import nltk
from nltk.tokenize import word_tokenize

train = [('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible.', 'neg')]

all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

test_sentence = "This is not the best band I've ever heard!"
test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}

classifier = nltk.NaiveBayesClassifier.train(t)
print classifier.classify(test_sent_features)
