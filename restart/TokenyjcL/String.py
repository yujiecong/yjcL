#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :String.py
@Author   :yujiecong
@Date     :2021/8/31 15:39 
'''
from restart.TokenyjcL.Token import Token_yjcL


class String_yjcL(Token_yjcL):
    def __init__(self,valueDict):
        self.type_=valueDict["type"]
        self.value=valueDict["value"]

