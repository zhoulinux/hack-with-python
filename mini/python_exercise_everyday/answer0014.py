#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中.

xlwt is a library for developers to use to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
"""


import json, xlwt


student = {}
with open('./student.txt') as f:
    student = json.loads(f.read())

wb = xlwt.Workbook()
ws = wb.add_sheet('student')

for i, (key, values) in enumerate(student.items()):
    col = 0
    ws.write(i, col, key)
    for value in values:
        col += 1
        ws.write(i, col, value)

wb.save('student.xls')