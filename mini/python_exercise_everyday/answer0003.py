#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""


import random
import redis
from answer0001 import make_promotions


promotion_number = 200
promotion_list = make_promotions(promotion_number)

random.seed(433)
promotions = {f"promotion:{random.getrandbits(32)}": p for p in promotion_list}

r = redis.Redis()
r.flushdb()
with r.pipeline() as pipe:
    for p_id, promotion in promotions.items():
        pipe.hmset(p_id, promotion)
    pipe.execute()
r.bgsave()

for key in r.keys():
    print(r.hgetall(key))