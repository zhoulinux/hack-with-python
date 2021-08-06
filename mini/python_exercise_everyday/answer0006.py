#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""


import glob
from answer0004 import word_counter


for f in glob.glob('./txt_00006/*.txt'):
    print(word_counter(f).most_common(1)[0][0])