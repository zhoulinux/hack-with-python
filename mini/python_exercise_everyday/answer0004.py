#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


import re
from collections import Counter


def word_counter(file):
    pattern = r'\b[A-Za-z]+\b'
    word_counter = Counter()
    
    with open(file, encoding='utf-8') as f:
        for line in f:
            words = re.findall(pattern, line)
            print(words)
            word_counter.update(words)
            
    return word_counter


print(word_counter('mbox-short.txt').most_common())