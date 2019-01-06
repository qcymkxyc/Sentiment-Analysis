#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: lstm.py
 @time: 2019/1/1 21:32

"""
from tensorflow import keras
import tensorflow as tf

embedding_unit = 200
lstm_unit = 120
hidden_units = [80, ]


def create_lstm(vocab_size):
    """建立LSTM网络

    :param vocab_size: int
        词汇表的个数
    """
    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, embedding_unit))
    model.add(keras.layers.LSTM(units=lstm_unit, return_sequences=False))
    for i, unit in enumerate(hidden_units):
        model.add(keras.layers.Dense(units=unit, activation=tf.nn.relu))
    model.add(keras.layers.Dense(units=1, activation=tf.nn.sigmoid))

    return model
