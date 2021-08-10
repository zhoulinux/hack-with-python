#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。
"""


import os
from PIL import Image


def resize_images(imageDir, resizeHeight, resizeWidth):
    '''
    Parameters
    ----------
    imageDir : str
        The directory of images to be resized.
    resizeHeight : float
        The target height in inch.
    resizeWidth : float
        The target width in inch.

    Returns
    -------
    None.

    '''
    
    fixed_height, fixed_width = int(resizeHeight * 96), int(resizeWidth * 96)
    
    images = () # record all image names and their absolute paths
    for root, _, files in os.walk(imageDir):
        image_filenames = [f for f in files if not f.startswith('.')]
        images = zip(image_filenames, [os.path.join(root, f) for f in image_filenames])
    
    for name, file in images:
        with Image.open(file) as img:
            img = img.resize((fixed_height, fixed_width), Image.NEAREST)
            img.save(imageDir + 'resized_' + name)
        

iPhoneHeightInch = 4.87
iPhoneWidthInch = 2.31
resize_images('./img/', iPhoneHeightInch, iPhoneWidthInch)