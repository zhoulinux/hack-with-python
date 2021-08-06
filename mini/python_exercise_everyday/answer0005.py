#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小（123.8 x 58.6 mm 或 4.87 x 2.31 in)。
1 inch = 96 pixel
"""


import os
from PIL import Image


iPhone_height_inch = 4.87
iPhone_width_inch = 2.31
fixed_height, fixed_width = int(iPhone_height_inch * 96), int(iPhone_width_inch * 96)

images = () # record all image names and their absolute paths
for root, _, files in os.walk('./img/'):
    image_filenames = [f for f in files if not f.startswith('.')]
    images = zip(image_filenames, [os.path.join(root, f) for f in image_filenames])

for name, file in images:
    with Image.open(file) as img:
        img = img.resize((fixed_height, fixed_width), Image.NEAREST)
        img.save('./img/' + 'resized_' + name)