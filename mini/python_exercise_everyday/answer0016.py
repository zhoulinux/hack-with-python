#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xlsx 文件中。
"""


import xlwt, re


numbers = []
with open('numbers.txt') as f:
    for line in f:
        line = line.strip('[]').strip()
        if line:
            numbers.append(re.findall(r'[\d]+', line))

wb = xlwt.Workbook()
ws = wb.add_sheet('number')

row = 0
for number in numbers:
    col = 0
    for value in number:
        ws.write(row, col, value)
        col += 1
    row += 1
            
wb.save('numbers.xlsx')