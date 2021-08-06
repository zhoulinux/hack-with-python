#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://www.pythonchallenge.com/pc/def/equality.html
"""


import re, requests


page = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
comments = re.findall(r'[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+', page.content.decode())
print(''.join(comments))
# change equality.html to linkedlist.html, then change linkedlist.html to linkedlist.php