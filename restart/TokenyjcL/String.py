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
from restart.TokenyjcL.Token_yjcL import TokenyjcL


class String(TokenyjcL):
    def __init__(self,value):
        self.type_="STRING"
        self.value=value
