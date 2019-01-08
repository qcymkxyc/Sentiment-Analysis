#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
    @Time :    19-1-3 上午11:31
    @Author:  qcymkxyc
    @File: data_helper.py
    @Software: PyCharm
    
    
"""


def data_to_voc(data):
    """数据转化为词典

    :param data: List[str]
        数据
    :return: dict{str ： int}
        Vocabulary
    """
    words = set()
    for sentence in data:
        for i, word in enumerate(sentence.split()):
            words.add(word)

    words_to_index = dict()
    for i, word in enumerate(words):
        words_to_index[word] = i

    return words_to_index
