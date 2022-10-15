#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://www.pythonchallenge.com/pc/def/peak.html

<peakhell src="banner.p"/>

<!-- peak hell sounds familiar ? -->
peakhell, peakhell, ..., sounds like pickle,
which is Python's object serialization module.
"""


import requests
import pickle


page = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
p = pickle.loads(page.content)
print(p)

# p is a list of lists of tuple, which includes a character and a number.
with open('./answer5.txt', 'w') as f:
    for li in p:
        for tu in li:
            f.write(tu[0] * tu[1])
        f.write('\n')

# we get channel, so change to channel.html.
# http://www.pythonchallenge.com/pc/def/channel.html
