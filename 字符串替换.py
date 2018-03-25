# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:17:50 2018

@author: Lenovo
"""


def replaceSpace(s):
    new_s = ' '
    for i in s:
        if i != ' ':
            new_s = new_s+(i)
        else:
            new_s = new_s+("%20")
    return new_s