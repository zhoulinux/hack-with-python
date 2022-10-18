'''
http://www.pythonchallenge.com/pc/return/evil.html

only evil1.jpg, change to evil2.jpg
and evil2.jpg shows evil2.gfx
deal with evil2.gfx we get dis, pro, port, ional
http://www.pythonchallenge.com/pc/return/disproportional.html

but we need to move forward to solve next problem.
evil3.jpg shows 'no more evils'
evil4.jpg cannot be displayed, so we use other tools to read it:
$ curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
Bert is evil! go back!
'''


data = open('evil2.gfx', 'rb').read()
for i in range(5):
    open(f'{i}.jpg', 'wb').write(data[i::5])
