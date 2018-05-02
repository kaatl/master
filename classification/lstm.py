import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "3"

from keras.layers import Dense, Dropout, LSTM, Embedding, Flatten, Permute, Conv1D, MaxPooling1D, Activation, Input, AveragePooling1D, GlobalMaxPooling1D
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential, load_model
from keras.callbacks import Callback, EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.utils.layer_utils import print_summary
from keras.regularizers import l1, l2
from keras.optimizers import Adam, SGD, Adagrad, RMSprop, Nadam


import matplotlib.pyplot as plt

from sklearn.metrics import f1_score, precision_score, recall_score, classification_report


import pandas as pd
import numpy as np



"""
Trainingset : 838
    class-1 : 672
    class-2 : 166
Testset : 210
    class-1 : 45
    class-2 : 166
"""
# input_file = 'classification_datasets/trainingset_glove.tsv'
# input_file_test = 'classification_datasets/testset_glove.tsv'
input_file = 'classification_datasets/trainingset_fasttext.tsv'
input_file_test = 'classification_datasets/testset_fasttext.tsv'
# input_file = 'classification_datasets/trainingset_w2v.tsv'
# input_file_test = 'classification_datasets/testset_w2v.tsv'


class Metrics(Callback):
    # https://keras.io/callbacks/#earlystopping

    def on_train_begin(self, logs={}):
        # self.val_f1s = []
        # self.val_recalls = []
        # self.val_precisions = []
        self.test_acc = []
        self.test_f1s = []
        self.training_f1s = []



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

    # df = df.reindex(np.random.permutation(df.index))
    # df = df.sample(frac=1).reset_index(drop=True)

    """
    Testset
    """
    df_test = pd.read_csv(input_file_test, sep="\t", header=0)

    df_test['sequence'] = df_test['sequence'].apply(lambda x: [e for e in x.split(',')])
    df_test['sequence'] = df_test['sequence'].apply(lambda liste: [[float(e) for e in x.split()] for x in liste])

    # df_test = df_test.reindex(np.random.permutation(df.index))
    # df_test = df_test.sample(frac=1).reset_index(drop=True)



    # train_size = int(len(df) * (1 - test_split)) # 670 er 80% av 838

    X_train = df['sequence'].values[:]
    y_train = np.array(df['label'].values[:])
    X_test = np.array(df_test['sequence'].dropna().values[:])
    y_test = np.array(df_test['label'].dropna().values[:])

    pad_X_train = pad_sequences(X_train, dtype='float', padding="post", maxlen=50)
    pad_X_test = pad_sequences(X_test, dtype='float', padding="post", maxlen=50)

    # return pad_sequences(X_train), y_train, pad_sequences(X_test), y_test
    return pad_X_train, y_train, pad_X_test, y_test


def create_model(X_train):
    print ('Creating model...')

    #input shape = (838, 50, 300)
    input_shape = X_train.shape[1:]
    input_length = len(X_train)

    model = Sequential()
    model.add(Dense(50, input_shape=input_shape, activation=None)) # INPUT LAYER

    reg = 'l1l2(l1=0.0, l2=0.0)'


    """
    Dense layers
    """
    # model.add(Dense(50, activation='sigmoid'))
    # model.add(Dropout(0.1))
    # model.add(Flatten())
    # model.add(Dense(1, activation='sigmoid')) # Output

    """
    LSTM layers
    """
    # model.add(LSTM(50, activation='sigmoid'))
    # model.add(Dropout(0.2))
    # model.add(Dense(1, activation='sigmoid')) # Output


    # # return_sequences=True

    """
    Convolutional
    """
    # model.add(Conv1D(filters = 32,
    #             kernel_size = 3,
    #             padding='valid',
    #             activation='relu',
    #             strides=1,
    #             ))
    #
    # model.add(MaxPooling1D(pool_size = 2))
    # model.add(Flatten())
    #
    # model.add(Dense(1)) # Output

    """
    Convolutional and LSTM
    """
    #kernel_size = 3
    # filters = 200

    # https://stackoverflow.com/questions/46503816/keras-conv1d-layer-parameters-filters-and-kernel-size: --- You're right to say that kernel_size defines the size of the sliding window. The filters parameters is just how many different windows you will have. (All of them with the same length, which is kernel_size). How many different results or channels you want to produce. When you use filters=100 and kernel_size=4, you are creating 100 different filters, each of them with length 4. The result will bring 100 different convolutions.



    # model.add(Dense(200, activation='sigmoid'))


    model.add(Conv1D(filters = 50,
                kernel_size = 4,
                padding='valid',
                activation='tanh',
                strides=2,

                ))

    # model.add(MaxPooling1D(pool_size = 1))
    model.add(AveragePooling1D(pool_size = 2))
    # model.add(Dropout(0.2))

    model.add(Dense(100, activation='sigmoid'))
    #
    # model.add(Dropout(0.2))

    model.add(LSTM(50, activation='tanh'))

    model.add(Dropout(0.3))


    model.add(Dense(1, activation='sigmoid'))
    # model.add(Activation('sigmoid'))



    print ('Compiling...')

    # OPTIMIZERS
    # adam = Adam(lr=0.035, decay=0.0001)
    adam = Adam()
    sgd = SGD()
    adagrad = Adagrad()
    rmsprop = RMSprop(lr=0.0075)
    nadam = Nadam()

    model.compile(loss='binary_crossentropy',
                  optimizer=adam,
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
    axes.set_ylim([0, 1.1])
    axes.set_xlim([0, len(training_acc)-1])
    plt.title('Performance Scores')
    plt.legend()
    plt.show()


# Load data
X_train, y_train, X_test, y_test = load_data()
model = create_model(X_train)

# Print info about model
# print_summary(model)

print ('\nFitting model...\n')

"""
    Instantiate metrics
"""
metrics = Metrics()
earlystop = EarlyStopping(monitor='loss', min_delta=0.0001, patience=15, verbose=1, mode='auto')
filepath = 'models/model_{epoch:02d}.hdf5'
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=0, save_best_only=False, save_weights_only=False, mode='auto', period=1)
reduce_lr = ReduceLROnPlateau(monitor='acc', factor=0.01, patience=5, min_lr=0.000001, verbose=1)

fitting = model.fit(X_train, y_train,
                    batch_size=32,
                    epochs=100,
                    verbose = 2,
                    callbacks=[metrics, earlystop, checkpoint, reduce_lr],
                    )


# Accuracy and F1-Score for training and test data
training_acc = [0] + fitting.history['acc']
test_acc = [0] + metrics.test_acc
test_f1 = [0] + metrics.test_f1s
training_f1 = [0] + metrics.training_f1s


max_test_f1 = max(test_f1)
# Find LAST index of best f1-score
max_test_f1_epoch_first = test_f1.index(max_test_f1)
max_test_f1_epoch = len(test_f1) - 1 - test_f1[::-1].index(max_test_f1)
max_test_f1 = round(max_test_f1, 4)

print "\nMax Test F1-score in epoch {}, with a score of {}".format(max_test_f1_epoch, max_test_f1)

print ('\nPrinting test scores\n')

# Evaluate test set
score, acc = model.evaluate(X_test, y_test, batch_size=1)

print '\nTest Accuracy:', format(acc, '.4f')
print 'Test F1-score: ', format(test_f1[-1], '.4f')

# F1-score per class
print "\nAverage scores for each class: "

def best_model_print(max_f1, epoch):
    str_max_test_f1 = max_f1

    model = load_model('models/model_01.hdf5')

    str_max_test_f1 = ""
    if str(epoch) != "00":

        if epoch < 10:
            str_max_test_f1 = "0" + str(epoch)
        else:
            str_max_test_f1 = str(epoch)

        print 'Printing prediction score for the model in epoch ' + str_max_test_f1
        filepath = 'models/model_' + str_max_test_f1 + '.hdf5'
        model = load_model(filepath)
        # score, acc = model.evaluate(X_test, y_test, batch_size=1)

        y_pred = model.predict_classes(X_test)
        print(classification_report(y_test, y_pred, digits=4))

    return model


# model = best_model_print(max_test_f1, max_test_f1_epoch_first)
model = best_model_print(max_test_f1, max_test_f1_epoch)

def class_labels(X):
    predictions = model.predict_classes(X, verbose=0, batch_size=1)
    pred_class_1 = [item[0] for item in predictions]

    # pred_class_1 = pred_class_1[]
    print len(pred_class_1)
    print
    for x in pred_class_1:
        print x


class_labels(X_test)
# class_labels(X_train)

# Plot diagram
plot_diagram(training_acc, test_acc, test_f1, training_f1)



"""
SOURCES
"""
#https://faroit.github.io/keras-docs/1.2.2/regularizers/
#https://keras.io/optimizers/
#https://keras.io/callbacks/
