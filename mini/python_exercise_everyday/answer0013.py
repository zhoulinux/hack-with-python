#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0013 题： 用 Python 写一个爬图片的程序，爬这个链接里的图片.
http://tieba.baidu.com/p/2166231880

The link above is obselete, so I download comic images from xkcd.com.
"""


import requests, bs4, os, logging, traceback
logging.basicConfig(filename='downloadXkcdLog.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

print('Start.')
try:
    url = 'http://xkcd.com'             # starting url
    os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

    names = []
    for root, dirs, files in os.walk('xkcd'):
        for file in files:
            path = os.path.join(root, file)
            names.append(path)

    # while not url.endswith('#'): # down load all images
    for i in range(5):
        # Download the page
        print('Downloading page %s...' % url)
        logging.info('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features='lxml')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
            logging.warning('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Check if the image file already exists.
            imagePath = os.path.join('./xkcd', os.path.basename(comicUrl))
            if imagePath in names:
                continue

            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            logging.info('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            with open(imagePath, 'wb') as img:
                for chunk in res.iter_content(100000):
                    img.write(chunk)

        # Get the prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
except:
    with open('errorInfo.txt', 'w') as errorFile:
        errorFile.write(traceback.format_exc())
print('Done.')