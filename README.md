# 同音形近判别系统

## 功能
判断两个中文词语是否为同音或形近。


## 使用方法
step 1. 下载源码，[click here](https://github.com/sinsa110/pyAndForm_v1/archive/master.zip)

step 2. 解压后放在自己的代码（ 运行环境 `python2.＊` ）目录下，修改文件夹名称 `pyandform.git` 改为 `pyandform` (文件夹名字中如果包含 `.`，import 时会报错)

step 3. 在自己的代码中加入下面代码即可

``` python
from pyandform import is_form_same, is_pinyin_same  # pyandform 为解压后的文件夹名

```

## 参数说明

``` python
def is_pinyin_same(words1, words2):
    """ 判断两个词语是否同音
    :param words1: 词语 1，unicode 编码
    :param words2: 词语 2，unicode 编码
    :return: 是否同音，布尔型
    example: >> is_pinyin_same(u'重要', u"你要")
                False
    """
```

```python
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
```

```python
def is_words_same(words1, words2):
    """ 判断两个句子是否相近
        :param words1: 词语 1，unicode 编码
        :param words2: 词语 2，unicode 编码
        :return: 是否形近，布尔型 （编辑距离小于 3，则认为相近，否则不相近）。
        example: >> is_words_same(u'习大大', u'大大习')
                    True
                 >> is_form_same(u'习大大', u"习夶")
                    False
        """
```

## 示例

``` python
>> from pyandform import is_form_same, is_pinyin_same, is_words_same  
>> is_pinyin_same(u'重要', u"你要")
    False
>>
>> is_form_same(u'习大大', u"习夶", return_number=True)
    1
>> is_form_same(u'习大大', u"习夶")
    True
>> is_words_same(u'习大大', u'大大习')
    True
>> is_form_same(u'习大大', u"习夶")
    False
```