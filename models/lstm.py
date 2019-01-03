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


def create_lstm(vocab_size):
    """建立LSTM网络

    :param vocab_size: int
        词汇表的个数
    """
    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 200))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(units=80, activation=tf.nn.relu))
    model.add(keras.layers.Dense(units=1, activation=tf.nn.sigmoid()))

    return model
