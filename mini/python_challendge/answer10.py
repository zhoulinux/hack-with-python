'''
http://www.pythonchallenge.com/pc/return/bull.html

http://www.pythonchallenge.com/pc/return/sequence.txt
a = [1, 11, 21, 1211, 111221,

http://www.pythonchallenge.com/pc/return/5808.html
'''


import re


s = '1'
for i in range(30):
    tl = re.findall(r'(\d)(\1*)', s)
    # print(i, '=>', tl)
    s = ''.join([str(len(others) + 1) + digit for digit, others in tl])
    # print(s)
print(len(s))
