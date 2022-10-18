'''
replace html with zip to download the files, which I can't think of.
http://www.pythonchallenge.com/pc/def/channel.zip
I lear from this challenge that if I can't think it through for a long
time, it's better to find some new thoughts.

then read the readme.txt for useful info.
hint1: start from 90052
hint2: answer is inside the zip

read txt files successively, and get message:
Collect the comments.

What commemts? No comments in the web page at all.
Ask for help to know that to collect comment of zip files.
Which is out of my knowledge.

go to http://www.pythonchallenge.com/pc/def/hockey.html, get:
it's in the air. look at the letters.

The right answer is in the letters: oxygen.
I can't get it.

http://www.pythonchallenge.com/pc/def/oxygen.html
'''


import zipfile
import re


f = zipfile.ZipFile('channel.zip')
num = '90052'
comments = []
while True:
    content = f.read(num + '.txt').decode()
    comments.append(f.getinfo(num + '.txt').comment.decode())
    # print(content)
    match = re.search(r'Next nothing is (\d+)', content)
    if match is None:
        break
    else:
        num = match.group(1)
print(''.join(comments))
