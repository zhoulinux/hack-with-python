#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <numbers>
    <!-- 
    	数字信息
    -->
    
    [
        	[1, 82, 65535],
        	[20, 90, 13],
        	[26, 809, 1024]
    ]
    
    </numbers>
</root>
"""


from xlrd import open_workbook
from lxml import etree


numbers = []

wb = open_workbook('./numbers.xls')
ws = wb.sheet_by_name('numbers')
        
for cur_row in range(0, ws.nrows):
    row_value = ws.row_values(cur_row)
    numbers.append([int(n) for n in row_value])
    
root = etree.Element('root')
child = etree.SubElement(root, 'numbers')
child.text = str(numbers)

comment = '''
数字信息'''
comment = etree.Comment(comment)
root.insert(0, comment)

et = etree.ElementTree(root)
et.write('./numbers.xml', encoding='utf-8', xml_declaration=True, pretty_print=True)