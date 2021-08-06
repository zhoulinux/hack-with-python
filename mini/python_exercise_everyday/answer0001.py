#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
"""


from datetime import datetime, timezone


def make_promotions(n):
    effective_date = datetime(2021, 8, 1, tzinfo=timezone.utc).isoformat()
    expired_date = datetime(2021, 8, 31, 23, 59, 59, tzinfo=timezone.utc).isoformat()
    amount = 100
    issued = 0
    used = 0
    
    return [{'id': id,
             'effective datetime': effective_date,
             'expired datetime': expired_date,
             'amount': amount,
             'issued': issued,
             'used': used}
            for id in range(0, n)]


promotion_number = 200
promotion_list = make_promotions(promotion_number)
print(promotion_list)