#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""


import requests


hints = []
link = (
    'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    '?nothing='
)
s = '12345'

for i in range(0, 400):
    print(f'tring {i} time')
    page = requests.get(link + s)
    s = page.content.decode().split()[-1]
    if not str.isnumeric(s):
        hints.append(s)
    # Added after solving the puzzle.
    if s.endswith('html'):
        break

print(''.join(hints))
# change linkedlist.php to peak.html
# http://www.pythonchallenge.com/pc/def/peak.html
