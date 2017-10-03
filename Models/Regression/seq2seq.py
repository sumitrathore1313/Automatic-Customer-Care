from __future__ import print_function
from keras.models import Sequential
from keras import layers
import numpy as np
from six.moves import range

def seq2seq(train_x, train_y, val_x, val_y, HIDDEN_SIZE= 128,BATCH_SIZE = 128, LAYERS = 5, epochs = 1):
    """
    sequence to sequence model keras implement
    :param train_x: training data input
    :param train_y: training data output
    :param val_x: validation data input
    :param val_y: validation data output
    :param HIDDEN_SIZE: size of hidden neuron
    :param BATCH_SIZE: batch size
    :param LAYERS: layers of lstm
    :param epochs: number of epoch
    :return: return model
    """
    RNN = layers.LSTM

    model = Sequential()
    model.add(RNN(HIDDEN_SIZE, input_shape=(50, 100)))
    model.add(layers.RepeatVector(50))
    for _ in range(LAYERS):
        model.add(RNN(HIDDEN_SIZE, return_sequences=True))
    model.add(layers.TimeDistributed(layers.Dense(100)))
    model.add(layers.Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    model.summary()

    model.fit(train_x, train_y,
                  batch_size=BATCH_SIZE,
                  epochs=epochs,
                  validation_data=(val_x, val_y))
    return model