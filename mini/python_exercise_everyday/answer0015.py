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


import json, xlwt


city = {}
with open('./city.txt') as f:
    city = json.loads(f.read())

wb = xlwt.Workbook()
ws = wb.add_sheet('city')

for i, (key, value) in enumerate(city.items()):
    ws.write(i, 0, key)
    ws.write(i, 1, value)
            
wb.save('./city.xls')