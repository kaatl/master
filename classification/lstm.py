from keras.layers import Dense, Dropout, LSTM, Embedding, Flatten, Permute
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
import pandas as pd
import numpy as np

input_file = 'trainingset_glove.tsv'

def load_data(test_split = 0.2):
    print ('Loading data...')

    df = pd.read_csv(input_file, sep="\t", header=0)
    # 1 2 3, 2 3 5
    df['sequence'] = df['sequence'].apply(lambda x: [e for e in x.split(',')])
    # print df['sequence']
    print
    # [[1 2 3], [2 3 5]]

    df['sequence'] = df['sequence'].apply(lambda liste: [[float(e) for e in x.split()] for x in liste])
    # z = [v + w for v in x for w in y]
    # [[int(y) for y in x] for x in values]




    train_size = int(len(df) * (1 - test_split)) # 670 er 80% av 838

    X_train = df['sequence'].values[:train_size]
    y_train = np.array(df['label'].values[:train_size])
    X_test = np.array(df['sequence'].values[train_size:])
    y_test = np.array(df['label'].values[train_size:])

    pad_X_train = pad_sequences(X_train, dtype='float32', padding="post", maxlen=5)
    pad_X_test = pad_sequences(X_test, dtype='float32', padding="post", maxlen=5)

    # return pad_sequences(X_train), y_train, pad_sequences(X_test), y_test
    return pad_X_train, y_train, pad_X_test, y_test


def create_model(input_length, X_train):
    print ('Creating model...')
    model = Sequential()

    #input shape = (670, 5, 300)


    # model.add(LSTM(300, return_sequences=True, input_shape=(670, 300), activation = 'sigmoid'))
    # model.add(Dropout(0.5))
    # model.add(LSTM(300, activation = 'sigmoid'))
    # model.add(Dropout(0.5))
    #
    # # model.add(Dense(650))
    # model.add(Flatten())
    # model.add(Dense(1, activation='sigmoid'))


    # model.add(Embedding(300, output_dim = 50, input_length = input_length))
    # model.add(LSTM(300, activation='sigmoid', input_shape=(5, 300), return_sequences=True))
    # model.add(Dropout(0.5))
    # model.add(LSTM(300, activation='sigmoid'))
    # model.add(Dropout(0.5))

    # model.add(Flatten())

    model.add(Dense(300, activation='relu', input_shape=(670, 5, 300)))
    # model.add(Dense(300, activation='sigmoid'))

    print ('Compiling...')
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


# Load data
X_train, y_train, X_test, y_test = load_data()

model = create_model(len(X_train[0]), X_train)

print ('Fitting model...')
hist = model.fit(X_train, y_train, batch_size=64, epochs=10, validation_split = 0.0, verbose = 1)

score, acc = model.evaluate(X_test, y_test, batch_size=1)
print('Test score:', score)
print('Test accuracy:', acc)


 # 1 3 4, 6 5 7, 1 2 7

 # [[1,3,5],[6,5,7],[1,2,7]]


 # float(0.145953,-0.208433)
