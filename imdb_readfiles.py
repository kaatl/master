import os

dir_list_neg = os.listdir("/Users/carolineodden/Documents/code/master/aclImdb/train/neg")

print len(dir_list_neg)

negative_sentiment_dataset = ''
for path in dir_list_neg:
    with open('aclImdb/train/neg/' + path, 'r') as f:
        # print f.read() + ', Negative\n'

        negative_sentiment_dataset += f.read() + ', Negative\n'

print negative_sentiment_dataset

# with open('dataset/imdb_sentiment.txt', 'w') as f:
#     f.write(negative_sentiment_dataset)



dir_list_pos = os.listdir("/Users/carolineodden/Documents/code/master/aclImdb/train/pos")

print len(dir_list_pos)

positive_sentiment_dataset = ''
for path in dir_list_pos:
    with open('aclImdb/train/pos/' + path, 'r') as f:
        # print f.read() + ', Positive\n'

        positive_sentiment_dataset += f.read() + ', Positive\n'

print positive_sentiment_dataset

with open('dataset/imdb_sentiment.txt', 'a') as f:
    f.write(positive_sentiment_dataset)
