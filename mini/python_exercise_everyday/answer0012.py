#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""


import re


words = []
with open('filtered_words.txt') as f:
    for line in f:
        words.append(line.rstrip('\n'))
print(words)

text = input()
words = list(filter(lambda word:  word in text, words))
print(words)
for word in words:
    text = re.sub(word, '*'*len(word), text)

print(text)