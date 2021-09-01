#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Identifier.py
@Author   :yujiecong
@Date     :2021/8/31 15:39 
'''
from restart.TokenyjcL.Token import Token_yjcL


class Identifier_yjcL(Token_yjcL):
    def __init__(self,valueDict):
        super(Identifier_yjcL, self).__init__(valueDict)
