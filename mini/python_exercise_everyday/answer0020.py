#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""


from xlrd import open_workbook
from datetime import datetime, timedelta


wb = open_workbook('./OneMonthDetail.xls')
ws = wb.sheet_by_index(0)

dt = datetime(2021, 1, 1, 0, 0, 0)
for cur_row in range(1, ws.nrows):
    x = ws.cell(cur_row, 4).value
    x = int(x * 24 * 3600)
    delta = timedelta(hours = x // 3600, minutes = (x % 3600) // 60, seconds = x % 60)
    dt += delta
    
print(dt.time())