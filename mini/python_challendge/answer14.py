'''
http://www.pythonchallenge.com/pc/return/italy.html

walk around
<!-- remember: 100*100 = (100+99+99+98) + (...  -->
<img src="wire.png" width="100" height="100">

http://www.pythonchallenge.com/pc/return/cat.html
'''


from PIL import Image


im = Image.open('wire.png')
# print(im.size)
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = Image.new('RGB', (100, 100))
x, y, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y), im.getpixel((p, 0)))
            p += 1
        d -= 1
out.save('level_14_result.jpg')
