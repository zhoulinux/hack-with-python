#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
阅读资料:https://www.pythoncentral.io/hashing-strings-with-python/
"""


import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Please input a password: ')
hashed_password = hash_password(new_pass)
print(f'The string to store in the db is: {hashed_password}')

old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You enter the right password!')
else:
    print('I am sorry but the password does not match.')