# !/usr/bin/env python
# -*- coding:utf-8 -*-
# create on 18/4/27
__author__ = 'yipu.si'

from models.getChineseStrokes import word2strokes, levenshtein_distance, words2strokes
from models.pypinyin import pinyin
from models.toSimpleChinese import zh_hans


def is_contains_relation(word1, word2):
    if word1 in word2 or word2 in word1:
        return True
    else:
        return False


def is_change_name(word1, word2):
    if set(list(word1)) == set(list(word2)):
        return True
    else:
        return False


def is_pinyin_same(words1, words2):
    """ 判断两个词语是否同音
    :param words1: 词语 1，unicode 编码
    :param words2: 词语 2，unicode 编码
    :return: 是否同音，布尔型
    example: >> is_pinyin_same(u'重要', u"你要")
                False
    """
    words1 = zh_hans(words1)
    words2 = zh_hans(words2)
    if len(words1) != len(words2):
        return False
    pinyin1 = pinyin(words1, heteronym=True)
    pinyin2 = pinyin(words2, heteronym=True)
    is_same = 1
    for i in range(len(pinyin1)):
        set1 = set(pinyin1[i])
        set2 = set(pinyin2[i])
        res = set1.intersection(set2)
        is_same *= res.__len__()
    if is_same == 0:
        return False
    else:
        return True


def is_form_same(words1, words2, return_number=False):
    """ 判断两个词语是否形近
    :param words1: 词语 1，unicode 编码
    :param words2: 词语 2，unicode 编码
    :param return_number: 返回结果是否为 编辑距离数值，默认为 False
    :return: 是否形近，布尔型 （笔顺的编辑距离小于 3 则认为形近，否则为不形近）。
            当 return_number = True 时，返回结果为两个字符串笔顺的编辑距离取值，int 型
    example: >> is_form_same(u'习大大', u"习夶", return_number=True)
                1
             >> is_form_same(u'习大大', u"习夶")
                True
    """
    words1 = zh_hans(words1)
    words2 = zh_hans(words2)
    form1 = words2strokes(words1)
    form2 = words2strokes(words2)
    distance = levenshtein_distance(form1, form2)
    if return_number:
        return distance
    if distance < 3:
        return True
    else:
        return False


def is_words_same(words1, words2):
    """ 判断两个句子是否相近
        :param words1: 词语 1，unicode 编码
        :param words2: 词语 2，unicode 编码
        :return: 是否形近，布尔型
        （1. 编辑距离比小于 0.5，则认为相近，否则不相近；
        2. 构成元素相同，顺序不同，则相近；
        3. 两个词之间的关系为包含关系，则为相近）。
        example: >> is_words_same(u'习大大', u'大大习')
                    True
                 >> is_form_same(u'习大大', u"习夶")
                    False
        """
    words1 = zh_hans(words1)
    words2 = zh_hans(words2)
    if len(words1) != len(words2):
        if is_contains_relation(words1, words2):
            return True
        else:
            return False
    distance = levenshtein_distance(words1, words2)
    if distance * 1.0 / len(words1) < 0.5 or is_change_name(words1, words2):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_pinyin_same(u'重要', u"你要"))
    print(is_form_same(u'习大大', u"习夶", return_number=True))
    print(is_words_same(u'习大大', u"习夶"))
    print(is_pinyin_same(u'必须', u"必需"))
    print(is_form_same(u'习大大', u"大大习"))
    print(is_words_same(u'习大大', u"习夶"))
    print(is_words_same(u'彭永志', u"彭志永"))
