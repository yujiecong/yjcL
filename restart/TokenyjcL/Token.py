#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@IDE      :PyCharm
@Project  :yjcL 
@USER     :yanyin
@File     :Token_yjcL.py
@Author   :yujiecong
@Date     :2021/8/31 15:38 
'''
import restart.Global.Variable
from restart.Enum.Enum import TokenType


class TokenyjcL:
    @staticmethod
    def getValue(valueDict):
        type_=valueDict["type"]
        value=valueDict["value"]

        if type_==TokenType.String:
            return value
        if type_==TokenType.Number:
            return value
        if type_==TokenType.Identifier:
            return restart.Global.Variable.GlobalVariable.__var__[value]

