#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""


from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype('wqy-microhei.ttc', 48)
fillcolor = '#ff0000'
with Image.open('wechat_avator.png') as f:
    draw = ImageDraw.Draw(f)
    width, height = f.size
    draw.text((width/1.3, height*0.02), '666', fill=fillcolor, font=font)
    f.show()