'''
extract from the gray scale, we get:
'smart guy, you made it. the next level is
[105, 110, 116, 101, 103, 114, 105, 116, 121]'
'''


from urllib.request import urlopen
import png
import re


response = urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')

(w, h, rgba, dummy) = png.Reader(response).read()

it = list(rgba)
mid = h // 2
length = len(it[mid])
res = [
    chr(it[mid][i])
    for i in range(0, length, 4 * 7)
    if it[mid][i] == it[mid][i+1] == it[mid][i+2]
]

message = ''.join(res)
numbers = re.findall(r'\d+', message)
integers = map(int, numbers)
print(''.join(map(chr, integers)))
