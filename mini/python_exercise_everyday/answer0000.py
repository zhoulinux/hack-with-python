#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype('wqy-microhei.ttc', 48)
fillcolor = '#ff0000'
with Image.open('wechat_avator.png') as f:
    draw = ImageDraw.Draw(f)
    width, height = f.size
    draw.text((width/1.3, height*0.02), '666', fill=fillcolor, font=font)
    f.show()