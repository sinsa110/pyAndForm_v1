# !/usr/bin/env python
# -*- coding:utf-8 -*-
# create on 17/10/27
__author__ = 'yipu.si'

import os

def read_dict():
    root = os.path.dirname(__file__)
    DIC_PATH = root + "/ChineseStrokes.dat"
    data = open(DIC_PATH)
    data = [e.decode("utf8").strip() for e in data]
    data = [e.split(u"\t") for e in data]
    return dict(data)

WORD_DICT = read_dict()

def word2strokes(ustring):
    return WORD_DICT.get(ustring, "")


def words2strokes(ustrings):
    res = []
    for w in ustrings:
        res.append(word2strokes(w))
    return " ".join(res)


def levenshtein_distance(first, second):
    '''
    计算两个字符串之间的L氏编辑距离
    :输入参数 first: 第一个字符串
    :输入参数 second: 第二个字符串
    :返回值: L氏编辑距离
    '''
    if len(first) == 0 or len(second) == 0:
        return len(first) + len(second)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for i in range(first_length)]  # 初始化矩阵
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length - 1][second_length - 1]


def find_n_words(s1, li):
    T = []
    for e in li:
        dis = levenshtein_distance(s1, e)
        if dis < 3 and dis > 0:
            T.append(li[e] + "_" + str(dis))
    return ",".join(T)


if __name__ == '__main__':
    s1 = u"日"
    s2 = u"阳"
    s1 = word2strokes(s1)
    s2 = word2strokes(s2)
