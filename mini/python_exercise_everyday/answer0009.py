#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0009 题： 一个HTML文件，找出里面的链接。
"""


import requests, re
from lxml import html


page = requests.get('https://docs.python-guide.org/scenarios/scrape/#web-scraping')
tree = html.fromstring(page.content)
links = tree.xpath('//a/@href')
hlinks = [link for link in links if re.match(r'^http', link)]
print(hlinks)