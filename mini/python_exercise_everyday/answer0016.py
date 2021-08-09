#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中。
"""


import json, xlwt


numbers = []
with open('./numbers.txt') as f:
    numbers = json.loads(f.read())

wb = xlwt.Workbook()
ws = wb.add_sheet('number')

for i, number in enumerate(numbers):
    col = 0
    for value in number:
        ws.write(i, col, value)
        col += 1
            
wb.save('./numbers.xls')