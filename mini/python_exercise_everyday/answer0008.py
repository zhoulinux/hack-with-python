#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0008 题： 一个HTML文件，找出里面的正文。
"""


import requests
from lxml import html


page = requests.get('https://docs.python-guide.org/scenarios/scrape/#web-scraping')
tree = html.fromstring(page.content)
texts = tree.xpath('//p/text()')
texts.extend(tree.xpath('//span/text()'))

print(texts)