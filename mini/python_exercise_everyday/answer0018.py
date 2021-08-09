#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
    <cities>
    <!-- 
      城市信息
    -->
        {
      "1" : "上海",
      "2" : "北京",
      "3" : "成都"
    }
    </cities>
</root>
"""


from xlrd import open_workbook
from lxml import etree


city = {}

wb = open_workbook('./city.xls')
ws = wb.sheet_by_name('city')
        
for cur_row in range(0, ws.nrows):
    row_value = ws.row_values(cur_row)
    city[row_value[0]] = row_value[1]
    
root = etree.Element('root')
child = etree.SubElement(root, 'cities')
child.text = str(city)

comment = '城市信息'
comment = etree.Comment(comment)
root.insert(0, comment)

et = etree.ElementTree(root)
et.write('./city.xml', encoding='utf-8', xml_declaration=True, pretty_print=True)