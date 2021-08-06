#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

I replace MySQL with sqllite.
"""


import sqlite3
from answer0001 import make_promotions


def write_promotion_list_to_sqllite(promotion_list):
    with sqlite3.connect('promotion.db') as con:
        cur = con.cursor()
        cur.execute('''
                    DROP TABLE promotion
                    ''')
        cur.execute('''
                    CREATE TABLE promotion
                    (id int,
                     'effective datetime' text,
                     'expired datetime' text,
                     amount real,
                     issued int,
                     used int)
                    ''')
        for promotion in promotion_list:
            cur.execute('''INSERT INTO promotion
                        ('id', 'effective datetime', 'expired datetime', 'amount', 'issued', 'used')
                        VALUES (?, ?, ?, ?, ?, ?)''',
                        (promotion['id'],
                         promotion['effective datetime'],
                         promotion['expired datetime'],
                         promotion['amount'],
                         promotion['issued'],
                         promotion['used']))
        con.commit()


promotion_number = 200
promotion_list = make_promotions(promotion_number)
write_promotion_list_to_sqllite(promotion_list)

