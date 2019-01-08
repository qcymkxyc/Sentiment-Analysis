#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
 @author:qcymkxyc
 @email:qcymkxyc@163.com
 @software: PyCharm
 @file: preprocess.py
 @time: 2019/1/1 18:07

"""
import os
import codecs


def read_file(filename):
    """"""
    with codecs.open(filename, "r",encoding="gbk",errors="ignore",) as f:
        content = f.read()
    return content


def read_data(base_path):
    """读取数据

    :param base_path: str
        基路径
    :return:
    """
    neg_path = os.path.join(base_path, "neg")
    pos_path = os.path.join(base_path, "pos")

    data, labels = list(), list()
    # neg文件夹读取
    for filename in os.listdir(neg_path):
        file_path = os.path.join(neg_path, filename)
        try:
            content = read_file(file_path)
        except UnicodeDecodeError:
            continue
        else:
            data.append(content)
            labels.append("neg")

    # pos文件夹读取
    for filename in os.listdir(pos_path):
        file_path = os.path.join(pos_path, filename)
        try:
            content = read_file(file_path)
        except UnicodeDecodeError:
            continue
        else:
            data.append(content)
            labels.append("pos")

    return data, labels


def create_vocab(data):
    """用数据生成词汇表

    :param data: List[str]
        数据
    :return dict{str : int}
        词对应的index
    """
    words = set()
    for sentence in data:
        for word in sentence.split():
            words.add(word)

    word2index = dict()
    for i, word in enumerate(words):
        word2index[word] = i

    return word2index
