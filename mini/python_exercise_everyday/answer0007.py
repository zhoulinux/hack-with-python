#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码，包括空行和注释，但是要分别列出来。
"""


import glob, re
from collections import Counter


line_counter = Counter({"all": 0, "codes": 0, "blanks": 0, "comments": 0})

# count all lines, blank lines and single-line comments
for file in glob.glob("./*.py"):
    with open(file, encoding="utf-8") as f:
        for line in f:
            line_counter.update({"all": 1})
            if re.search(r"^$", line):
                line_counter.update({"blanks": 1})
            elif re.search(r"^#", line):
                line_counter.update({'comments': 1})

# count multiline comments
for file in glob.glob("./*.py"):
    with open(file, encoding="utf-8") as f:
        comments = re.findall(r"[\'\"]{3}[\w\W]*?[\'\"]{3}", f.read(), re.MULTILINE)
        for comment in comments:
            line_counter.update({'comments': len(re.findall(r'\n', comment))})

print(line_counter["all"])                
print(line_counter["blanks"])
print(line_counter["comments"])