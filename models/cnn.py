#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: cnn.py
 @time: 2019/1/1 21:33

"""
from tensorflow import keras
import tensorflow as tf

conv_size = 5
filters = 4
hidden_units = [80, ]


def create_cnn(vocab_size):
    """建立CNN网络

    :param vocab_size: int
        词典个数
    :return: model
    """
    model = keras.Sequential()
    model.add(keras.layers.Embedding(input_dim=vocab_size, output_dim=200))
    model.add(keras.layers.Conv1D(
        filters=filters,
        kernel_size=conv_size,
        activation=tf.nn.tanh)
    )
    model.add(keras.layers.GlobalMaxPool1D())
    for i, unit in enumerate(hidden_units):
        model.add(keras.layers.Dense(units=unit,activation=tf.nn.relu))
    model.add(keras.layers.Dense(units=1, activation=tf.nn.sigmoid))

    return model