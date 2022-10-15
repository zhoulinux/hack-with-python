#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""


import requests
import re


page = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
comment = re.findall(r'<!--(.*?)-->', page.content.decode(), re.DOTALL)[-1]
print(''.join(re.findall(r'[a-zA-Z]', comment)))
# equality
# http://www.pythonchallenge.com/pc/def/equality.html
