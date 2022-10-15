#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import string


if __name__ == '__main__':
    text = (
        "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
        "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm "
        "jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    )

    table = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    )
    print(text.translate(table))
    print('map'.translate(table))
    # change map.html to ocr.html to next level
    # http://www.pythonchallenge.com/pc/def/ocr.html
