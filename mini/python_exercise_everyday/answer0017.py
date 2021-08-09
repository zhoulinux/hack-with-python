#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
"""

from xlrd import open_workbook
from lxml import etree


student = {}

wb = open_workbook('./student.xls')
ws = wb.sheet_by_name('student')
        
for cur_row in range(0, ws.nrows):
    row_value = ws.row_values(cur_row)
    student[row_value[0]] = [row_value[1], int(row_value[2]), int(row_value[3]), int(row_value[4])]
    
root = etree.Element('root')
child = etree.SubElement(root, 'students')
child.text = str(student)

comment = '''
学生信息表
"id" : [名字, 数学, 语文, 英文]
'''
comment = etree.Comment(comment)
root.insert(0, comment)

et = etree.ElementTree(root)
et.write('./student.xml', encoding='utf-8', xml_declaration=True, pretty_print=True)