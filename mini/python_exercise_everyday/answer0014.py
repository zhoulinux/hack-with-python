#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xlsx 文件中.
"""


import xlwt, re


students = []
with open('student.txt') as f:
    for line in f:
        line = line.strip('{}').strip()
        if line:
            students.append(re.findall(r'[\w\d]+', line))

wb = xlwt.Workbook()
ws = wb.add_sheet('student')

row = 0
for student in students:
    col = 0
    for value in student:
        ws.write(row, col, value)
        col += 1
    row += 1
            
wb.save('student.xlsx')