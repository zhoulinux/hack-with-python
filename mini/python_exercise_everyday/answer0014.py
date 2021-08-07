#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
"""


import xlwt


students = {
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}

wb = xlwt.Workbook()
ws = wb.add_sheet('students')

row = 0
for key, values in students.items():
    col = 0
    ws.write(row, col, key)
    col += 1
    for value in values:
        ws.write(row, col, value)
        col += 1
    row += 1
            
wb.save('students.xlsx')