#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
"""


import random
import string
from PIL import Image, ImageDraw, ImageFont


text = []
for i in range(4):
    text.extend(random.choice(string.ascii_uppercase))
text = ' '.join(text)

width, height = 200, 100
font = ImageFont.truetype('wqy-microhei.ttc', size=48)
with Image.new('RGB', (width, height)) as img:
    canvas = ImageDraw.Draw(img)
    canvas.text((25, 20), text, font=font, fill='#FFFFFF')
    img.show()