# !/usr/bin/env python
# -*- coding:utf-8 -*-
# create on 17/1/5
__author__ = 'siyipu'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from langconv import *

hans_converter = Converter("zh-hans")
hant_converter = Converter("zh-hant")


def jfti(line, mod="zh-hans"):
    # mod="zh-hans": 繁体到简体, 默认
    # mod="zh-hant": 简体到繁体
    line = Converter(mod).convert(line.decode('utf-8'))
    return line


def zh_hans(ustring):
    '''
    繁体到简体转换
    :param ustring: unicode string
    :return: unicode string
    '''
    return hans_converter.convert(ustring)


def zh_hant(ustring):
    '''
    简体到繁体转换
    :param ustring: unicode string
    :return: unicode string
    '''
    return hant_converter.convert(ustring)


if __name__ == '__main__':
    line = "需求：把中文字符串進行繁體和間體中文的轉換； 思路：引入間繁體處理庫，有興趣的同學可以研究壹下內部實現"
    line = jfti(line)
    print line
    line = jfti(line, mod="zh-hant")
    print line
