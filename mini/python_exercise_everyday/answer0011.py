#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""


words = []
with open('filtered_words.txt') as f:
    for line in f:
        words.append(line.rstrip('\n'))
print(words)

text = input()
if any([word for word in words if word in text]):
    print('Freedom')
else:
    print('Human Rights')