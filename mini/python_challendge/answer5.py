#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http://www.pythonchallenge.com/pc/def/peak.html

<peakhell src="banner.p"/>

<!-- peak hell sounds familiar ? -->
peakhell, peakhell, ..., sounds like pickle, which is Python's object serialization module.
"""


import requests, pickle


page = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
p = pickle.loads(page.content) 

# p is a list of lists of tuple, which includes a character and a number.
with open('./answer5.txt', 'w') as f:
    for l in p:
        for t in l:
            f.write(t[0] * t[1])
        f.write('\n')
        
# we get channel, so change to channel.html.