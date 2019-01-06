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


def create_cnn(vocab_size):
    """建立CNN网络

    :param vocab_size: int
        词典个数
    :return: model
    """
    model = keras.Sequential()
    model.add(keras.layers.Embedding(input_dim=vocab_size,output_dim=200))
    model.add(keras.layers.Conv)
