from keras.layers import Dense, Dropout, LSTM, Embedding, Flatten, Permute, Conv1D, MaxPooling1D, Activation
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.callbacks import Callback
from keras.utils.layer_utils import print_summary

import matplotlib.pyplot as plt

from sklearn.metrics import f1_score, precision_score, recall_score


import pandas as pd
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# input_file = 'classification_datasets/trainingset_glove.tsv'
# input_file_test = 'classification_datasets/testset_glove.tsv'
# input_file = 'classification_datasets/trainingset_fasttext.tsv'
# input_file_test = 'classification_datasets/testset_fasttext.tsv'
input_file = 'classification_datasets/trainingset_w2v.tsv'
input_file_test = 'classification_datasets/testset_w2v.tsv'

class Metrics(Callback):
    def on_train_begin(self, logs={}):
        # self.val_f1s = []
        # self.val_recalls = []
        # self.val_precisions = []
        self.test_acc = []
        self.test_f1s = []
        self.training_f1s = []

        # loss, acc = self.model.evaluate(X_test, y_test, verbose=0)
        # self.test_acc.append(acc)
        #
        # print acc
        #
        # val_predict = (np.asarray(self.model.predict(X_test))).round()
        # val_targ = y_test
        # val_f1 = f1_score(val_predict, val_targ)
        # self.test_f1s.append(val_f1)
        # print val_f1
        #
        # val_predict2 = (np.asarray(self.model.predict(X_train))).round()
        # val_targ2 = y_train
        # val2_f1 = f1_score(val_predict2, val_targ2)
        # self.training_f1s.append(val2_f1)
        # print val2_f1



    def on_epoch_end(self, epoch, logs={}):
        loss, acc = self.model.evaluate(X_test, y_test, verbose=0)
        self.test_acc.append(acc)

        val_predict = (np.asarray(self.model.predict(X_test))).round()
        val_targ = y_test
        val_f1 = f1_score(val_predict, val_targ, average='micro')
        self.test_f1s.append(val_f1)

        val_predict2 = (np.asarray(self.model.predict(X_train))).round()
        val_targ2 = y_train
        val2_f1 = f1_score(val_predict2, val_targ2, average='micro')
        self.training_f1s.append(val2_f1)

metrics = Metrics()


def load_data(test_split = 0.2):
    print ('Loading data...\n')

    df = pd.read_csv(input_file, sep="\t", header=0)

    """
    Trainingset
    """
    # print df['sequence']
    # print df
    df['sequence'] = df['sequence'].apply(lambda x: [e for e in x.split(',')])
    df['sequence'] = df['sequence'].apply(lambda liste: [[float(e) for e in x.split()] for x in liste])

    df = df.reindex(np.random.permutation(df.index))
    df = df.sample(frac=1).reset_index(drop=True)

    """
    Testset
    """
    df_test = pd.read_csv(input_file_test, sep="\t", header=0)

    df_test['sequence'] = df_test['sequence'].apply(lambda x: [e for e in x.split(',')])
    df_test['sequence'] = df_test['sequence'].apply(lambda liste: [[float(e) for e in x.split()] for x in liste])

    df_test = df_test.reindex(np.random.permutation(df.index))
    df_test = df_test.sample(frac=1).reset_index(drop=True)



    # train_size = int(len(df) * (1 - test_split)) # 670 er 80% av 838

    X_train = df['sequence'].values[:]
    y_train = np.array(df['label'].values[:])
    X_test = np.array(df_test['sequence'].dropna().values[:])
    y_test = np.array(df_test['label'].dropna().values[:])

    pad_X_train = pad_sequences(X_train, dtype='float32', padding="post", maxlen=50)
    pad_X_test = pad_sequences(X_test, dtype='float32', padding="post", maxlen=50)

    # return pad_sequences(X_train), y_train, pad_sequences(X_test), y_test
    return pad_X_train, y_train, pad_X_test, y_test


def create_model(X_train):
    print ('Creating model...')
    model = Sequential()

    #input shape = (838, 50, 300)
    input_shape = X_train.shape[1:]
    input_length = len(X_train)

    """
    LSTM layers
    """
    model.add(LSTM(50, activation='sigmoid', input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(100, activation='sigmoid'))
    model.add(Dropout(0.2))
    # model.add(Dense(30, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))


    # return_sequences=True
    # model.add(LSTM(50, activation='relu'))
    # model.add(Dropout(0.5))




    """
    Dense layers
    """
    # model.add(Dense(100, activation='sigmoid', input_shape=input_shape))
    # model.add(Dropout(0.1))
    # model.add(Flatten())
    # model.add(Dense(1, activation='sigmoid'))

    """
    Convolutional
    """
    # kernel_size = 3
    # # filters = 200
    # pool_size = 2
    # model.add(Conv1D(32,
    #             kernel_size,
    #             padding='valid',
    #             activation='relu',
    #             strides=1,
    #             input_shape=input_shape))
    # model.add(MaxPooling1D(pool_size=pool_size))
    # model.add(Dropout(0.1))
    # model.add(LSTM(200, activation='sigmoid'))
    # model.add(Dense(1))
    # model.add(Activation('sigmoid'))



    print ('Compiling...')
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model

def plot_diagram(training_acc, test_acc, test_f1, training_f1):
    plt.plot(training_f1, 'darkblue', label="Training F1-score")
    plt.plot(test_f1, 'darkgreen', label="Test F1-score")
    plt.plot(training_acc, '--', color='deepskyblue', label="Training Accuracy")
    plt.plot(test_acc, '--', color='limegreen', label="Test Accuracy")
    # plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    axes = plt.gca()
    axes.set_ylim([0, 1])
    axes.set_xlim([0, len(training_acc)-1])
    plt.legend()
    plt.show()


# Load data
X_train, y_train, X_test, y_test = load_data()
model = create_model(X_train)

# Print info about model
# print_summary(model)

print ('\nFitting model...\n')

fitting = model.fit(X_train, y_train,
                    batch_size=32,
                    epochs=40,
                    validation_split = 0.0,
                    verbose = 2,
                    callbacks=[metrics],
                    shuffle=True)


# Accuracy and F1-Score for training and test data
training_acc = [0] + fitting.history['acc']
test_acc = [0] + metrics.test_acc
test_f1 = [0] + metrics.test_f1s
training_f1 = [0] + metrics.training_f1s

max_test_f1 = max(test_f1)
max_test_f1_epoch = test_f1.index(max_test_f1) - 1
print "\nMax Test F1-score in epoch {}, with a score of {}".format(max_test_f1_epoch, max_test_f1)

print ('\nPrinting test scores\n')

# Evaluate test set
score, acc = model.evaluate(X_test, y_test, batch_size=1)
# print('Test score:', score)
print('Test Accuracy:', acc)
print('Test F1-score: ', test_f1[-1])

# Plot diagram
plot_diagram(training_acc, test_acc, test_f1, training_f1)
