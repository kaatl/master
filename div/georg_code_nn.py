    # to create your model you define something like:
    model = Sequential()

    model.add(Embedding(top_words, vector_dimension, input_length=max_words))

    model.add(LSTM(lstm_size))
    model.add(Dense(max_words, activation='relu', W_regularizer=l2(0.1)))
    # adding a dropout level is sometimes necessary for reducing the overfitting
    model.add(Dropout(0.4))
    model.add(Dense(3, activation='softmax', W_regularizer=l2(0.1)))

    # this is for setting the learning rate (lr)
    adam_1 = Adam(lr=0.035)



    model.compile(
        loss='categorical_crossentropy',
        optimizer=adam_1,
        metrics=['accuracy'])
    print (model.summary())

    # next, somewhere you train the model over the sample of data you provide as input.
    model.fit(X_train,Y_train,
            nb_epoch=(num of epocs to run),
            batch_size=50,
            validation_data=(X_test, Y_test),
            verbose=1,
            shuffle=False)
    # where: X_train and Y_train are two arrays which contain the input training data and the class each input belongs to.

    # once trained over a number of epocs you then use the trained model to do predictions on unseen data ...
    predictions = model.predict(X_valid, verbose=1)

    # .... and finally evaluate the accuracy of the predictions
    scores = model.evaluate(X_valid, Y_valid, verbose=1)
