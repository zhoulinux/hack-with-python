#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中.
"""


import xlwt, re


citys = []
with open('city.txt') as f:
    for line in f:
        line = line.strip('{}').strip()
        if line:
            citys.append(re.findall(r'[\w\d]+', line))

wb = xlwt.Workbook()
ws = wb.add_sheet('city')

row = 0
for city in citys:
    col = 0
    for value in city:
        ws.write(row, col, value)
        col += 1
    row += 1
            
wb.save('city.xlsx')